from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/message', views.MessageViews)


urlpatterns = [
    path('', include(router.urls)),
    path('message/', views.message_views, name='message_views'),
    path('message/<username>/', views.message_views_specific_user, name='message_views_specific_user'),
    path('readMessage/', views.read_message, name='read_message'),
    path('deleteMessage/', views.delete_message, name='delete_message'),
    path('loggedMessage/', views.logged_message, name='logged_message'),
]
