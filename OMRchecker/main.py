from glob import glob
from csv import QUOTE_NONNUMERIC
from time import localtime, strftime, time

import re
import os
import cv2
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Local globals
from django.conf import settings
from django.core.files import File
from django.forms import model_to_dict

from OMRchecker import config, utils
from OMRchecker.template import Template
# from sqlalchemy import create_engine

from posts.admin import MarksForm
from posts.models import ProcessedMarks, ProcessedMarks100
from posts.utils import get_marks_from_dict, get_student, save_processed_marks, get_exam, get_exam100

filesMoved = 0
filesNotMoved = 0

mark_class = MarksForm()


# TODO(beginner task) :-
# from colorama import init
# init()
# from colorama import Fore, Back, Style

# def student_id_to_email(student_id):
#     disk_engine = create_engine('sqlite:///db.sqlite3')
#     df2 = pd.read_sql_table('posts_student', disk_engine)
#     df2 = df2.loc[df2['student_id'] == student_id]
#     studentemail = df2.iat[0, 3]
#
#     return studentemail


def process_dir(root_dir, subdir, template):
    print(root_dir)
    print('-'*10, 'root_dir')
    exam_title = root_dir.rsplit('/', 2)[1]
    print(exam_title)
    print('-'*10, 'root_dir')
    curr_dir = os.path.join(root_dir, subdir)

    # Look for template in current dir
    template_file = os.path.join(curr_dir, config.TEMPLATE_FILE)
    if os.path.exists(template_file):
        template = Template(template_file)

    # look for images in current dir to process
    print(args['output_dir'])
    print('--------------------args[\'output_dir\']------------------')
    paths = config.Paths(os.path.join(args['output_dir']))
    exts = ('*.png', '*.jpg')
    omr_files = sorted(
        [f for ext in exts for f in glob(os.path.join(curr_dir, ext))])

    # Exclude marker image if exists
    if template and template.marker_path:
        omr_files = [f for f in omr_files if f != template.marker_path]

    sub_folders = sorted([file for file in os.listdir(
        curr_dir) if os.path.isdir(os.path.join(curr_dir, file))])
    if omr_files:
        args_local = args.copy()
        if "OverrideFlags" in template.options:
            args_local.update(template.options["OverrideFlags"])
        print('\n------------------------------------------------------------------')
        print(f'Processing directory "{curr_dir}" with settings- ')
        print("\tTotal images       : %d" % (len(omr_files)))
        print("\tCropping Enabled   : " + str(not args_local["noCropping"]))
        print("\tAuto Alignment     : " + str(args_local["autoAlign"]))
        print("\tUsing Template     : " + str(template.path) if (template) else "N/A")
        print("\tUsing Marker       : " + str(template.marker_path)
              if (template.marker is not None) else "N/A")
        print('')

        if not template:
            print(f'Error: No template file when processing {curr_dir}.')
            print(f'  Place {config.TEMPLATE_FILE} in the directory or specify a template using -t.')
            return

        utils.setup_dirs(paths)
        output_set = setup_output(paths, template)
        print(output_set)
        print('------------------output_set--------------')
        process_files(omr_files, template, args_local, output_set, exam_title)
    elif len(sub_folders) == 0:
        # the directory should have images or be non-leaf
        print(f'Note: No valid images or subfolders found in {curr_dir}')

    # recursively process subfolders
    for folder in sub_folders:
        process_dir(root_dir, os.path.join(subdir, folder), template)


