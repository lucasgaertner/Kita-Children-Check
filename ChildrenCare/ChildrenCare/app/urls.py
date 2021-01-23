from django.conf.urls import url
from django.urls import path, include
from app import views
from .views import SignUpView

urlpatterns = [
    url(r'^$', views.DataPageView.as_view(), name='overview'), 
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^data/$', views.UploadDataPageView.as_view(), name='data'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]