from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.utils.translation import gettext_lazy as _

from .models import (
    Exams,
    Student,
    ProcessedMarks,
    Exams100,
    ProcessedMarks100
)
from .utils import get_marks_from_dict


class MarksForm:
    def get_marks(self, instance):
        all_fields = model_to_dict(instance)
        return get_marks_from_dict(data=all_fields)

    def count_final_marks(self, processed_marks, exam_marks):
        marks = 0
        for key in exam_marks.keys():
            if exam_marks[key] == processed_marks[key]:
                marks += 1
        return marks

    def retotal(self, instance, exam):
        processed_marks = self.get_marks(instance=instance)
        exam_marks = self.get_marks(instance=exam)
        final_marks = self.count_final_marks(
            processed_marks=processed_marks,
            exam_marks=exam_marks,
        )
        if instance.final_marks != final_marks:
            instance.final_marks = final_marks
            instance.save()


class ProcessedMarksForm(forms.ModelForm, MarksForm):
    class Meta:
        model = ProcessedMarks
        fields = (
            'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11',
            'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21',
            'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31',
            'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40'
        )

    def save(self, commit=True):
        instance = super().save(commit=commit)
        try:
            exam = Exams.objects.get(title=instance.exam_title)
        except Exams.DoesNotExist:
            raise ValidationError(_('Exam Not Found.'))
        self.retotal(instance=instance, exam=exam)
        return instance


@admin.register(ProcessedMarks)
class ProcessedMarksAdmin(admin.ModelAdmin):
    form = ProcessedMarksForm
    change_form_template = 'admin/custom_change_form.html'

    fields = (
        'exam_title', 'student_id', 'student_name', 'admin_photo', 'final_marks', 'q1',
        'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
        'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26',
        'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38',
        'q39', 'q40'
    )
    list_display = [
        'exam_title',
        'student_name',
        'student_id',
        'final_marks',

    ]

    readonly_fields = (
        'student_id',
        'admin_photo',
        'exam_title',
        'student_name',
        'final_marks'
    )


class ProcessedMarks100Form(forms.ModelForm, MarksForm):
    class Meta:
        model = ProcessedMarks100
        fields = (
            'q1',
            'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
            'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26',
            'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38',
            'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50',
            'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q61', 'q62',
            'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 'q71', 'q72', 'q73', 'q74',
            'q75', 'q76', 'q77', 'q78', 'q79', 'q80', 'q81', 'q82', 'q83', 'q84', 'q85', 'q86',
            'q87', 'q88', 'q89', 'q90', 'q91', 'q92', 'q93', 'q94', 'q95', 'q96', 'q97', 'q98',
            'q99', 'q100'
        )

    def save(self, commit=True):
        instance = super().save(commit=commit)
        try:
            exam = Exams100.objects.get(title=instance.exam_title)
        except Exams100.DoesNotExist:
            raise ValidationError(_('Exam Not Found.'))
        self.retotal(instance=instance, exam=exam)

        return instance


@admin.register(ProcessedMarks100)
class ProcessedMarks100Admin(admin.ModelAdmin):
    form = ProcessedMarks100Form
    change_form_template = 'admin/custom_change_form.html'

    fields = (
        'exam_title', 'student_id', 'student_name', 'admin_photo', 'final_marks', 'q1',
        'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14',
        'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26',
        'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38',
        'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50',
        'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q61', 'q62',
        'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 'q71', 'q72', 'q73', 'q74',
        'q75', 'q76', 'q77', 'q78', 'q79', 'q80', 'q81', 'q82', 'q83', 'q84', 'q85', 'q86',
        'q87', 'q88', 'q89', 'q90', 'q91', 'q92', 'q93', 'q94', 'q95', 'q96', 'q97', 'q98',
        'q99', 'q100'
    )

    list_display = [
        'exam_title',
        'student_name',
        'student_id',
        'final_marks',

    ]

    readonly_fields = ('student_id', 'admin_photo', 'exam_title', 'student_name')


admin.site.register(Exams)
admin.site.register(Student)
admin.site.register(Exams100)
