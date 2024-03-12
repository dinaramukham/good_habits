from rest_framework.permissions import BasePermission


class IsOwnerPermissionsClass(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsPublicHabit(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.it_public == True:
            return True
        return False
