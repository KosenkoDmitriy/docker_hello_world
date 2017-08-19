from django.conf.urls import url,include
from rest_framework import routers
from . import views
#from .views import LocationSearchView
'''
router = routers.DefaultRouter()
router.register("location/search", LocationSearchView, base_name="location-search")
'''
urlpatterns = [
#	url(r"/api/v1/", include(router.urls)),
    url(r'^$', views.index, name='index'),
]
