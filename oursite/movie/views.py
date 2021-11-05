from django.shortcuts import render
from rest_framework import generics
from rest_framework.utils import serializer_helpers
from .models import Movies
from .serializers import Sort

# Create your views here.
class ViewPage(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = Sort

class Action(generics.ListCreateAPIView):
    queryset = Movies.objects.filter(category= 'action')
    serializer_class = Sort

class Comedy(generics.ListCreateAPIView):
    queryset = Movies.objects.filter(category = 'comedy')
    serializer_class = Sort

class Horror(generics.ListCreateAPIView):
    queryset = Movies.objects.filter(category = 'horror')
    serializer_class= Sort

class Fantasy(generics.ListCreateAPIView):
    queryset = Movies.objects.filter(category = 'fantasy')
    serializer_class= Sort

class Romance(generics.ListCreateAPIView):
    queryset = Movies.objects.filter(category = 'romance')
    serializer_class= Sort

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = Sort
