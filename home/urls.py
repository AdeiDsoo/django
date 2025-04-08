from django.urls import path
from home.views import homeView, create_auto
urlpatterns=[
    path('', homeView, name='homeView' ),
    path('create_auto', create_auto, name='create_auto'),
]