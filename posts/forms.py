from django import forms
from .models import Post, Student


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
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
