from django.contrib import admin
from student.models.student_model import Student
from student.models.student_details_model import StudentDetails

admin.site.register(Student)
admin.site.register(StudentDetails)
# admin.site.register(Subject_wise_marks)