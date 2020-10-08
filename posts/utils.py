from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from posts.models import Student, Exams, Exams100


def get_marks_from_dict(data):
    marks_field = {}
    for key in data.keys():
        if len(key) <= 3 and key[0] == 'q':
            marks_field[key] = data[key]
    return marks_field


def get_student(student_id):
    try:
        return Student.objects.get(student_id=student_id)
    except Student.DoesNotExist:
        raise ValidationError(_('Student not found.'))


def get_exam(exam_title: str):
    try:
        return Exams.objects.get(title=exam_title)
    except Exams.DoesNotExist:
        raise ValidationError(_('Exam not found.'))


def get_exam100(exam_title: str):
    try:
        return Exams100.objects.get(title=exam_title)
    except Exams100.DoesNotExist:
        raise ValidationError(_('Exam100 not found.'))


def save_processed_marks(instance, processed_marks: dict):
    for key in processed_marks.keys():
        setattr(instance, key, processed_marks.get(key))
    instance.save()
