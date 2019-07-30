from joc import views
from django.conf.urls import url

urlpatterns=[
    url("menu",views.menu),
    url("week1quiz",views.week1quiz)

]
