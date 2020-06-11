from django import forms
from .models import Exams, Student, ProcessedMarks, CHOICES
from django.utils.safestring import mark_safe


class ExamsForm(forms.ModelForm):
    q1 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q2 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q3 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q4 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q5 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q6 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q7 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q8 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q9 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q10 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q11 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q12 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q13 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q14 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q15 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q16 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q17 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q18 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q19 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q20 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q21 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q22 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q23 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q24 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q25 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q26 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q27 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q28 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q29 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q30 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q31 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q32 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q33 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q34 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q35 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q36 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q37 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q38 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q39 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q40 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Exams
        fields = [
            'title',
            'cover',
            'template',
            'marker',
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
            'q8',
            'q9',
            'q10',
            'q11',
            'q12',
            'q13',
            'q14',
            'q15',
            'q16',
            'q17',
            'q18',
            'q19',
            'q20',
            'q21',
            'q22',
            'q23',
            'q24',
            'q25',
            'q26',
            'q27',
            'q28',
            'q29',
            'q30',
            'q31',
            'q32',
            'q33',
            'q34',
            'q35',
            'q36',
            'q37',
            'q38',
            'q39',
            'q40'

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
            'processed_image',
            'student_id',
            'student_name',
            'final_marks',
            'exam_title',
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
            'q8',
            'q9',
            'q10',
            'q11',
            'q12',
            'q13',
            'q14',
            'q15',
            'q16',
            'q17',
            'q18',
            'q19',
            'q20',
            'q21',
            'q22',
            'q23',
            'q24',
            'q25',
            'q26',
            'q27',
            'q28',
            'q29',
            'q30',
            'q31',
            'q32',
            'q33',
            'q34',
            'q35',
            'q36',
            'q37',
            'q38',
            'q39',
            'q40'

        ]
