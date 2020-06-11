from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import os

CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)


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
    marker = models.ImageField(upload_to=template_upload_location, blank=True)
    q1 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q2 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q3 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q4 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q5 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q6 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q7 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q8 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q9 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q10 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q11 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q12 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q13 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q14 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q15 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q16 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q17 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q18 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q19 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q20 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q21 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q22 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q23 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q24 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q25 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q26 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q27 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q28 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q29 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q30 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q31 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q32 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q33 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q34 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q35 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q36 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q37 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q38 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q39 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q40 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    class Meta: verbose_name_plural = 'Students Record'

    student_id = models.CharField(max_length=15, default='')
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name


class ProcessedMarks(models.Model):
    class Meta: verbose_name_plural = 'Processed Marks'

    exam_title = models.CharField(max_length=20)
    student_id = models.CharField(max_length=15, default='')
    student_name = models.CharField(max_length=50, default='')
    processed_image = models.ImageField()
    final_marks = models.CharField(max_length=20, null=True, blank=True)
    q1 = models.CharField(max_length=4, null=True)
    q2 = models.CharField(max_length=4, null=True)
    q3 = models.CharField(max_length=4, null=True)
    q4 = models.CharField(max_length=4, null=True)
    q5 = models.CharField(max_length=4, null=True)
    q6 = models.CharField(max_length=4, null=True)
    q7 = models.CharField(max_length=4, null=True)
    q8 = models.CharField(max_length=4, null=True)
    q9 = models.CharField(max_length=4, null=True)
    q10 = models.CharField(max_length=4, null=True)
    q11 = models.CharField(max_length=4, null=True)
    q12 = models.CharField(max_length=4, null=True)
    q13 = models.CharField(max_length=4, null=True)
    q14 = models.CharField(max_length=4, null=True)
    q15 = models.CharField(max_length=4, null=True)
    q16 = models.CharField(max_length=4, null=True)
    q17 = models.CharField(max_length=4, null=True)
    q18 = models.CharField(max_length=4, null=True)
    q19 = models.CharField(max_length=4, null=True)
    q20 = models.CharField(max_length=4, null=True)
    q21 = models.CharField(max_length=4, null=True)
    q22 = models.CharField(max_length=4, null=True)
    q23 = models.CharField(max_length=4, null=True)
    q24 = models.CharField(max_length=4, null=True)
    q25 = models.CharField(max_length=4, null=True)
    q26 = models.CharField(max_length=4, null=True)
    q27 = models.CharField(max_length=4, null=True)
    q28 = models.CharField(max_length=4, null=True)
    q29 = models.CharField(max_length=4, null=True)
    q30 = models.CharField(max_length=4, null=True)
    q31 = models.CharField(max_length=4, null=True)
    q32 = models.CharField(max_length=4, null=True)
    q33 = models.CharField(max_length=4, null=True)
    q34 = models.CharField(max_length=4, null=True)
    q35 = models.CharField(max_length=4, null=True)
    q36 = models.CharField(max_length=4, null=True)
    q37 = models.CharField(max_length=4, null=True)
    q38 = models.CharField(max_length=4, null=True)
    q39 = models.CharField(max_length=4, null=True)
    q40 = models.CharField(max_length=4, null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width= 40% />'.format(self.processed_image.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return '%s Student %s %s' % (self.exam_title, self.student_id, self.student_name)
