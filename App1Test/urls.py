from django.urls import path
from App1Test.views import home
urlpatterns = [
    path('', home, name="home"),
]