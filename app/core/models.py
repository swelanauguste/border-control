import uuid

from django.db import models
from django.utils.text import slugify


class WorkstationRole(models.Model):
    role = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    desc = models.TextField("description", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.role)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.role


# class OtherLocation(models.Model):
#     sub_location = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.sub_location


class Workstation(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    roles = models.ManyToManyField(WorkstationRole, blank=True)
    computer_name = models.CharField(max_length=100)
    computer_sn = models.CharField(max_length=100, unique=True, blank=True, null=True)
    network = models.GenericIPAddressField(unique=True, blank=True, null=True)
    ip_address = models.CharField(max_length=3, unique=True)
    peripherals = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.computer_name


class ContactPerson(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True, db_index=True
    )
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField(blank=True)
    contact_tel = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.contact_name} - {self.contact_tel}"


class Location(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    l_name = models.CharField("location", max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    contact_person = models.ForeignKey(
        ContactPerson, on_delete=models.CASCADE, blank=True, null=True
    )
    workstations = models.ManyToManyField(Workstation, blank=True)
    
    class Meta:
        ordering = ["l_name"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.l_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.l_name
