from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView

from OMRchecker import OMRChecker
from .forms import Exams100Form, ExamsForm
from .mixins import Exam40Mixin, Exam100Mixin
from .models import Exams100, Exams, Student, ProcessedMarks
from .usecases import (
    ProcessAllExamsUseCase,
    SendExamFeedbackUseCase,
    SendExam100FeedbackUseCase,
    DownloadExamExcelReportUseCase,
    DownloadExam100ExcelReportUseCase
)


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
    OMRChecker(
        input_dir=[settings.MEDIA_ROOT + '/40/' + exam_name + '/input'],
        output_dir=settings.MEDIA_ROOT + '/40/' + exam_name + '/output'
    ).execute()
    return HttpResponseRedirect(reverse('home40'))


def feedback_exams_all(request):
    print('----------called-------')
    print("Process All Feedback")
    return HttpResponseRedirect(reverse('processed40'))


def process_all_exam(request):
    print('----------called-------')
    ProcessAllExamsUseCase(folder=settings.MEDIA_ROOT + '/40').execute()
    # OMRChecker(input_dir=[settings.MEDIA_ROOT + '/40/']).execute()
    return HttpResponseRedirect(reverse('home40'))


def process_image100(request, exam_name):
    print('----------called-------')
    OMRChecker(
        input_dir=[settings.MEDIA_ROOT + '/100/' + exam_name + '/input'],
        output_dir=settings.MEDIA_ROOT + '/100/' + exam_name + '/output'
    ).execute()
    # OMRChecker(input_dir=[BASE_DIR + '/media/images/100/' + exam_name]).execute()
    return HttpResponseRedirect(reverse('home100'))


def process_all_exam100(request):
    print('----------called-------')
    ProcessAllExamsUseCase(folder=settings.MEDIA_ROOT + '/100').execute()
    # OMRChecker(input_dir=[BASE_DIR + '/media/images/100/']).execute()
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


def retotal_processed40(request):
    print(request)
    print('afasssssssssssssssssssssssss')


def process_exam(request, exam_id):
    try:
        exam = Exams.objects.get(pk=exam_id)
    except Exams.DoesNotExist:
        raise ValidationError('Invalid Exam Id.')
    OMRChecker(
        input_dir=[settings.MEDIA_ROOT + '/40/' + exam.title + '/input'],
        output_dir=settings.MEDIA_ROOT + '/40/' + exam.title + '/output'
    ).execute()
    return HttpResponseRedirect('/posts/exams')


class SendExamFeedbackView(View, Exam40Mixin):
    def get(self, *args, **kwargs):
        SendExamFeedbackUseCase(
            exam=self.get_exam()
        ).execute()
        return HttpResponseRedirect('/posts/exams')


class SendExam100FeedbackView(View, Exam100Mixin):
    def get(self, *args, **kwargs):
        SendExam100FeedbackUseCase(
            exam=self.get_exam()
        ).execute()
        return HttpResponseRedirect('/posts/exams100')


class DownloadExamExcelReportView(View, Exam40Mixin):
    def get(self, *args, **kwargs):
        return DownloadExamExcelReportUseCase(
            exam=self.get_exam()
        ).execute()


class DownloadExam100ExcelReportView(View, Exam40Mixin):
    def get(self, *args, **kwargs):
        return DownloadExam100ExcelReportUseCase(
            exam=self.get_exam()
        ).execute()


def process_exam100(request, exam_id):
    try:
        exam = Exams100.objects.get(pk=exam_id)
    except Exams100.DoesNotExist:
        raise ValidationError('Invalid Exam Id.')
    OMRChecker(
        input_dir=[settings.MEDIA_ROOT + '/100/' + exam.title + '/input'],
        output_dir=settings.MEDIA_ROOT + '/100/' + exam.title + '/output'
    ).execute()
    return HttpResponseRedirect('/posts/exams100')