def insert_to_db(exam_title, response, file_name):
    # s = exam_title
    # s = s.replace('\\', '/')
    # start = 'outputs/'
    # end = '/sheets/CheckedOMRs/'
    # title = (s.split(start))[1].split(end)[0]
    # savepath = title
    #
    # if title.find('/') != -1:
    #     start2 = '/'
    #     end2 = '/'
    #     exam_name = (title.split(start2))[1].split(end2)[0]
    #     savepath = title
    #     title = exam_name

    # file_name = 'outputs/' + savepath + '/sheets/CheckedOMRs/' + file_name

    marks_dataset = get_marks_from_dict(data=response)

    student = get_student(student_id=response.get('Roll'))

    if len(marks_dataset) == 40:
        processed_marks, created = ProcessedMarks.objects.get_or_create(exam_title=exam_title)
        save_processed_marks(instance=processed_marks, processed_marks=marks_dataset)
        processed_marks.student_id = student.student_id
        processed_marks.student_name = student.student_name
        processed_marks.processed_image = '/40/' + exam_title + '/output/' + file_name

        # final marks
        exam_marks = get_marks_from_dict(
            data=model_to_dict(get_exam(exam_title=exam_title))
        )
        processed_marks.final_marks = mark_class.count_final_marks(
            processed_marks=marks_dataset,
            exam_marks=exam_marks
        )

        processed_marks.save()

    elif len(marks_dataset) == 100:
        processed_marks, created = ProcessedMarks100.objects.get_or_create(exam_title=exam_title)
        save_processed_marks(instance=processed_marks, processed_marks=marks_dataset)
        processed_marks.student_id = student.student_id
        processed_marks.student_name = student.student_name
        processed_marks.processed_image = '/100/' + exam_title + '/output/' + file_name

        # final marks
        exam_marks = get_marks_from_dict(
            data=model_to_dict(get_exam100(exam_title=exam_title))
        )
        processed_marks.final_marks = mark_class.count_final_marks(
            processed_marks=marks_dataset,
            exam_marks=exam_marks
        )
        processed_marks.save()


def checkAndMove(error_code, filepath, filepath2):
    # print("Dummy Move:  "+filepath, " --> ",filepath2)
    global filesNotMoved
    filesNotMoved += 1
    return True

    global filesMoved
    if not os.path.exists(filepath):
        print('File already moved')
        return False
    if os.path.exists(filepath2):
        print('ERROR : Duplicate file at ' + filepath2)
        return False

    print("Moved:  " + filepath, " --> ", filepath2)
    os.rename(filepath, filepath2)
    filesMoved += 1
    return True


def processOMR(template, omrResp):
    # Note: This is a reference function. It is not part of the OMR checker
    # So its implementation is completely subjective to user's requirements.
    csvResp = {}

    # symbol for absent response
    UNMARKED_SYMBOL = ''

    # print("omrResp",omrResp)

    # Multi-column/multi-row questions which need to be concatenated
    for qNo, respKeys in template.concats.items():
        csvResp[qNo] = ''.join([omrResp.get(k, UNMARKED_SYMBOL)
                                for k in respKeys])

    # Single-column/single-row questions
    for qNo in template.singles:
        csvResp[qNo] = omrResp.get(qNo, UNMARKED_SYMBOL)

    # Note: Concatenations and Singles together should be mutually exclusive
    # and should cover all questions in the template(exhaustive)
    # TODO: ^add a warning if omrResp has unused keys remaining
    return csvResp


def report(status, streak, scheme, q_no, marked, ans, prev_marks, curr_marks, marks):
    print(
        '%s \t %s \t\t %s \t %s \t %s \t %s \t %s ' % (
            q_no,
            status,
            str(streak),
            '[' + scheme + '] ',
            (str(prev_marks) + ' + ' + str(curr_marks) + ' =' + str(marks)),
            str(marked),
            str(ans)
        )
    )


# check sectionwise only.


