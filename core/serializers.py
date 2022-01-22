
from core.models import Course,Instructor,Modules,Student
from rest_framework import serializers



class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ['id','modules_name','module_duration','class_room']
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields= ['id','name','age','grade','modules']
        depth= 1















class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Course
        fields = '__all__'
        

class InstructorSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True,read_only=True)
    class Meta:
        model = Instructor
        fields = '__all__'
    