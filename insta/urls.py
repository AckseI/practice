from django.urls import path

from . import views
#from insta.views import home_page

app_name = 'insta'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('submit/', views.submit, name='submit'),
    path('result/<int:pk>', views.ResultView.as_view(), name='result'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
]
