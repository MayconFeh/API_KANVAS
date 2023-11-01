from django.db import models
from uuid import uuid4


class StudentCourseStatus(models.TextChoices):
    Pending = "pending"
    Accepted = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.CharField(choices=StudentCourseStatus.choices, default=StudentCourseStatus.Pending, max_length=11)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, related_name="students_courses")
    student = models.ForeignKey("accounts.Account", on_delete=models.CASCADE, related_name="students_courses")
