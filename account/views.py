from django.shortcuts import render
from rest_framework.viewsets import ViewSet 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserProfileSerializer

class UserProfileViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def update(self,request):
        serializer = UserProfileSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
