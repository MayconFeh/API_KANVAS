from django.urls import path
from courses.views import ListCreateCourseView, RetrieveUpdateDestroyCourseView
from contents.views import CreateContentView, RetrieveUpdateDestroyContentView
from students_courses.views import StudentCourseView


urlpatterns = [
    path("courses/", ListCreateCourseView.as_view()),
    path("courses/<uuid:course_id>/", RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<uuid:course_id>/contents/", CreateContentView.as_view()),
    path("courses/<uuid:course_id>/contents/<uuid:content_id>/", RetrieveUpdateDestroyContentView.as_view()),
    path("courses/<uuid:course_id>/students/", StudentCourseView.as_view()),
]
