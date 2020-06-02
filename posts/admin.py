from django.contrib import admin
from .models import Exams, Student, ProcessedMarks

admin.site.register(Exams)
admin.site.register(Student)
admin.site.register(ProcessedMarks)
