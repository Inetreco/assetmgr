# Haystack imports
from haystack import indexes

# Import from our apps
from server.models import Server

class ServerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    hostname = indexes.CharField(model_attr='hostname')
    #decomissioned = indexes.BooleanField(model_attr='decomissioned')
    location = indexes.CharField(model_attr='location')
    owner = indexes.CharField(model_attr='owner')
    brand = indexes.CharField(model_attr='brand')
    #server_model = indexes.CharField(model_attr='server_model')
    generation = indexes.CharField(model_attr='generation')
    #manufacture_year = indexes.IntegerField(model_attr='manufacture_year')
    serial_number = indexes.CharField(model_attr='serial_number')
    company_asset_number = indexes.CharField(model_attr='company_asset_number')
    os = indexes.CharField(model_attr='os')
    #warranty = indexes.CharField(model_attr='warranty')
    #server_cpu = indexes.CharField(model_attr='server_cpu')
    #server_ram = indexes.CharField(model_attr='server_ram')
    #local_storage = indexes.CharField(model_attr='local_storage')
    current_roles = indexes.CharField(model_attr='current_roles')
    ip_v4_address = indexes.CharField(model_attr='ip_v4_address')
    ip_v4_address_public = indexes.CharField(model_attr='ip_v4_address_public')
    ip_v6_address = indexes.CharField(model_attr='ip_v6_address')
    ilo_ip_address = indexes.CharField(model_attr='ilo_ip_address')
    other = indexes.CharField(model_attr='other')

    def get_model(self):
        return Server

    def index_queryset(self, using=None):
        return self.get_model().objects.all()