#from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser , Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.gis.db import models
from django.conf import settings
from django.contrib.gis.geos import Point
from django.utils.encoding import python_2_unicode_compatible
from django_countries.fields import CountryField
from location_field.models.spatial import LocationField #GeoSpatial Support
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager
from organizations.models import Organization, OrganizationUser
from model_utils.fields import MonitorField, StatusField
from model_utils import Choices
#from haystack.utils.geo import Point
import simplejson, urllib
import datetime

# Create your models here.

class WorldBorder(models.Model):
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    def __str__(self):  # __unicode__ on Python 2
        return self.name


#Locations -Geography
class Place(models.Model):
    parent_place = models.ForeignKey('self', null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank = True)
    street = models.CharField(max_length=255, null=True, blank = True)
    zipcode = models.CharField(max_length=7, null=True, blank = True)
    city = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True, blank = True)
    country = CountryField(default='US')
    location = LocationField(based_fields=['city'], zoom=7, default='POINT(0.0 0.0)', null=True, blank=True)
    objects = models.GeoManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)
    STATUS = Choices('', 'published')

    @property
    def coordinates(self):
        return self.location.coords

    @property
    def latitude(self):
        return '%s' % self.location.x

    @property
    def longitude(self):
        return '%s' % self.location.y

    def __str__(self): # __unicode__ on Python 2
        return '{2} {0}, {1}'.format (self.location.x, self.location.y, self.city)

    @property
    def address(self):
        return '{0} {1}, {2}, {3}, {4} {5}'.format(self.street_address, self.street, self.city, self.state, self.country, self.zipcode)


#User Extensions
class MyUser(AbstractBaseUser):
    USERNAME_FIELD = 'identifier'
    date_of_birth = models.DateField()
    REQUIRED_FIELDS = ['date_of_birth', 'nationality']
    tags = TaggableManager(blank=True)

##Profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    company_name = models.CharField(max_length=100)
    fax_number = PhoneNumberField(blank=True)
    place = models.OneToOneField(Place, null=True)
    tags = TaggableManager(blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()


# Organization
class Account(Organization):

    class Meta:
        proxy = True
        verbose_name = 'organization'


class AccountUser(OrganizationUser):

    class Meta:
        proxy = True
        verbose_name = 'member'
    def __str__(self):
        return u'{0} ({1})'.format(self.user.username if self.user.is_active else self.user.email, self.organization.name)


# Employee
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, default = 'IC')
    company = models.CharField(max_length=100, default = 'Runur')

    tags = TaggableManager(blank=True)
    def __str__(self):
        return self.user.get_username()


