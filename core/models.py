from django.db import models




class Modules(models.Model):
    module_name = models.CharField(max_length=50)
    module_duration = models.IntegerField()
    class_room = models.IntegerField()
    
    def __str__(self) -> str:
        return self.module_name
    
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    grade = models.IntegerField()
    modules = models.ManyToManyField(Modules, related_name="modules")
    
    def __str__(self) -> str:
        return self.name











class Instructor(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return self.email
    
class Course(models.Model):
    title = models.CharField(max_length=30)
    rating = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="courses")