from .views import index
from django.urls import path
urlpatterns=[
     path('<str:group_name>/',index,name="index")
]