import os

from django.conf import settings
from django.core.exceptions import ValidationError
from mail_templated import EmailMessage

from OMRchecker import OMRChecker
# from posts.email import ExamFeedbackEmail
from posts.models import Exams, Exams100


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
