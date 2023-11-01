from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.permissions import IsStudantsOrSuperuser
from .models import Course
from rest_framework.permissions import IsAuthenticated
from .serializers import CourseSerializer


class ListCreateCourseView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsStudantsOrSuperuser]

    def get_queryset(self):
        if not self.request.user.is_superuser:
            queryset = Course.objects.filter(students=self.request.user)
            return queryset
        else:
            queryset = Course.objects.all()
            return queryset


class RetrieveUpdateDestroyCourseView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_url_kwarg = "course_id"
    permission_classes = [IsAuthenticated, IsStudantsOrSuperuser]
