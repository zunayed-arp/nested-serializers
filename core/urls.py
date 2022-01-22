from django.urls import path,include
from core.views import InstructorListView


urlpatterns = [
    path('instructors/',InstructorListView.as_view())
]
