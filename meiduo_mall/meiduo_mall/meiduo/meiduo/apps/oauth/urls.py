from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^qq/authorization/$', views.OAuthQQUrlView.as_view()),
    url(r'^qq/user/$', views.OAuthQQUserView.as_view()),
]