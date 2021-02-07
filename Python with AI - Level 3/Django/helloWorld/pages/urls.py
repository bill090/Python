from django.urls import path
from .views import homePageView, simplePageView

urlpatterns = [
    path('', homePageView, name = 'home'),
    path('simple/', simplePageView, name = 'simple'),
]