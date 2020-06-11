from django.contrib import admin
from .models import Exams, Student, ProcessedMarks


class ProcessedMarksAdmin(admin.ModelAdmin):
    fields = ('exam_title', 'student_id', 'student_name', 'admin_photo', 'final_marks', 'q1', 'q2', 'q3',
              'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19',
              'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34',
              'q35', 'q36', 'q37', 'q38', 'q39', 'q40')
    list_display = [
        'exam_title',
        'student_name',
        'student_id'



    ]

    readonly_fields = ('student_id', 'admin_photo', 'exam_title', 'student_name')


admin.site.register(Exams)
admin.site.register(Student)
admin.site.register(ProcessedMarks, ProcessedMarksAdmin)
