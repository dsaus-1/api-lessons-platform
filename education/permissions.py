from rest_framework.permissions import BasePermission

class ModeratorPerms(BasePermission):

    def has_permission(self, request, view):
        if request.method in ['POST', 'DELETE']:
            return False
        return request.user.has_perms(['education.view_lesson', 'education.change_lesson', 'education.change_course', 'education.view_course'])

class SuperPerms(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser


class OwnerCoursePerm(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.owner_course:
            return True
        return False


class OwnerLessonPerm(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.pk == obj.owner_lesson:
            return True
        return False