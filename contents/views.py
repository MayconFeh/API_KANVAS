from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Content
from courses.models import Course
from .permissions import IsSuperUserOrReadOnly, IsContentOwnerOrSuperuser
from .serializers import ContentSerializer
from rest_framework.exceptions import NotFound


class CreateContentView(generics.CreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    permission_classes = [IsAuthenticated, IsSuperUserOrReadOnly]

    def perform_create(self, serializer):
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id)
        serializer.save(course=course)


class RetrieveUpdateDestroyContentView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsAuthenticated, IsContentOwnerOrSuperuser]
    # lookup_url_kwarg = 'content_id'

    def put(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get_object(self):
        try:
            Course.objects.get(pk=self.kwargs.get('course_id'))
            content = Content.objects.get(pk=self.kwargs.get('content_id'))

        except (Course.DoesNotExist):
            raise NotFound({"detail": "course not found."})
        except (Content.DoesNotExist):
            raise NotFound({"detail": "content not found."})

        self.check_object_permissions(self.request, content)

        return content
