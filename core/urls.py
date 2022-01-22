from django.urls import path,include
from django.conf.urls import url
from core.views import InstructorListView,CourseListView,ModulesViewSet,StudentViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("student",StudentViewSet,basename='student')
router.register("module",ModulesViewSet,basename='module')


urlpatterns = [
    path('instructors/',InstructorListView.as_view()),
    path('courses/',CourseListView.as_view()),
    url('',include(router.urls))
]
