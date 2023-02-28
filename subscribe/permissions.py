from rest_framework.permissions import BasePermission


class OwnerSubscribePerm(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return str(request.user.email) == str(obj.student)

        return False