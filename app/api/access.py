from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class AccessViewSet(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user_groups = list(request.user.groups.all())
        user_groups_names = [group.name for group in user_groups]
        return Response(user_groups_names)
