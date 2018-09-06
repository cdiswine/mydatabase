
from django.conf.urls import url
from django.contrib import admin
from viruses import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    #url(r'^dashboard/(\d+)/', views.dashboard, name='dashboard'),
    url(r'^burtin/', views.burtin, name='burtin'),
    
]