def evaluate(resp, squad="H", explain=False):
    # TODO: @contributors - Need help generalizing this function
    global Answers, Sections

    marks = 0
    answers = Answers[squad]
    if explain:
        print('Question\tStatus \t Streak\tSection \tMarks_Update\tMarked:\tAnswer:')
    for scheme, section in Sections[squad].items():
        sectionques = section['ques']
        prevcorrect = None
        allflag = 1
        streak = 0
        for q in sectionques:
            qNo = 'q' + str(q)
            ans = answers[qNo]
            marked = resp.get(qNo, 'X')
            firstQ = sectionques[0]
            lastQ = sectionques[len(sectionques) - 1]
            unmarked = marked == 'X' or marked == ''
            bonus = 'BONUS' in ans
            correct = bonus or (marked in ans)
            inrange = 0

            if unmarked or int(q) == firstQ:
                streak = 0
            elif prevcorrect == correct:
                streak += 1
            else:
                streak = 0

            if 'allNone' in scheme:
                # loop on all sectionques
                allflag = allflag and correct
                if (q == lastQ):
                    # at the end check allflag
                    prevcorrect = correct
                    currmarks = section['marks'] if allflag else 0
                else:
                    currmarks = 0

            elif 'Proxy' in scheme:
                a = int(ans[0])
                # proximity check
                inrange = 1 if unmarked else (
                        float(abs(int(marked) - a)) / float(a) <= 0.25)
                currmarks = section['+marks'] if correct else (
                    0 if inrange else -section['-marks'])

            elif ('Fibo' in scheme or 'Power' in scheme or 'Boom' in scheme):
                currmarks = section['+seq'][streak] if correct else (
                    0 if unmarked else -section['-seq'][streak])
            elif ('TechnoFin' in scheme):
                currmarks = 0
            else:
                print('Invalid Sections')
            prevmarks = marks
            marks += currmarks

            if explain:
                if bonus:
                    report('BonusQ', streak, scheme, qNo, marked,
                           ans, prevmarks, currmarks, marks)
                elif correct:
                    report('Correct', streak, scheme, qNo, marked,
                           ans, prevmarks, currmarks, marks)
                elif unmarked:
                    report('Unmarked', streak, scheme, qNo, marked,
                           ans, prevmarks, currmarks, marks)
                elif inrange:
                    report('InProximity', streak, scheme, qNo,
                           marked, ans, prevmarks, currmarks, marks)
                else:
                    report('Incorrect', streak, scheme, qNo,
                           marked, ans, prevmarks, currmarks, marks)

            prevcorrect = correct

    return marks


def setup_output(paths, template):
    ns = argparse.Namespace()
    print("\nChecking Files...")

    # Include current output paths
    ns.paths = paths

    # custom sort: To use integer order in question names instead of
    # alphabetical - avoids q1, q10, q2 and orders them q1, q2, ..., q10
    ns.respCols = sorted(list(template.concats.keys()) + template.singles,
                         key=lambda x: int(x[1:]) if ord(x[1]) in range(48, 58) else 0)
    ns.emptyResp = [''] * len(ns.respCols)
    ns.sheetCols = ['file_id', 'input_path',
                    'output_path', 'score'] + ns.respCols
    ns.OUTPUT_SET = []
    ns.filesObj = {}
    return ns


''' TODO: Refactor into new process flow.
    Currently I have no idea what this does so I left it out'''


def preliminary_check():
    pass
    # filesCounter=0
    # mws, mbs = [],[]
    # # PRELIM_CHECKS for thresholding
    # if(config.PRELIM_CHECKS):
    #     # TODO: add more using unit testing
    #     TEMPLATE = TEMPLATES["H"]
    #     ALL_WHITE = 255 * np.ones((TEMPLATE.dims[1],TEMPLATE.dims[0]), dtype='uint8')
    #     OMRresponseDict,final_marked,MultiMarked,multiroll = readResponse("H",ALL_WHITE,name = "ALL_WHITE", savedir = None, autoAlign=True)
    #     print("ALL_WHITE",OMRresponseDict)
    #     if(OMRresponseDict!={}):
    #         print("Preliminary Checks Failed.")
    #         exit(2)
    #     ALL_BLACK = np.zeros((TEMPLATE.dims[1],TEMPLATE.dims[0]), dtype='uint8')
    #     OMRresponseDict,final_marked,MultiMarked,multiroll = readResponse("H",ALL_BLACK,name = "ALL_BLACK", savedir = None, autoAlign=True)
    #     print("ALL_BLACK",OMRresponseDict)
    #     show("Confirm : All bubbles are black",final_marked,1,1)


