from django.db import models
from student.models.student_model import Student
class StudentDetails(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='details')
    address = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return f'Details for {self.student.student_name}'
