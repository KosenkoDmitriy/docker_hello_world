from django.http import HttpResponse
#from drf_haystack.serializers import HaystackSerializer
#from drf_haystack.viewsets import HaystackViewSet
#from JON.models import Location
#from .search_indexes import LocationIndex

'''
class LocationSerializer(HaystackSerializer):

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [LocationIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "address", "city", "zip_code", "autocomplete"
        ]


class LocationSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Location]

    serializer_class = LocationSerializer
'''
def index(request):
    return HttpResponse("Hi there ;)You're at the Runur Search index.")
