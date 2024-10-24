from django.urls import path
from . import views

urlpatterns =[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("<int:id>",views.index, name="index"),
    path("classification/heartdisease/",views.heartdisease,name="heartdisease"),
    path("tests/",views.tests,name="tests"),
    path("cv/",views.cv,name="cv")
    #path("plots/",views.plots,name="plots")

]
