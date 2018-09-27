# Haystack imports
from haystack import indexes

# Import from our apps
from company.models import Company

class CompanyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    address = indexes.CharField(model_attr='address')
    phone = indexes.CharField(model_attr='phone')
    contact_person = indexes.CharField(model_attr='contact_person')
    email = indexes.CharField(model_attr='email')
    #inactive = indexes.BooleanField(model_attr='inactive')

    def get_model(self):
        return Company

    def index_queryset(self, using=None):
        return self.get_model().objects.all()