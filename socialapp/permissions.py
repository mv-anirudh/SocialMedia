from rest_framework import permissions

# custom permissions

# class based permission => has_permission
# object based permisiion => has_object_permission

class IsOwnerOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj.owner
    

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:

            return True
        
        else:

            return request.user == obj.owner


