from dataclasses import fields
import imp
from pyexpat import model
from statistics import mode
from core.models import Course,Instructor
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'
        

class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True,read_only=True)
    class Meta:
        model = Instructor
        fields = '__all__'
    