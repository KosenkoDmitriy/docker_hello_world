from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, Permission, Group
from rest_framework import permissions, viewsets, status, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.views import LoginView
from rest_auth.social_serializers import TwitterLoginSerializer
from API.models import API
from API.permissions import IsOwnerOrReadOnly
from API.serializers import APISerializer, UserSerializer, PermissionSerializer, GroupSerializer, AccountSerializer, AccountUserSerializer
from API.serializers import ProgramSerializer, ProjectSerializer, OrderSerializer, \
    OrderTypeSerializer, ContractSerializer, ConditionSerializer
from JON.models import Program, Project, Order, OrderType, Contract, Condition, Account, AccountUser
from JON.models import Asset, Vehicle, Inventory, Place, Driver
from API.serializers import AssetSerializer, VehicleSerializer, InventorySerializer, PlaceSerializer, DriverSerializer
# import django_filters.rest_framework
from django_filters import rest_framework as filters


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(LoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


def index(request):
    return HttpResponse("Hi there :) You're at the Runur API index.")


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts (orgs) to be viewed or edited.

    retrieve:
    Return the given account (org).

    list:
    Return a list of all the existing accounts (orgs).

    create:
    Create a new account (org) instance.

    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_fields = ('name', 'slug', 'is_active')


class AccountUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows members (account user) to be viewed or edited.

    retrieve:
    Return the given member (account user).

    list:
    Return a list of all the existing members (account users).

    create:
    Create a new member (account user) instance.

    """
    queryset = AccountUser.objects.all()
    serializer_class = AccountUserSerializer
    filter_fields = ('is_admin', 'user__username', 'user__email', 'organization__name', 'organization__slug')


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assets to be viewed or edited.

    retrieve:
    Return the given asset.

    list:
    Return a list of all the existing assets.

    create:
    Create a new asset.

    """
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    filter_fields = ('name', 'text', 'user__user__username', 'user__user__email', 'user__user__is_active', 'org__name', 'org__slug', 'type',  'tags__name', 'tags__slug')


class InventoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows inventories to be viewed or edited.

    retrieve:
    Return the given inventory.

    list:
    Return a list of all the existing inventories.

    create:
    Create a new inventory.

    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_fields = ('name', 'text', 'asset__name', 'asset__text', 'tags__name', 'tags__slug')


class VehicleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vehicles to be viewed or edited.

    retrieve:
    Return the given vehicle.

    list:
    Return a list of all the existing vehicles.

    create:
    Create a new vehicle.

    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_fields = ('name', 'text', 'type', 'model_name', 'manufacturer_year', 'manufacturer_vehicle', 'cargo_capacity', 'load_weight', 'load_description', 'asset__name', 'asset__text',  'tags__name', 'tags__slug')


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.

    retrieve:
    Return the given order.

    list:
    Return a list of all the existing orders.

    create:
    Create a new order instance.

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_fields = ('text', 'type', 'status', 'contract', 'tags__name', 'tags__slug')


class OrderTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order types to be viewed or edited.

    retrieve:
    Return the given order type.

    list:
    Return a list of all the existing order types.

    create:
    Create a new order type instance.

    """
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer
    filter_fields = ('name', 'duration', 'delivery_datetime', 'price', 'tags__name', 'tags__slug')


class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.

    retrieve:
    Return the given contract.

    list:
    Return a list of all the existing contracts.

    create:
    Create a new contract instance.

    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_fields = ('name', 'text', 'conditions', 'tags__name', 'tags__slug')


class ConditionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows conditions to be viewed or edited.

    retrieve:
    Return the given condition.

    list:
    Return a list of all the existing conditions.

    create:
    Create a new condition instance.

    """
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    filter_fields = ('name', 'value', 'measure', 'tags__name', 'tags__slug')


class ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows programs to be viewed or edited.

    retrieve:
    Return the given program.

    list:
    Return a list of all the existing programs.

    create:
    Create a new program instance.

    """
    queryset = Program.objects.all().order_by('name')
    serializer_class = ProgramSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'text', 'tags__name', 'tags__slug')

    # filter_backends = (filters.SearchFilter,)
    # filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    # search_fields = ('name', 'text', 'tags')


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.

    retrieve:
    Return the given project.

    list:
    Return a list of all the existing projects.

    create:
    Create a new project instance.

    """
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    filter_fields = ('name', 'text', 'is_active', 'orders', 'tags__name', 'tags__slug')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.

    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.

    retrieve:
    Return the given place.

    list:
    Return a list of all the existing places.

    create:
    Create a new place instance.

    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class DriverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows drivers to be viewed or edited.

    retrieve:
    Return the given driver.

    list:
    Return a list of all the existing drivers.

    create:
    Create a new driver instance.

    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class UserList(generics.ListAPIView):
    """
    get:
    Return a list of all the existing users.

    post:
    Create a new user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    get:
    Return the given user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permissions to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class APIList(generics.ListCreateAPIView):
    """
    List all API Description Schemes, or create a new API Description Scheme.

    """
    queryset = API.objects.all()
    serializer_class = APISerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class APIDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete an API Description Scheme instance.
    """
    queryset = API.objects.all()
    serializer_class = APISerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
