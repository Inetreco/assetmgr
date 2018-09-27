# Haystack imports
from haystack import indexes

# Import from our apps
from netdev.models import Netdev

class NetdevIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='hostname')
    ip_v4_address = indexes.CharField(model_attr='ip_v4_address')
    #decomissioned = indexes.BooleanField(model_attr='decomissioned')
    location = indexes.CharField(model_attr='location')
    owner = indexes.CharField(model_attr='owner')
    device_type = indexes.CharField(model_attr='device_type')
    brand = indexes.CharField(model_attr='brand')
    #netdev_model = indexes.CharField(model_attr='netdev_model')
    #generation = indexes.CharField(model_attr='generation')
    os = indexes.CharField(model_attr='os')
    #manufacture_year = indexes.IntegerField(model_attr='manufacture_year')
    #port_number = indexes.IntegerField(model_attr='port_number')
    port_description = indexes.CharField(model_attr='port_description')
    serial_number = indexes.CharField(model_attr='serial_number')
    company_asset_number = indexes.CharField(model_attr='company_asset_number')
    #warranty = indexes.CharField(model_attr='warranty')
    current_roles = indexes.CharField(model_attr='current_roles')
    ip_v4_address_public = indexes.CharField(model_attr='ip_v4_address_public')
    ip_v6_address = indexes.CharField(model_attr='ip_v6_address')
    other = indexes.CharField(model_attr='other')

    def get_model(self):
        return Netdev

    def index_queryset(self, using=None):
        return self.get_model().objects.all()