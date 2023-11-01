from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsCourseInstructorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.instructor


class IsCourseStudentPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS and request.user in obj.course.students.all()
