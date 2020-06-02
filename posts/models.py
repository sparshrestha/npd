from django.db import models
from django.conf import settings
import os


def sheet_upload_location(instance, filename):
    file_path = 'images/{exam_name}/sheets/{filename}'.format(exam_name=str(instance.title), filename=filename
                                                              )
    return file_path


def template_upload_location(instance, filename):  # removing empty media folders and get upload location
    file_path = 'images/{exam_name}/{filename}'.format(exam_name=str(instance.title), filename=filename
                                                       )
    media_root = getattr(settings, 'MEDIA_ROOT', None)
    for relative_root, dirs, files in os.walk(media_root, topdown=False):
        for dir_ in dirs:
            if not os.listdir(os.path.join(relative_root, dir_)):
                os.rmdir(os.path.join(relative_root, dir_))
    return file_path


class Exams(models.Model):
    class Meta: verbose_name_plural = 'Exams Record'

    title = models.CharField(max_length=20)
    cover = models.ImageField(upload_to=sheet_upload_location)
    template = models.FileField(upload_to=template_upload_location, default=None)
    marker = models.ImageField(upload_to=template_upload_location, null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    class Meta: verbose_name_plural = 'Students Record'

    student_id = models.CharField(max_length=8, default='')
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=200)

    def __str__(self):
        return self.student_id


class ProcessedMarks(models.Model):
    class Meta: verbose_name_plural = 'Processed Marks'

    exam_title = models.CharField(max_length=20)
    student_id = models.CharField(max_length=8, default='')
    raw_marks = models.CharField(max_length=300)

    def __str__(self):
        return self.student_id