def process_files(omr_files, template, args, out, exam_title):
    start_time = int(time())
    filesCounter = 0
    filesNotMoved = 0

    for filepath in omr_files:
        filesCounter += 1
        # For windows filesystem support: all '\' will be replaced by '/'
        filepath = filepath.replace(os.sep, '/')

        # Prefixing a 'r' to use raw string (escape character '\' is taken
        # literally)
        finder = re.search(r'.*/(.*)/(.*)', filepath, re.IGNORECASE)
        if finder:
            inputFolderName, filename = finder.groups()
        else:
            print("Error: Filepath not matching to Regex: " + filepath)
            continue
        # set global var for reading

        inOMR = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        print(
            '\n[%d] Processing image: \t' %
            (filesCounter),
            filepath,
            "\tResolution: ",
            inOMR.shape)

        OMRCrop = utils.getROI(inOMR, filename, noCropping=args["noCropping"])

        if OMRCrop is None:
            # Error OMR - could not crop
            newfilepath = out.paths.errorsDir + filename
            out.OUTPUT_SET.append([filename] + out.emptyResp)
            if checkAndMove(config.NO_MARKER_ERR, filepath, newfilepath):
                err_line = [filename, filepath,
                            newfilepath, "NA"] + out.emptyResp
                pd.DataFrame(
                    err_line,
                    dtype=str).T.to_csv(
                    out.filesObj["Errors"],
                    quoting=QUOTE_NONNUMERIC,
                    header=False,
                    index=False)
            continue

        if template.marker is not None:
            OMRCrop = utils.handle_markers(OMRCrop, template.marker, filename)

        if args["setLayout"]:
            templateLayout = utils.drawTemplateLayout(
                OMRCrop, template, shifted=False, border=2)
            utils.show("Template Layout", templateLayout, 1, 1)
            continue

        # uniquify
        # file_id = inputFolderName + '_' + filename
        file_id = filename
        savedir = out.paths.saveMarkedDir
        OMRresponseDict, final_marked, MultiMarked, multiroll = \
            utils.readResponse(template, OMRCrop, name=file_id,
                               savedir=savedir, autoAlign=args["autoAlign"])

        # concatenate roll nos, set unmarked responses, etc
        resp = processOMR(template, OMRresponseDict)
        print("\nRead Response: \t", resp)

        # This evaluates and returns the score attribute
        insert_to_db(exam_title, resp, file_id)
        # TODO: Automatic scoring
        # score = evaluate(resp, explain=explain)
        score = 0

        respArray = []
        for k in out.respCols:
            respArray.append(resp[k])

        out.OUTPUT_SET.append([filename] + respArray)

        # TODO: Add roll number validation here
        if MultiMarked == 0:
            filesNotMoved += 1
            newfilepath = savedir + file_id
            # Enter into Results sheet-
            results_line = [filename, filepath, newfilepath, score] + respArray
            # Write/Append to results_line file(opened in append mode)
            # pd.DataFrame(
            #     results_line,
            #     dtype=str).T.to_csv(
            #     out.filesObj["Results"],
            #     quoting=QUOTE_NONNUMERIC,
            #     header=False,
            #     index=False)
            # print("[%d] Graded with score: %.2f" %
            #       (filesCounter, score), '\t file_id: ', file_id)
            # print(filesCounter,file_id,resp['Roll'],'score : ',score)

    timeChecking = round(time() - start_time, 2) if filesCounter else 1
    print('')
    print('Total files moved        : %d ' % filesMoved)
    print('Total files not moved    : %d ' % filesNotMoved)
    print('------------------------------')
    print(
        'Total files processed    : %d (%s)' %
        (filesCounter,
         'Sum Tallied!' if filesCounter == (
                 filesMoved +
                 filesNotMoved) else 'Not Tallying!'))

    if config.showimglvl <= 0:
        print(
            '\nFinished Checking %d files in %.1f seconds i.e. ~%.1f minutes.' %
            (filesCounter, timeChecking, timeChecking / 60))
        print('OMR Processing Rate  :\t ~ %.2f seconds/OMR' %
              (timeChecking / filesCounter))
        print('OMR Processing Speed :\t ~ %.2f OMRs/minute' %
              ((filesCounter * 60) / timeChecking))
    else:
        print("\nTotal script time :", timeChecking, "seconds")

    if config.showimglvl <= 1:
        # TODO: colorama this
        print(
            "\nTip: To see some awesome visuals, open globals.py and increase 'showimglvl'")

    # evaluate_correctness(template, out)

    # Use this data to train as +ve feedback
    if config.showimglvl >= 0 and filesCounter > 10:
        for x in [utils.thresholdCircles]:  # ,badThresholds,veryBadPoints, mws, mbs]:
            if x != []:
                x = pd.DataFrame(x)
                print(x.describe())
                plt.plot(range(len(x)), x)
                plt.title("Mystery Plot")
                plt.show()
            else:
                print(x)


