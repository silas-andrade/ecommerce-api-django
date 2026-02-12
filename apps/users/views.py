from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema


@extend_schema(request=None, responses=None)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get("refresh"))
        token.blacklist()
        return Response(status=204)
