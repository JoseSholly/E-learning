from rest_framework.permissions import BasePermission


class IsRolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.id).exists()