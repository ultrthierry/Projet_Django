from django.conf.urls import url  # import tous les urls du project

from . import views

urlpatterns = [

    url(r'^$', views.listing, name ="listing"),  # "/store will call the method "index" in "views.py"
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name ="detail"),
    url(r'search/$', views.search, name='search'),


    #url(r'^$', views.listing), #"/store will call the method "index" in "views.py"

]