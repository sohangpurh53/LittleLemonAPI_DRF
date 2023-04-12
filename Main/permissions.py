from rest_framework.permissions import BasePermission

class IsAllowedEditOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name = 'manager'):
            return True
        
        return request.user.is_authenticated and request.method == 'GET'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager'):
            return True
        return request.user.is_authenticated and (request.user.groups.filter(
            name='customer') or request.user.groups.filter(
            name='deliverycrew')) and request.method == 'GET'
