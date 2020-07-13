from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy, reverse

from GFoody.settings import BASE_DIR
from OMRchecker import OMRChecker
from .forms import Exams100Form, ExamsForm
from .models import Exams100, Exams, Student, ProcessedMarks
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from sqlalchemy import create_engine
import sqlite3
import numpy as np
import pandas as pd
import re
import os
import cv2

class HomePage(ListView):
    model = Student
    template_name = 'process.html'


class HomePageView(ListView):
    model = Exams
    template_name = 'processexam.html'


class HomePageView100(ListView):
    model = Exams100
    template_name = 'processexam100.html'


class HomePageProcessed(ListView):
    model = ProcessedMarks
    template_name = 'processed.html'


def process_image(request, exam_name):
    print('----------called-------')
    OMRChecker(input_dir=[BASE_DIR + '/media/images/40/' + exam_name]).execute()
    return HttpResponseRedirect(reverse('home40'))


def feedback_exams(request, processed_id):
    print('----------called-------')
    print(processed_id)
    processed_id = int(processed_id)
    disk_engine = create_engine('sqlite:///db.sqlite3')
    df2 = pd.read_sql_table('posts_processedmarks', disk_engine)
    new = df2[['id', 'student_id', 'exam_title', 'student_name','processed_image','final_marks']]
    print(new)

    sname = new.loc[new.id == processed_id, 'student_name'].values[0]
    print(sname)
    sid = new.loc[new.id == processed_id, 'student_id'].values[0]
    print(sid)
    exam_name = new.loc[new.id == processed_id, 'exam_title'].values[0]
    print(exam_name)
    output_image = new.loc[new.id == processed_id, 'processed_image'].values[0]
    attach_file = 'media/' + output_image
    print(attach_file)
    f_marks = new.loc[new.id == processed_id, 'final_marks'].values[0]
    print(f_marks)
    subject = sid + " " + sname + " " + exam_name
    body = "Final marks for" + sid + " " + sname + " " + exam_name + " is " + f_marks + " " + "check attached answer " \
                                                                                        "sheet for confirmation "

    email = EmailMessage(
        subject,
        body,
        'admin@npd.com.np',
        ['narayan.adhikari60@gmail.com'],
        ['narayan.adhikari60@gmail.com'],
        headers={'Message-ID': 'foo'},
    )
    email.attach_file(attach_file)
    email.send()
    print('email sent')

    return HttpResponseRedirect(reverse('processed40'))


def feedback_exams_all(request):
    print('----------called-------')
    print("Process All Feedback")
    return HttpResponseRedirect(reverse('processed40'))


def process_all_exam(request):
    print('----------called-------')
    OMRChecker(input_dir=[BASE_DIR + '/media/images/40/']).execute()
    return HttpResponseRedirect(reverse('home40'))


def process_image100(request, exam_name):
    print('----------called-------')
    OMRChecker(input_dir=[BASE_DIR + '/media/images/100/' + exam_name]).execute()
    return HttpResponseRedirect(reverse('home100'))


def process_all_exam100(request):
    print('----------called-------')
    OMRChecker(input_dir=[BASE_DIR + '/media/images/100/']).execute()
    return HttpResponseRedirect(reverse('home100'))


class CreateExamView(CreateView):
    model = Exams
    form_class = ExamsForm
    template_name = 'exam.html'
    success_url = reverse_lazy('home')


class CreateExamView100(CreateView):
    model = Exams100
    form_class = Exams100Form
    template_name = 'exam100.html'
    success_url = reverse_lazy('home100')
