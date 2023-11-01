from django.db import models
from uuid import uuid4


class Content(models.Model):
    class Meta:
        ordering = ("id",)

    id = models.UUIDField(primary_key=True, default=uuid4,  editable=False)
    name = models.CharField(max_length=150, null=False)
    content = models.TextField(null=False)
    video_url = models.URLField(max_length=200, null=True)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, null=False,  related_name="contents")