# Asset
class Asset(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    org = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(AccountUser, on_delete=models.CASCADE, null=True, blank=True)
    CAPITAL = 'CP'
    GOOD = 'GD'
    TYPES = (
        (CAPITAL, 'Capital'),
        (GOOD, 'Good'),
    )
    type = models.CharField(max_length=2, choices=TYPES, default=CAPITAL)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

# Vehicle
class Vehicle(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    model_name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    manufacturer_vehicle = models.CharField(max_length=64, null=True, blank=True)
    manufacturer_year = models.IntegerField(null=True, blank=True)
    CAR = 'car'
    TRUCK = 'truck'
    BICYCLE  = 'bicycle'
    MOTORCYCLE = 'motorcycle'
    TYPES = (
        (CAR, 'Car'),
        (TRUCK, 'Truck'),
        (BICYCLE, 'Bicycle'),
        (MOTORCYCLE, 'Motorcycle'),
    )
    type = models.CharField(max_length=16, choices=TYPES, default=CAR)
    cargo_capacity = models.FloatField(null=True, blank=True)
    load_weight = models.FloatField(default=0.00, null=True, blank=True)
    load_description = models.TextField(null=True, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


class Driver(Employee):
    pos = models.OneToOneField(Place, null=True) # current position/coordinates
    vehicles = models.ManyToManyField(Vehicle, blank=True)


# Order Type
class OrderType(models.Model):
    TYPE0 = 0
    TYPE1 = 1
    TYPE2 = 2
    TYPE3 = 3
    TYPE4 = 4
    ORDER_TYPES = (
        (TYPE0, 'None'),
        (TYPE1, 'Subscription'),
        (TYPE2, 'Overnight'),
        (TYPE3, 'Day Delivery'),
        (TYPE4, 'Hotshot'),
    )
    name = models.IntegerField(choices=ORDER_TYPES, default=TYPE0)
    duration = models.DurationField(null=True, blank=True)
    delivery_datetime = models.DateTimeField(auto_created=False, auto_now=False, auto_now_add=False, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True) # TODO: use MoneyField if needed
    tags = TaggableManager(blank=True)

    def __str__(self):
        return "{0}: ${1}".format(self.ORDER_TYPES[self.name][1], self.price)

    def get_name_display(self):
        return self.ORDER_TYPES[self.name[1]]

DRAFTED = 0
CREATED = 1
ORDERED = 2
EN_ROUTE = 3
COMPLETED = 4
STATUSES = (
    (DRAFTED, 'Drafted'),
    (CREATED, 'Created'),
    (ORDERED, 'Ordered'),
    (EN_ROUTE, 'En Route'),
    (COMPLETED, 'Completed'),
)

# Condition
class Condition(models.Model):
    name = models.CharField(max_length=64, default='')
    value = models.FloatField(default=0.0)
    DISTANCE = 'km'
    MASS_KG = 'kg'
    TIME = 'h'

    INCH = 'in'
    FOOT = 'ft'
    YARD = 'yd'
    MILE = 'mi'
    OUNCE = 'oz'
    POUND = 'lb'


    # TODO: add US/UK measurements
    MEASURES = (
        (DISTANCE, 'Kilometer(-s)'),
        (MASS_KG, 'Kilogram(-s)'),
        (TIME, 'Hour(-s)'),
        (INCH, 'Inch(-es)'),
        (FOOT, 'Foot(-s)'),
        (YARD, 'Yard(-s)'),
        (MILE, 'Mile(-s)'),
        (OUNCE, 'Ounce(-s)'),
        (POUND, 'Pound(-s)'),
    )
    measure = models.CharField(max_length=2, choices=MEASURES, default=DISTANCE) # distance, mass, time
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

# Contract
class Contract(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    conditions = models.ManyToManyField(Condition)

    organization = models.OneToOneField(Account, null=True)
    buyer = models.OneToOneField(AccountUser, null=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


# Order
class Order(models.Model):

    no = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    type = models.ForeignKey(OrderType, null=True, blank=True)
    status = models.IntegerField(choices=STATUSES, default=DRAFTED)
    contract = models.ForeignKey(Contract, null=True)

    # current location
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    pickup_datetime = models.DateTimeField(auto_created=False, auto_now_add=False, auto_now=False, null=True)
    delivery_promise_eta = models.DateTimeField(auto_created=False, auto_now=False, auto_now_add=False, null=True, blank=True)
    delivery_distance = models.FloatField(default=0.00, null=True, blank=True) # length/distance

    delivery_datetime = models.DateTimeField(auto_created=False, auto_now=False, auto_now_add=False, null=True, blank=True)

    vehicle = models.ForeignKey(Vehicle, null=True, blank=True)
    driver = models.ForeignKey(Driver, null=True, blank=True)

    tags = TaggableManager(blank=True)

    def save(self):
        try:
            # driver_place=self.driver.user.profile.place.location
            # buyer_place=self.contract.buyer.user.profile.place.location
            # self.delivery_distance = buyer_place.distance(driver_place) * 100
            # orig_coord = '{0},{1}'.format(buyer_place.x,buyer_place.y)
            # dest_coord = '{0},{1}'.format(driver_place.x,driver_place.y)

            orig_coord = urllib.parse.quote(self.driver.pos.address)
            dest_coord = urllib.parse.quote(self.contract.buyer.user.profile.place.address)
            mode = 'bicycling' if self.vehicle.type == self.vehicle.BICYCLE else 'driving'
            api_key = settings.GOOGLE_MAP_API_KEY
            lang = 'en-US'
            url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode={2}&language={3}&sensor=false&key={4}".format(
                str(orig_coord), str(dest_coord), mode, lang, api_key)
            result = simplejson.load(urllib.request.urlopen(url))
            duration_value = result['rows'][0]['elements'][0]['duration']['value']
            distance_value = result['rows'][0]['elements'][0]['distance']['value']

            delivery_promise_eta = self.pickup_datetime + datetime.timedelta(seconds=duration_value)
            self.delivery_promise_eta = delivery_promise_eta
            self.delivery_distance = distance_value / 1000 # km
        except Exception as e:
            self.delivery_distance = 0.00

        super(Order, self).save()

    def __str__(self):
        return "Order #{0}".format(self.pk)

# Project
@python_2_unicode_compatible
class Project(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    orders = models.ManyToManyField(Order, blank=True)
    is_active = models.BooleanField(blank=True)
    # total_price = TODO SUM of all orders.order.order_type.price (implementation in view ?)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

# Program
@python_2_unicode_compatible
class Program(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name


# Inventory
class Inventory(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, null=True, blank=True)

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Inventories'

##Task
class Task(models.Model):
    tags = TaggableManager(blank=True)
    class Meta:
        permissions = (
            ("view_task", "Can see available tasks"),
            ("change_task_status", "Can change the status of tasks"),
            ("close_task", "Can remove a task by setting its status as closed"),
        )

##Messages
class Message(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    tags = TaggableManager(blank=True)
    class Meta:
        permissions = (
            ("view_message", "Can see available messages"),
            ("close_message", "Can remove a message by setting its status as closed"),
        )
