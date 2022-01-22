from django.conf.urls import url
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from posts.views import PostsViewSet,PostsRatesViewSet


router = DefaultRouter()
router.register("posts",PostsViewSet,basename="posts")
router.register("posts-rates",PostsViewSet, basename="posts-rates")

urlpatterns = [
    url('',include(router.urls))
]
