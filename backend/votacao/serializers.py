from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class VotacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Votacao
        