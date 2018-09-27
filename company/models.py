#Django native imports
from django.contrib import admin
from django.db import models
from django.urls import reverse, reverse_lazy

class Company(models.Model):
    name = models.CharField("Company name", max_length=100, default="Company name")
    address = models.CharField("Company address", max_length=100)
    phone = models.CharField("Company phone number", max_length=20)
    contact_person = models.CharField("Contact person", max_length=20)
    email = models.EmailField(unique=True)
    inactive = models.BooleanField("Inactive", default=False)

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its edit view page
        """
        #return reverse('company_create')
        return reverse('company_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('company_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('company_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Company"
        return class_name

    class Meta:
        verbose_name_plural = "Companies"



