from django.contrib.auth.models import User, Permission, Group
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from taggit.models import Tag
from API.models import API, LANGUAGE_CHOICES, STYLE_CHOICES
from JON.models import Program, Project, Order, OrderType, Contract, Condition, Account, AccountUser
from JON.models import Asset, Vehicle, Inventory, Place, Driver


class TagListSerializer(serializers.Field):
    def to_internal_value(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_representation(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        if type(data) is list:
            return data
        return data.values_list('name', flat=True)


class TagSerializer(serializers.ModelSerializer):
    tags = TagSerializerField()

    class Meta:
        model = Tag
        fields = '__all__'  # ('name', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(TagSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance


class User2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'is_active')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('pk', 'is_active', 'name', 'slug')


class AccountUserSerializer(serializers.HyperlinkedModelSerializer):
    user = User2Serializer()
    organization = AccountSerializer()
    class Meta:
        model = AccountUser
        fields = ('pk', 'is_admin', 'user', 'organization')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializer()
    class Meta:
        model = Place
        fields = ('pk', 'parent_place', 'street_address', 'street', 'zipcode', 'country', 'state', 'city', 'latitude', 'longitude', 'created', 'updated', 'tags')


class ProjectSerializer(serializers.ModelSerializer):
    orders = serializers.HyperlinkedRelatedField(many=True, view_name='order_detail', read_only=True)
    tags = TagListSerializer()

    class Meta:
        model = Project
        fields = ('pk', 'name', 'text', 'is_active', 'orders', 'tags')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        item = Project.objects.create(**validated_data)
        for tag_data in tags_data:
            item.tags.add(tag_data)
        return item

    def update(self, instance, validated_data):
        """
        Update and return an existing `project` instance, given the validated data.
        """
        if 'tags' in validated_data:
            tags_data = validated_data.pop('tags')
            for tag_data in tags_data:
                instance.tags.add(tag_data)

        super(ProjectSerializer, self).update(instance, validated_data)
        return instance

class ProgramSerializer(serializers.ModelSerializer):
    # projects = serializers.HyperlinkedRelatedField(many=True, view_name='project_detail', read_only=True)
    projects = ProjectSerializer(many=True)
    tags = TagSerializerField()  # TagListSerializer()

    class Meta:
        model = Program
        fields = ('pk', 'name', 'text', 'projects', 'tags')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        # prjs_data = validated_data.pop('projects') # TODO save projects with tags
        item = Program.objects.create(**validated_data)
        # for prj in prjs_data:
        # item.projects.add(prj)
        # p=Project.objects.create(**prj)
        # p.program_set.create(item)
        for tag_data in tags_data:
            # Tag.objects.create(program=item, **tag_data)
            # item.tags.create(**tag_data)
            item.tags.add(tag_data)
        return item


class OrderTypeSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializer()

    class Meta:
        model = OrderType
        fields = ('pk', 'name', 'duration', 'delivery_datetime', 'price', 'tags')


class ConditionSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializer()

    class Meta:
        model = Condition
        fields = ('pk', 'name', 'value', 'measure', 'tags')


class ContractSerializer(serializers.HyperlinkedModelSerializer):
    conditions = serializers.HyperlinkedRelatedField(many=True, view_name='condition_detail', read_only=True)
    organization = serializers.HyperlinkedRelatedField(view_name='account_detail', read_only=True)
    buyer = serializers.HyperlinkedRelatedField(view_name='account_user_detail', read_only=True)
    tags = TagListSerializer()

    class Meta:
        model = Contract
        fields = ('pk', 'name', 'organization', 'buyer', 'text', 'conditions', 'tags')


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagListSerializer()
    user = AccountUserSerializer()
    org = AccountSerializer()
    class Meta:
        model = Asset
        fields = ('pk', 'name', 'text', 'org', 'user', 'type', 'tags')


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    asset = AssetSerializer()
    tags = TagListSerializer()

    class Meta:
        model = Vehicle
        fields = ('pk', 'name', 'model_name', 'text', 'asset', 'manufacturer_vehicle', 'manufacturer_year', 'type', 'cargo_capacity', 'load_weight', 'load_description', 'tags')


class InventorySerializer(serializers.HyperlinkedModelSerializer):
    asset = AssetSerializer()
    tags = TagListSerializer()

    class Meta:
        model = Inventory
        fields = ('name', 'text', 'asset', 'tags')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    # type = serializers.PrimaryKeyRelatedField(read_only=True)
    type = OrderTypeSerializer(read_only=True)
    status = serializers.StringRelatedField(read_only=True)
    contract = serializers.HyperlinkedRelatedField(view_name='contract_detail', read_only=True)
    vehicle = serializers.HyperlinkedRelatedField(view_name='vehicle_detail', read_only=True)
    driver = serializers.HyperlinkedRelatedField(view_name='driver_detail', read_only=True)
    tags = TagListSerializer()

    class Meta:
        model = Order
        fields = ('pk', 'text', 'type', 'status', 'contract', 'pickup_datetime', 'delivery_promise_eta', 'delivery_distance', 'delivery_datetime', 'vehicle', 'driver', 'tags')


class DriverSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user_detail', read_only=True)
    vehicles = serializers.HyperlinkedRelatedField(many=True, view_name='vehicle_detail', read_only=True)
    tags = TagListSerializer()

    class Meta:
        model = Driver
        fields = ('pk', 'user', 'department', 'title', 'company', 'vehicles', 'tags')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    api = serializers.PrimaryKeyRelatedField(many=True, queryset=API.objects.all())

    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email', 'groups', 'api')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('pk', 'name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('pk', 'name')


class APISerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username',default='runurvlam')
    class Meta:
        model = API
        fields = ('created', 'title', 'owner', 'language', 'classes', 'methods', 'style', 'example')

    def create(self, validated_data):
        """
        Create and return a new `API` instance, given the validated data.
        """
        return API.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `API` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.language = validated_data.get('language', instance.language)
        instance.classes = validated_data.get('classes', instance.classes)
        instance.methods = validated_data.get('methods', instance.methods)
        instance.style = validated_data.get('style', instance.style)
        instance.example = validated_data.get('example', instance.example)
        instance.save()
        return instance
