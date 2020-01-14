from rest_framework.generics import RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Token
from .serializers import TokenSerializer



class TokenViewSet(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

    def list(self, request):
        queryset = Token.objects.all()
        serializer = TokenSerializer(queryset, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        queryset = Token.objects.all()
        token = get_object_or_404(queryset, pk=pk)
        serializer = TokenSerializer(token)
        return Response(serializer.data)

class SingleTokenView(RetrieveUpdateDestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
