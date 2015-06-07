from django.conf.urls import patterns, url
from essential_nutritions import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home/$', views.home_view, name='home'),
    # url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
)