# Evaluate accuracy based on OMRDataset file generated through moderation
# portal on the same set of images
def evaluate_correctness(template, out):
    # TODO: TEST_FILE WOULD BE RELATIVE TO INPUT SUBDIRECTORY NOW-
    TEST_FILE = 'inputs/OMRDataset.csv'
    if os.path.exists(TEST_FILE):
        print("\nStarting evaluation for: " + TEST_FILE)

        TEST_COLS = ['file_id'] + out.respCols
        y_df = pd.read_csv(
            TEST_FILE, dtype=str)[TEST_COLS].replace(
            np.nan, '', regex=True).set_index('file_id')

        if np.any(y_df.index.duplicated):
            y_df_filtered = y_df.loc[~y_df.index.duplicated(keep='first')]
            print(
                "WARNING: Found duplicate File-ids in file %s. Removed %d rows from testing data. Rows remaining: %d" %
                (TEST_FILE, y_df.shape[0] - y_df_filtered.shape[0], y_df_filtered.shape[0]))
            y_df = y_df_filtered

        x_df = pd.DataFrame(
            out.OUTPUT_SET,
            dtype=str,
            columns=TEST_COLS).set_index('file_id')
        # print("x_df",x_df.head())
        # print("\ny_df",y_df.head())
        intersection = y_df.index.intersection(x_df.index)

        # Checking if the merge is okay
        if intersection.size == x_df.index.size:
            y_df = y_df.loc[intersection]
            x_df['TestResult'] = (x_df == y_df).all(axis=1).astype(int)
            print(x_df.head())
            print("\n\t Accuracy on the %s Dataset: %.6f" %
                  (TEST_FILE, (x_df['TestResult'].sum() / x_df.shape[0])))
        else:
            print(
                "\nERROR: Insufficient Testing Data: Have you appended MultiMarked data yet?")
            print("Missing File-ids: ",
                  list(x_df.index.difference(intersection)))


timeNowHrs = strftime("%I%p", localtime())

# construct the argument parse and parse the arguments
argparser = argparse.ArgumentParser()
# https://docs.python.org/3/howto/argparse.html
# store_true: if the option is specified, assign the value True to
# args.verbose. Not specifying it implies False.
argparser.add_argument(
    "-c",
    "--noCropping",
    required=False,
    dest='noCropping',
    action='store_true',
    help="Disables page contour detection - used when page boundary is not visible e.g. document scanner.")
argparser.add_argument(
    "-a",
    "--autoAlign",
    required=False,
    dest='autoAlign',
    action='store_true',
    help="(experimental) Enables automatic template alignment - use if the scans show slight misalignments.")
argparser.add_argument(
    "-l",
    "--setLayout",
    required=False,
    dest='setLayout',
    action='store_true',
    help="Set up OMR template layout - modify your json file and run again until the template is set.")
argparser.add_argument("-i", "--inputDir", required=False, action='append',
                       dest='input_dir', help="Specify an input directory.")
argparser.add_argument("-o", "--outputDir", default='outputs', required=False,
                       dest='output_dir', help="Specify an output directory.")
argparser.add_argument(
    "-t",
    "--template",
    required=False,
    dest='template',
    help="Specify a default template if no template file in input directories.")

args, unknown = argparser.parse_known_args()
args = vars(args)


# if len(unknown) > 0:
#     print("\nError: Unknown arguments:", unknown)
#     argparser.print_help()
#     exit(11)
#
# if args['template']:
#     args['template'] = Template(args['template'])
#
# if args['input_dir'] is None:
#     args['input_dir'] = ['inputs']
#
# for root in args['input_dir']:
#     process_dir(root, '', args['template'])


# integration

class OMRChecker:
    def __init__(self, input_dir: list, output_dir: str):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def execute(self):
        if args['template']:
            args['template'] = Template(args['template'])

        args['input_dir'] = self.input_dir
        args['output_dir'] = self.output_dir

        for root in args['input_dir']:
            print('------------------rooooooot--------------------')
            print(root)
            process_dir(root, '', args['template'])
