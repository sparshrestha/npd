from django import forms
from .models import Exams, Student, ProcessedMarks, CHOICES, Exams100, ProcessedMarks100
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


class ProcessedMarksForm(forms.ModelForm):
    class Meta:
        model = ProcessedMarks
        fields = [
            'processed_image',
            'student',
            'final_marks',
            'exam',
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


class Exams100Form(forms.ModelForm):
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
    q41 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q42 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q43 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q44 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q45 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q46 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q47 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q48 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q49 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q50 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q51 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q52 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q53 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q54 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q55 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q56 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q57 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q58 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q59 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q60 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q61 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q62 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q63 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q64 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q65 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q66 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q67 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q68 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q69 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q70 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q71 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q72 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q73 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q74 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q75 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q76 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q77 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q78 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q79 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q80 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q81 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q82 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q83 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q84 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q85 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q86 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q87 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q88 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q89 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q90 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q91 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q92 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q93 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q94 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q95 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q96 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q97 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q98 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q99 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    q100 = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Exams100
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
            'q40',
            'q41',
            'q42',
            'q43',
            'q44',
            'q45',
            'q46',
            'q47',
            'q48',
            'q49',
            'q50',
            'q51',
            'q52',
            'q53',
            'q54',
            'q55',
            'q56',
            'q57',
            'q58',
            'q59',
            'q60',
            'q61',
            'q62',
            'q63',
            'q64',
            'q65',
            'q66',
            'q67',
            'q68',
            'q69',
            'q70',
            'q71',
            'q72',
            'q73',
            'q74',
            'q75',
            'q76',
            'q77',
            'q78',
            'q79',
            'q80',
            'q81',
            'q82',
            'q83',
            'q84',
            'q85',
            'q86',
            'q87',
            'q88',
            'q89',
            'q90',
            'q91',
            'q92',
            'q93',
            'q94',
            'q95',
            'q96',
            'q97',
            'q98',
            'q99',
            'q100'


        ]


class ProcessedMarks100Form(forms.ModelForm):
    class Meta:
        model = ProcessedMarks100
        fields = [
            'processed_image',
            'student',
            'final_marks',
            'exam',
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
            'q40',
            'q41',
            'q42',
            'q43',
            'q44',
            'q45',
            'q46',
            'q47',
            'q48',
            'q49',
            'q50',
            'q51',
            'q52',
            'q53',
            'q54',
            'q55',
            'q56',
            'q57',
            'q58',
            'q59',
            'q60',
            'q61',
            'q62',
            'q63',
            'q64',
            'q65',
            'q66',
            'q67',
            'q68',
            'q69',
            'q70',
            'q71',
            'q72',
            'q73',
            'q74',
            'q75',
            'q76',
            'q77',
            'q78',
            'q79',
            'q80',
            'q81',
            'q82',
            'q83',
            'q84',
            'q85',
            'q86',
            'q87',
            'q88',
            'q89',
            'q90',
            'q91',
            'q92',
            'q93',
            'q94',
            'q95',
            'q96',
            'q97',
            'q98',
            'q99',
            'q100'
        ]
