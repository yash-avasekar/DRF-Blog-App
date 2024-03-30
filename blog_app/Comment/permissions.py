from rest_framework import permissions


class IsOwnerOfCommentOrOwnerOfPostOrReadOnly(permissions.BasePermission):
    """
    Comment Owner edit
    Post Owner can delete
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are allowed to the owner of the comment or the owner of the post.
        return (
            obj.profile == request.user.profile
            or obj.post.profile == request.user.profile
        )
