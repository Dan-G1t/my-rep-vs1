from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pass, CustomUser, Coordinates, Level, Image
from .serializers import CustomUserSerializer, CoordinatesSerializer, LevelSerializer, PassSerializer
from django.core.exceptions import ValidationError


@api_view(['POST'])
def submit_data(request):
    serializer = PassSerializer(data=request.data)

    if serializer.is_valid():
        try:
            pass_instance = serializer.save()
            return Response({"status": 200, "message": None, "id": pass_instance.id}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": 500, "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response({"status": 400, "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)