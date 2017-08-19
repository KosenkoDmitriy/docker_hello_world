from django.conf.urls import url #, include
# from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
# router = DefaultRouter()
# router.register(r'API/users2', views.UserViewSet)

http_methods_for_list = {
    'get': 'list',
    'post': 'create'
}
user_list = views.UserViewSet.as_view(http_methods_for_list)

http_methods_for_detail = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}
user_detail = views.UserViewSet.as_view(http_methods_for_detail)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^', include(router.urls), name='users'), # default router

    url(r'^list/$', views.APIList.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.APIDetail.as_view(), name='detail'),

    url(r'^users/$', views.UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user_detail'),
    # url(r'^users/$', user_list, name='user_list'),
    # url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user_detail'),
    url(r'^accounts/$', views.AccountViewSet.as_view(http_methods_for_list), name='account_list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountViewSet.as_view(http_methods_for_detail), name='account_detail'),
    url(r'^account_users/$', views.AccountUserViewSet.as_view(http_methods_for_list), name='account_user_list'),
    url(r'^account_users/(?P<pk>[0-9]+)/$', views.AccountUserViewSet.as_view(http_methods_for_detail), name='account_user_detail'),

    url(r'^programs/$', views.ProgramViewSet.as_view(http_methods_for_list), name='program_list'),
    url(r'^programs/(?P<pk>[0-9]+)/$', views.ProgramViewSet.as_view(http_methods_for_detail), name='program_detail'),
    url(r'^projects/$', views.ProjectViewSet.as_view(http_methods_for_list), name='project_list'),
    url(r'^projects/(?P<pk>[0-9]+)/$', views.ProjectViewSet.as_view(http_methods_for_detail), name='project_detail'),

    url(r'^contracts/$', views.ContractViewSet.as_view(http_methods_for_list), name='contract_list'),
    url(r'^contracts/(?P<pk>[0-9]+)/$', views.ContractViewSet.as_view(http_methods_for_detail), name='contract_detail'),
    url(r'^conditions/$', views.ConditionViewSet.as_view(http_methods_for_list), name='condition_list'),
    url(r'^conditions/(?P<pk>[0-9]+)/$', views.ConditionViewSet.as_view(http_methods_for_detail), name='condition_detail'),

    url(r'^orders/$', views.OrderViewSet.as_view(http_methods_for_list), name='order_list'),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderViewSet.as_view(http_methods_for_detail), name='order_detail'),
    url(r'^order_types/$', views.OrderTypeViewSet.as_view(http_methods_for_list), name='order_type_list'),
    url(r'^order_types/(?P<pk>[0-9]+)/$', views.OrderTypeViewSet.as_view(http_methods_for_detail), name='order_type_detail'),

    url(r'^assets/$', views.AssetViewSet.as_view(http_methods_for_list), name='asset_list'),
    url(r'^assets/(?P<pk>[0-9]+)/$', views.AssetViewSet.as_view(http_methods_for_detail), name='asset_detail'),
    url(r'^vehicles/$', views.VehicleViewSet.as_view(http_methods_for_list), name='vehicle_list'),
    url(r'^vehicles/(?P<pk>[0-9]+)/$', views.VehicleViewSet.as_view(http_methods_for_detail), name='vehicle_detail'),
    url(r'^inventories/$', views.InventoryViewSet.as_view(http_methods_for_list), name='inventory_list'),
    url(r'^inventories/(?P<pk>[0-9]+)/$', views.InventoryViewSet.as_view(http_methods_for_detail), name='inventory_detail'),

    url(r'^places/$', views.PlaceViewSet.as_view(http_methods_for_list), name='place_list'),
    url(r'^places/(?P<pk>[0-9]+)/$', views.PlaceViewSet.as_view(http_methods_for_detail), name='place_detail'),

    url(r'^drivers/$', views.DriverViewSet.as_view(http_methods_for_list), name='driver_list'),
    url(r'^drivers/(?P<pk>[0-9]+)/$', views.DriverViewSet.as_view(http_methods_for_detail), name='driver_detail'),

    url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/twitter/$', views.TwitterLogin.as_view(), name='twitter_login')
]
