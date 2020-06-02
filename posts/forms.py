from django import forms
from .models import Exams, Student, ProcessedMarks


class ExamsForm(forms.ModelForm):
    class Meta:
        model = Exams
        fields = [
            'title',
            'cover',
            'template',
            'marker'
        ]


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'student_name',
            'student_email'
        ]


class ProcessedMarks(forms.ModelForm):
    class Meta:
        model = ProcessedMarks
        fields = [
            'student_id',
            'raw_marks',
            'exam_title'


        ]
