import os

import xlwt
from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from mail_templated import EmailMessage

from OMRchecker import OMRChecker
# from posts.email import ExamFeedbackEmail
from posts.models import Exams, Exams100, Student


class ProcessAllExamsUseCase:
    """
    Use this to process all exams at once
    """

    def __init__(self, folder: str):
        self._directory_path = folder

    def execute(self):
        self._factory()

    def _factory(self):
        # 1. get list of sub folder
        exams_folders = os.listdir(self._directory_path)

        # 2. process all exam_folders
        for exam in exams_folders:
            base_dir = '{}/{}'.format(
                self._directory_path,
                exam
            )

            input_dir = '{}/input'.format(
                base_dir
            )
            output_dir = '{}/output'.format(
                base_dir
            )
            OMRChecker(
                input_dir=[input_dir],
                output_dir=output_dir
            ).execute()


class GetExam40UseCase:
    def __init__(self, exam_id: str):
        self._exam_id = exam_id

    def execute(self):
        return self._factory()

    def _factory(self):
        try:
            return Exams.objects.get(pk=self._exam_id)
        except Exams.DoesNotExist:
            raise ValidationError('Invalid Exam Id.')


class GetExam100UseCase:
    def __init__(self, exam_id: str):
        self._exam_id = exam_id

    def execute(self):
        return self._factory()

    def _factory(self):
        try:
            return Exams100.objects.get(pk=self._exam_id)
        except Exams100.DoesNotExist:
            raise ValidationError('Invalid Exam Id.')


class SendExamFeedbackUseCase:
    def __init__(self, exam: Exams):
        self._exam = exam

    def execute(self):
        self._factory()

    def _factory(self):
        processed_marks = self._exam.processedmarks_set.all()
        for marks in processed_marks:
            student = marks.student
            context = {
                'student': student,
                'marks': marks,
            }
            file = 'media/{}'.format(marks.processed_image.name)
            message = EmailMessage('email/exam_feedback.tpl', context, settings.DEFAULT_FROM_EMAIL,
                                   to=[student.student_email])
            message.attach_file(file, 'image/jpg')
            message.send()


class SendExam100FeedbackUseCase:
    def __init__(self, exam: Exams100):
        self._exam = exam

    def execute(self):
        self._factory()

    def _factory(self):
        processed_marks = self._exam.processedmarks100_set.all()
        for marks in processed_marks:
            student = marks.student
            context = {
                'student': student,
                'marks': marks,
            }
            file = 'media/{}'.format(marks.processed_image.name)
            message = EmailMessage('email/exam_feedback.tpl', context, settings.DEFAULT_FROM_EMAIL,
                                   to=[student.student_email])
            message.attach_file(file, 'image/jpg')
            message.send()


class DownloadExamExcelReportUseCase:
    def __init__(self, exam: Exams):
        self._exam = exam

    def execute(self):
        return self._factory()

    def _factory(self):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(self._exam.title)

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(self._exam.title)

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        body_font_style = xlwt.XFStyle()

        ws.write(row_num, row_num, self._exam.title, font_style)
        row_num += 1

        question_lists = ['Q{}'.format(item) for item in range(1, 41)]
        answer_columns = ['Questions', '', ''] + question_lists

        # answer
        row_num += 1
        for col_num, value in enumerate(answer_columns):
            ws.write(row_num, col_num, value, font_style)

        answers = ['Answers', '', ''] + [getattr(self._exam, 'q{}'.format(item)) for item in range(1, 41)]

        row_num += 1
        for col_num, value in enumerate(answers):
            ws.write(row_num, col_num, value, body_font_style)

        row_num += 3

        columns = ['Student Id', 'Student', 'Total Marks'] + question_lists
        for col_num, value in enumerate(columns):
            ws.write(row_num, col_num, value, font_style)

        processed_marks = self._exam.processedmarks_set.all()
        for marks in processed_marks:
            row_num += 1
            student = marks.student
            student_info = [student.student_id, student.student_name, marks.final_marks]
            processed_answers = student_info + [getattr(marks, 'q{}'.format(item)) for item in range(1, 41)]
            for col_num, value in enumerate(processed_answers):
                ws.write(row_num, col_num, processed_answers[col_num], body_font_style)

        wb.save(response)
        return response


class DownloadExam100ExcelReportUseCase:
    def __init__(self, exam: Exams100):
        self._exam = exam

    def execute(self):
        return self._factory()

    def _factory(self):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}.xls"'.format(self._exam.title)

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet(self._exam.title)

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        body_font_style = xlwt.XFStyle()

        ws.write(row_num, row_num, self._exam.title, font_style)
        row_num += 1

        question_lists = ['Q{}'.format(item) for item in range(1, 101)]
        answer_columns = ['Questions', '', ''] + question_lists

        # answer
        row_num += 1
        for col_num, value in enumerate(answer_columns):
            ws.write(row_num, col_num, value, font_style)

        answers = ['Answers', '', ''] + [getattr(self._exam, 'q{}'.format(item)) for item in range(1, 101)]

        row_num += 1
        for col_num, value in enumerate(answers):
            ws.write(row_num, col_num, value, body_font_style)

        row_num += 3

        columns = ['Student Id', 'Student', 'Total Marks'] + question_lists
        for col_num, value in enumerate(columns):
            ws.write(row_num, col_num, value, font_style)

        processed_marks = self._exam.processedmarks100_set.all()
        for marks in processed_marks:
            row_num += 1
            student = marks.student
            student_info = [student.student_id, student.student_name, marks.final_marks]
            processed_answers = student_info + [getattr(marks, 'q{}'.format(item)) for item in range(1, 101)]
            for col_num, value in enumerate(processed_answers):
                ws.write(row_num, col_num, processed_answers[col_num], body_font_style)

        wb.save(response)
        return response
