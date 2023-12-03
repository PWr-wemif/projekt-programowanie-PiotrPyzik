from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from unidecode import unidecode

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Order.Status.PUBLISHED)


class Client(models.Model):
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    phone_number = models.IntegerField(blank = True)
    slug = models.SlugField(max_length=255,blank=True, unique=True)
    
    
    def __str__(self):
        return self.last_name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(f"{self.first_name}_{self.last_name}"))
        super(Client, self).save(*args, **kwargs)


    
    
class Order(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name='client')
    created = models.DateField(default = timezone.now)
    due = models.DateField(blank=True)
    slug = models.SlugField(max_length=255)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    def __str__(self):
        return self.status
    


class Element(models.Model):
    name = models.CharField(max_length=20, blank=True)
    width = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    length = models.FloatField(blank=True)
    count = models.IntegerField(blank=True)
    total_volume = models.FloatField(blank=True)
    description = models.TextField(blank = True)
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='element')    
    slug = models.SlugField(max_length=255)
    def __str__(self):
        return self.name
    