#Django native imports
from datetime import date
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext as _

#Import from our apps
from company.models import Company
from netdev.models import Netdev

def save_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/netdev/<hostname>/<filename>
    return '{0}/{1}/{2}'.format("station", instance.hostname, filename)

class Station(models.Model):

    ANTENNA_TYPES = (
        ('TRM55971.00', 'TRM55971.00'),
        ('TRM57971.00', 'TRM57971.00'),
        ('SEPCHOKE_B3E6', 'SEPCHOKE_B3E6'),
        ('TRM1155000.10', 'TRM1155000.10'),
    )
    ANTENNA_BRANDS = (
        ('SEPTENTRIO', 'SEPTENTRIO'),
        ('TRIMBLE', 'TRIMBLE'),
    )
    RECEIVER_TYPES = (
        ('NETR9', 'NETR9'),
        ('NETR5', 'NETR5'),
        ('POLARX5', 'POLARX5'),
    )
    RECEIVER_BRANDS = (
        ('SEPTENTRIO', 'SEPTENTRIO'),
        ('TRIMBLE', 'TRIMBLE'),
    )
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)

    # Model
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    decomissioned = models.BooleanField("Decomissioned", default=False)
    decomissioned_date = models.DateField(default="2023-12-31")
    hostname = models.CharField("Site ID", max_length=7, default=None)
    location = models.CharField("Site Location", max_length=100, default=None)
    site_name = models.CharField("Site Name", max_length=100, default=None)    
    g4 = models.BooleanField("G4 station", help_text=_("Check this field, if it is G2/G4 station"), default=False)
    gras = models.BooleanField("GRAS station", help_text=_("Check this field, if it is GRAS station"), default=False)
    antenna_brand = models.CharField("Antenna brand", max_length=100, default=None, choices=ANTENNA_BRANDS)
    antenna_type = models.CharField("Antenna type", max_length=100, default=None, choices=ANTENNA_TYPES)
    antenna_sn = models.CharField("Antenna Serial Number", max_length=50, default=None)
    has_radome = models.BooleanField("Atenna with radome", help_text=_("Check this field, if the antenna has radome"), default=False)
    receiver_brand = models.CharField("Receiver brand", max_length=100, default=None, choices=RECEIVER_BRANDS)
    receiver_type = models.CharField("Receiver type", max_length=100, default=None, choices=RECEIVER_TYPES)
    receiver_sn = models.CharField("Receiver Serial Number", max_length=50, default=None)
    company_asset_number = models.CharField("Company Asset Number", max_length=30)
    manufacture_year = models.IntegerField("Year of manufacture", default=None)
    warranty = models.CharField("Warranty status", max_length=100, default=None)
    os = models.CharField("Firmware", max_length=100, default=None)
    ip_v4_address = models.CharField("GNSS receiver private ipv4 address", max_length=30, default=None)
    ip_v4_address_public = models.CharField("GNSS receiver public ipv4 address", max_length=100, default=None)
    site_router_ip = models.ForeignKey(Netdev, on_delete=models.CASCADE, default=None)
    internet_connection_type = models.CharField("Internet connection type", max_length=30, default=None)
    bandwidth = models.CharField("Download/Upload", max_length=20, default=None)
    file_picture_1 = models.FileField("Site Diagram",blank=True, default=None, upload_to=save_directory_path)
    file_picture_2 = models.FileField("Antenna Picture",blank=True, default=None, upload_to=save_directory_path)
    file_other = models.FileField("Other file/Zip file if many", blank=True, default=None, upload_to=save_directory_path)
    site_contact = models.CharField("Site contact", max_length=100, default=None)
    other = models.TextField("Notes", max_length=500, default=None)


    def __str__(self):
        return "Station ID {}, site name {}".format(self.hostname, self.site_name)


    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('station_edit', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('station_detail', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('station_delete', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "Station"
        return class_name

    class Meta:
        verbose_name_plural = "Stations"