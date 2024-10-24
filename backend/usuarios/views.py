from rest_framework import viewsets, status
from rest_framework.views import APIView 
from rest_framework.response import Response 
from django.contrib.auth.models import User
from usuarios.serializer import UserSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        username =  request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username = username,password= password)
        if user is not None:
            return Response({'message':"Usuario logado"}, status=status.HTTP_200_OK)
        else:
            return Response({'message':"Usuario não encontrado"}, status=status.HTTP_401_UNAUTHORIZED)
            