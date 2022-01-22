
from django.contrib import admin
from core.models import Modules,Student,Instructor,Course


@admin.register(Modules)
class ModulesAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class ModulesAdmin(admin.ModelAdmin):
    pass
    