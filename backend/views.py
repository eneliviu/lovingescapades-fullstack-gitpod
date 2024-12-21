from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


@api_view()
def root_route(request):
    permission_classes = (IsAuthenticated,)
    return Response({
        'message': 'Welcome to my drf api!'
    })
