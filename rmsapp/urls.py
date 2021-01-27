from django.urls import path
from rmsapp import views

urlpatterns = [
    path('',views.showIndex,name='main')

]