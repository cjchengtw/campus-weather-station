from django.conf.urls import url
from pages.views import HomeView,StatusView,AboutView,ChartData
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^status$', views.StatusView.as_view(), name='status'),
    url(r'^about$', views.AboutView.as_view(), name='about'),
    url(r'^api/chart/data/$', ChartData.as_view()),
]