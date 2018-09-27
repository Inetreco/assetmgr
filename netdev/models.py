#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy

# Import from our apps
from company.models import Company


def save_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/netdev/<hostname>/<filename>
    return '{0}/{1}/{2}'.format("netdev", instance.hostname, filename)

class Netdev(models.Model):

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)

    # Model
    hostname = models.CharField("Hostname", max_length=100, default=None)
    decomissioned = models.BooleanField("Decomissioned", default=False)
    decomissioned_date = models.DateField(default="2023-12-31")
    location = models.CharField("Location", max_length=100, default=None)
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    device_type = models.CharField("Device type", max_length=30)
    brand = models.CharField("Brand", max_length=20)
    netdev_model = models.CharField("Model", max_length=20)
    generation = models.CharField("Generation", max_length=5)
    manufacture_year = models.IntegerField("Year of manufacture")
    os = models.CharField("Device image", max_length=100, default=None)
    port_number = models.IntegerField("Number of physical network ports")
    port_description = models.CharField("Port description", max_length=50)
    serial_number = models.CharField("Serial number", max_length=20)
    company_asset_number = models.CharField("Company Asset Number", max_length=30)
    warranty = models.CharField("Warranty status", max_length=100)
    current_roles = models.CharField("Current roles", max_length=100)
    ip_v4_address = models.CharField("Private ipv4 address", max_length=100, default=None)
    ip_v4_address_public = models.CharField("Public ipv4 address", max_length=100, default=None)
    ip_v6_address = models.CharField("IPv6 address", max_length=100, default=None)
    file_picture_1 = models.FileField("Front Picture",blank=True, default=None, upload_to=save_directory_path)
    file_picture_2 = models.FileField("Back Picture",blank=True, default=None, upload_to=save_directory_path)
    file_other = models.FileField("Other file/Zip file if many", blank=True, default=None, upload_to=save_directory_path)
    other = models.TextField("Notes", max_length=500)

    def __str__(self):
        return "{}, S/N {}".format(self.hostname, self.ip_v4_address)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        #return reverse('netdev_create')
        return reverse('netdev_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('netdev_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('netdev_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Network Device"
        return class_name


    class Meta:
        verbose_name_plural = "Network Devices"
