from django.db import models
from django.utils.safestring import mark_safe
from django.core.files import File
import os
from distutils.dir_util import copy_tree

from posts.storage import overwrite_storage
from posts.upload_handlers import (
    upload_exam_cover_to,
    upload_exam_template_to,
    upload_exam_marker_to,
    upload_processed_marks_image_to,
    upload_exam100_cover_to,
    upload_exam100_template_to,
    upload_exam100_marker_to,
    upload_100processed_marks_image_to
)

CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
)


class Exams(models.Model):
    class Meta:
        verbose_name_plural = 'Exams Record 40 Questions'

    title = models.CharField(max_length=20, unique=True)
    cover = models.ImageField(
        upload_to=upload_exam_cover_to,
        storage=overwrite_storage,
        verbose_name="Answer Sheet"
    )
    template = models.FileField(
        upload_to=upload_exam_template_to,
        blank=True,
        storage=overwrite_storage,
        default="template.json"
    )
    marker = models.ImageField(
        upload_to=upload_exam_marker_to,
        blank=True,
        storage=overwrite_storage,
        default="omr_marker.jpg"
    )
    q1 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True, verbose_name="Answer key:Q1")
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

    def save(self, *args, **kwargs):
        if self.template:
            fromDirectory = "media/examtemplate/40/save/"
            toDirectory = os.getcwd()
            copy_tree(fromDirectory, toDirectory)

            djangotemplate = File(open('template.json'))
            self.template = djangotemplate
            djangomarker = File(open('omr_marker.jpg', 'rb'))
            self.marker = djangomarker

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Student(models.Model):
    class Meta:
        verbose_name_plural = 'Students Record'

    student_id = models.CharField(max_length=15, default='')
    student_name = models.CharField(max_length=50)
    student_email = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name


class ProcessedMarks(models.Model):
    class Meta:
        verbose_name_plural = 'Processed Marks'

    exam_title = models.CharField(max_length=20, unique=True)
    student_id = models.CharField(max_length=15, blank=True)
    student_name = models.CharField(max_length=50, blank=True)
    processed_image = models.ImageField(
        upload_to=upload_processed_marks_image_to,
        storage=overwrite_storage,
    )
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
        return mark_safe('<img src="{}" width= 400 px />'.format(self.processed_image.url))

    admin_photo.short_description = 'Processed Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return '%s Student %s %s' % (self.exam_title, self.student_id, self.student_name)


