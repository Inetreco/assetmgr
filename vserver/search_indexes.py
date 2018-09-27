# Haystack imports
from haystack import indexes

# Import from our apps
from vserver.models import Vserver

class VserverIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    owner = indexes.CharField(model_attr='owner')
    #decomissioned = indexes.BooleanField(model_attr='decomissioned')
    hostname = indexes.CharField(model_attr='hostname')
    hypervisor = indexes.CharField(model_attr='hypervisor')
    #server_cpu = indexes.CharField(model_attr='server_cpu')
    #server_ram = indexes.CharField(model_attr='server_ram')
    #local_storage = indexes.CharField(model_attr='local_storage')
    current_roles = indexes.CharField(model_attr='current_roles')
    ip_v4_address = indexes.CharField(model_attr='ip_v4_address')
    ip_v4_address_public = indexes.CharField(model_attr='ip_v4_address_public')
    ip_v6_address = indexes.CharField(model_attr='ip_v6_address')
    other = indexes.CharField(model_attr='other')

    def get_model(self):
        return Vserver

    def index_queryset(self, using=None):
        return self.get_model().objects.all()