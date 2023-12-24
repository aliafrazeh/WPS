from django.urls import path
from .views import home,DetailWeb,CreateWeb
app_name = "home"
urlpatterns = [
    path('',home,name="home"),
    path('create/',CreateWeb.as_view(),name="create"),
    path('<slug>/',DetailWeb.as_view(),name="detail"),
]