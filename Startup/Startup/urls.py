from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from demo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleTodo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.todolist, name='todo'), #index
    url(r'^addtodo/$', views.addtodo, name='add'),
    url(r'^todofinish/(?P<id>\d+)/$',  views.todofinish, name='finish'),
    url(r'^todorestore/(?P<id>\d+)/$', views.todorestore, name='restore'),
    url(r'^updatetodo/(?P<id>\d+)/$',  views.updatetodo, name='update'),
    url(r'^tododelete/(?P<id>\d+)/$',  views.tododelete, name='delete'),
)