class Exams100(models.Model):
    class Meta:
        verbose_name_plural = 'Exams Record 100 Questions'

    title = models.CharField(max_length=20, unique=True)
    cover = models.ImageField(
        upload_to=upload_exam100_cover_to,
        storage=overwrite_storage,
        verbose_name="Answer Sheet"
    )
    template = models.FileField(
        upload_to=upload_exam100_template_to,
        blank=True,
        storage=overwrite_storage,
        default="template.json"
    )
    marker = models.ImageField(
        upload_to=upload_exam100_marker_to,
        blank=True,
        storage=overwrite_storage,
        default="omr_marker.jpg"
    )
    q1 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True, verbose_name="Answer key:Q1")
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
    q41 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q42 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q43 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q44 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q45 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q46 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q47 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q48 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q49 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q50 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q51 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q52 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q53 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q54 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q55 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q56 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q57 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q58 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q59 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q60 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q61 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q62 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q63 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q64 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q65 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q66 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q67 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q68 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q69 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q70 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q71 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q72 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q73 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q74 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q75 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q76 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q77 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q78 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q79 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q80 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q81 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q82 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q83 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q84 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q85 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q86 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q87 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q88 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q89 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q90 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q91 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q92 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q93 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q94 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q95 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q96 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q97 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q98 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q99 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)
    q100 = models.CharField(choices=CHOICES, max_length=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.template:
            fromDirectory = "media/examtemplate/100/save/"
            toDirectory = os.getcwd()
            copy_tree(fromDirectory, toDirectory)

            djangotemplate = File(open('template.json'))
            self.template = djangotemplate
            djangomarker = File(open('omr_marker.jpg', 'rb'))
            self.marker = djangomarker

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProcessedMarks100(models.Model):
    class Meta:
        verbose_name_plural = 'Processed Marks 100'

    exam_title = models.CharField(max_length=20)
    student_id = models.CharField(max_length=15, default='')
    student_name = models.CharField(max_length=50, default='')
    processed_image = models.ImageField(
        upload_to=upload_100processed_marks_image_to,
        storage=overwrite_storage,
    )
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
    q41 = models.CharField(max_length=4, null=True)
    q42 = models.CharField(max_length=4, null=True)
    q43 = models.CharField(max_length=4, null=True)
    q44 = models.CharField(max_length=4, null=True)
    q45 = models.CharField(max_length=4, null=True)
    q46 = models.CharField(max_length=4, null=True)
    q47 = models.CharField(max_length=4, null=True)
    q48 = models.CharField(max_length=4, null=True)
    q49 = models.CharField(max_length=4, null=True)
    q50 = models.CharField(max_length=4, null=True)
    q51 = models.CharField(max_length=4, null=True)
    q52 = models.CharField(max_length=4, null=True)
    q53 = models.CharField(max_length=4, null=True)
    q54 = models.CharField(max_length=4, null=True)
    q55 = models.CharField(max_length=4, null=True)
    q56 = models.CharField(max_length=4, null=True)
    q57 = models.CharField(max_length=4, null=True)
    q58 = models.CharField(max_length=4, null=True)
    q59 = models.CharField(max_length=4, null=True)
    q60 = models.CharField(max_length=4, null=True)
    q61 = models.CharField(max_length=4, null=True)
    q62 = models.CharField(max_length=4, null=True)
    q63 = models.CharField(max_length=4, null=True)
    q64 = models.CharField(max_length=4, null=True)
    q65 = models.CharField(max_length=4, null=True)
    q66 = models.CharField(max_length=4, null=True)
    q67 = models.CharField(max_length=4, null=True)
    q68 = models.CharField(max_length=4, null=True)
    q69 = models.CharField(max_length=4, null=True)
    q70 = models.CharField(max_length=4, null=True)
    q71 = models.CharField(max_length=4, null=True)
    q72 = models.CharField(max_length=4, null=True)
    q73 = models.CharField(max_length=4, null=True)
    q74 = models.CharField(max_length=4, null=True)
    q75 = models.CharField(max_length=4, null=True)
    q76 = models.CharField(max_length=4, null=True)
    q77 = models.CharField(max_length=4, null=True)
    q78 = models.CharField(max_length=4, null=True)
    q79 = models.CharField(max_length=4, null=True)
    q80 = models.CharField(max_length=4, null=True)
    q81 = models.CharField(max_length=4, null=True)
    q82 = models.CharField(max_length=4, null=True)
    q83 = models.CharField(max_length=4, null=True)
    q84 = models.CharField(max_length=4, null=True)
    q85 = models.CharField(max_length=4, null=True)
    q86 = models.CharField(max_length=4, null=True)
    q87 = models.CharField(max_length=4, null=True)
    q88 = models.CharField(max_length=4, null=True)
    q89 = models.CharField(max_length=4, null=True)
    q90 = models.CharField(max_length=4, null=True)
    q91 = models.CharField(max_length=4, null=True)
    q92 = models.CharField(max_length=4, null=True)
    q93 = models.CharField(max_length=4, null=True)
    q94 = models.CharField(max_length=4, null=True)
    q95 = models.CharField(max_length=4, null=True)
    q96 = models.CharField(max_length=4, null=True)
    q97 = models.CharField(max_length=4, null=True)
    q98 = models.CharField(max_length=4, null=True)
    q99 = models.CharField(max_length=4, null=True)
    q100 = models.CharField(max_length=4, null=True)

    def admin_photo(self):
        return mark_safe('<img src="{}" width= 400 px />'.format(self.processed_image.url))

    admin_photo.short_description = 'Processed Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return '%s Student %s %s' % (self.exam_title, self.student_id, self.student_name)
