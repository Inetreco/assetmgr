# Haystack imports
from haystack import indexes

# Import from our apps
from station.models import Station

class StationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    owner = indexes.CharField(model_attr='owner')
    #decomissioned = indexes.BooleanField(model_attr='decomissioned')
    hostname = indexes.CharField(model_attr='hostname')
    location = indexes.CharField(model_attr='location')
    site_name = indexes.CharField(model_attr='site_name')
    #g4 = indexes.BooleanField(model_attr='g4')
    #gras = indexes.BooleanField(model_attr='gras')
    antenna_brand = indexes.CharField(model_attr='antenna_brand')
    antenna_type = indexes.CharField(model_attr='antenna_type')
    antenna_sn = indexes.CharField(model_attr='antenna_sn')
    #has_radome = indexes.BooleanField(model_attr='has_radome')
    receiver_brand = indexes.CharField(model_attr='receiver_brand')
    receiver_type = indexes.CharField(model_attr='receiver_type')
    receiver_sn = indexes.CharField(model_attr='receiver_sn')
    company_asset_number = indexes.CharField(model_attr='company_asset_number')
    #manufacture_year = indexes.IntegerField(model_attr='manufacture_year')
    #warranty = indexes.CharField(model_attr='warranty')
    os = indexes.CharField(model_attr='os')
    site_router_ip = indexes.CharField(model_attr='site_router_ip')
    #internet_connection_type = indexes.CharField(model_attr='internet_connection_type')
    #bandwidth = indexes.CharField(model_attr='bandwidth')
    #site_contact = indexes.CharField(model_attr='site_contact')
    other = indexes.CharField(model_attr='other')

    def get_model(self):
        return Station

    def index_queryset(self, using=None):
        return self.get_model().objects.all()