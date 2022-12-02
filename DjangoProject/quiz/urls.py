from  django.urls import path
#configure the url for quiz url module in DjangoProject/urls.py

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.start, name='start'),
    path('results/', views.results, name='results'),
    path('statistics/', views.statistics, name='statistics'),
]