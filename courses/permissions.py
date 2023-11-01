from rest_framework.permissions import BasePermission

from accounts import permissions


class IsStudantsOrSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or request.user in obj.course.students.all()
