from django.conf.urls import patterns, include, url
from search import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foundation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name ='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^process/$', views.process, name='process'),
)
