from rest_framework.serializers import ValidationError
from rest_framework.generics import RetrieveUpdateAPIView
from accounts.models import Account
from courses.models import Course
from courses.permissions import IsStudantsOrSuperuser
from courses.serializers import CourseStudentSerializer
from students_courses.models import StudentCourse
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated


class StudentCourseView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, IsStudantsOrSuperuser]
    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
    lookup_url_kwarg = "course_id"

    def perform_update(self, serializer):
        emails = []
        students_courses = serializer.validated_data.pop("students_courses")
        email = students_courses[0]["student"]["email"]
        try:
            course = Course.objects.get(pk=self.kwargs["course_id"])
            student = Account.objects.get(email=email)
            StudentCourse.objects.create(course=course, student=student)
            course.students.add(student)
        except Account.DoesNotExist:
            emails.append(email)
        if len(emails) > 0:
            emails = ",".join(emails)
            raise ValidationError({"detail": f"No active accounts was found: {emails}."})

    @extend_schema(
        description="Rota para listagem dos estudantes do curso",
        tags=["Listagem e matrícula de estudante"],
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        description="Rota para adição de alunos ao curso",
        tags=["Listagem e matrícula de estudante"],
        parameters=[
            CourseStudentSerializer,
        ],
    )
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
