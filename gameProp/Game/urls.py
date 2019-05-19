from django.conf.urls import url

from .views import Game

urlpatterns = [
    url(r'game/', Game.as_view(), name='game'),
]