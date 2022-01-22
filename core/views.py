from django.shortcuts import render
from rest_framework import generics
from core.serializers import InstructorSerializer,CourseSerializer
from core.models import Instructor,Course


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()
