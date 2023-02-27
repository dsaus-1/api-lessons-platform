from rest_framework.permissions import BasePermission


class OwnerSubscribePerm(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.email == obj.student:
                return True
        return False