from django.conf.urls import url
from . import views

app_name = 'movie'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_database/$', views.create_database, name='create_database'),
    url(r'^country/$', views.country, name='country'),
    url(r'^add_country/$', views.add_country, name='add_country'),
    url(r'^update_country/$', views.update_country, name='update_country'),
    url(r'^delete_country/$', views.delete_country, name='delete_country'),
    url(r'^director/$', views.director, name='director'),
    url(r'^add_director/$', views.add_director, name='add_director'),
    url(r'^delete_director/$', views.delete_director, name='delete_director'),
    url(r'^movie/$', views.movie, name='movie'),
    url(r'^add_movie/$', views.add_movie, name='add_movie'),
    url(r'^delete_movie/$', views.delete_movie, name='delete_movie'),
]
