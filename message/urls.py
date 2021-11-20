from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('message', views.MessageViews)


urlpatterns = [
    path('', include(router.urls))
]
