from django.urls import path

from . import views

app_name = 'insta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('submit/', views.SubmitView.as_view(), name='submit'),
    path('result/<int:pk>', views.ResultView.as_view(), name='result'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]
