"""Runur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

import os.path
from django.conf import settings
from dddp.views import MeteorView

from django.conf.urls import include,url
#from django.contrib import admin
from django.contrib.gis import admin

from organizations.backends import invitation_backend,registration_backend
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from dashing.utils import router
from rest_framework_jwt.views import obtain_jwt_token
from API import views

from rest_framework_raml.renderers import RAMLRenderer, RAMLDocsRenderer
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from django.views.generic import RedirectView
from django.conf.urls.static import static

schema_view = get_schema_view(
    title='Runur API',
)

schema_view_raml = get_schema_view(
    title='Runur API',
    renderer_classes=[RAMLRenderer, RAMLDocsRenderer]
)

schema_view_swagger = get_schema_view(
    # title='Runur API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)

admin.autodiscover()

#import xadmin
#xadmin.autodiscover()

#from xadmin.plugins import xversion
#xversion.register_models()

#rest_router = routers.DefaultRouter()
#rest_router.register(r'users', views.UserViewSet)
#rest_router.register(r'groups', views.GroupViewSet)
#rest_router.register(r'permissions', views.PermissionViewSet)


urlpatterns = [
    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')), # Fake Admin Portal
    url(r'^secret/',include(admin.site.urls)), # Real Admin Portal
    #url(r'^', include(rest_router.urls)), #TODO Remove ASAP Exposes ViewSet API EndPoints on Root Site
    url(r'^rest-auth/', include('rest_auth.urls')), # Rest Auth
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')), # Rest AUth URLS
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token), # JSON Tokens
    url(r'^dashboard/', include(router.urls)), # Dashboard
    #url(r'^docs/', include('rest_framework_docs.urls')), # REST Docs
    #url(r'^docs/', include('sphinxdoc.urls')),

    # organization urls
    url(r'^accounts/', include('organizations.urls')),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^invite/', include(invitation_backend().get_urls())),
    url(r'^register/', include(registration_backend().get_urls())),
    url(r'^invitations/', include(invitation_backend().get_urls())),
    # end organization urls

    #url(r'^messages/', include('django_messages.urls')),
    url(r'^treenav/', include('treenav.urls')),
    #url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^API/', include('API.urls')),
    url(r'^EventEngine/', include('EventEngine.urls')),
    url(r'^JON/', include('JON.urls')),
    url(r'^Search/', include('Search.urls')),
    url(r'^TaskQue/', include('TaskQue.urls')),

    url(r'^schema/$', schema_view), # schema for rest api
    url(r'^raml/$', schema_view_raml),
    url(r'^ddocs/', include_docs_urls(title='Runur API')),
    url(r'^drfdocs/', include('rest_framework_docs.urls')),
    url(r'^docs/', schema_view_swagger), # it works with ModelViewSets

    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

