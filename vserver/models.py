#Django native imports
from django.db import models
from django.urls import reverse, reverse_lazy

# Import from our apps
from server.models import Server

def save_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/netdev/<hostname>/<filename>
    return '{0}/{1}/{2}'.format("vserver", instance.hostname, filename)

class Vserver(models.Model):
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default=None)

    # Model
    hostname = models.CharField("Hostname", max_length=100, default='localhost')
    owner = models.CharField("Owner/User/Admin", max_length=50, default='None')
    os = models.CharField("Operating system", max_length=50, default='None')
    decomissioned = models.BooleanField("Decomissioned", default=False)
    decomissioned_date = models.DateField(default="2023-12-31")
    hypervisor = models.ForeignKey(Server, on_delete=models.CASCADE)
    server_cpu = models.CharField("Server CPU", max_length=100)
    server_ram = models.CharField("Server RAM", max_length=100)
    local_storage = models.CharField("Local storage", max_length=100)
    current_roles = models.CharField("Current roles", max_length=100)
    ip_v4_address = models.CharField("IPv4 address", max_length=100, default="IPv4")
    ip_v4_address_public = models.CharField("Public ipv4 address", max_length=100, default=None)
    ip_v6_address = models.CharField("IPv6 address", max_length=100, default="IPv6")
    file_other = models.FileField("Other files/Zip file if many", blank=True, default=None, upload_to=save_directory_path)
    other = models.TextField("Notes", max_length=500)


    def __str__(self):
        return "{}, IP {}".format(self.hostname, self.ip_v4_address)

    def get_absolute_url(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('vserver_edit', args=[str(self.pk)])

    def get_delete(self):
        """
        Handy way of getting the url of the object to its delete view page
        """
        return reverse('vserver_delete', args=[str(self.pk)])

    def get_detail(self):
        """
        Handy way of getting the url of the object to its detail view page
        """
        return reverse('vserver_detail', args=[str(self.pk)])

    def get_class(self):
        """
        Handy way of getting the class of the object for the html templates
        """
        class_name = "vServer"
        return class_name

    class Meta:
        verbose_name_plural = "vServers"