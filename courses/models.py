from django.db import models
from uuid import uuid4


class StatusCourse(models.TextChoices):
    NotStart = "not started"
    InProgress = "in progress"
    Finish = "finished"


class Course(models.Model):
    class Meta:
        ordering = ("id",)

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(choices=StatusCourse.choices, max_length=11, default=StatusCourse.NotStart)
    start_date = models.DateField()
    end_date = models.DateField()
    instructor = models.ForeignKey("accounts.Account", null=True, on_delete=models.PROTECT, related_name="courses")
    students = models.ManyToManyField("accounts.Account", through="students_courses.StudentCourse", related_name="my_courses")
