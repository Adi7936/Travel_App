from django.db import models



# Create your models here.




BEACH = 'Beach'
MOUNTAIN = 'Mountain'
CITY = 'City'
HISTORICAL = 'Historical'

CATEGORY_CHOICES = [
        (BEACH, 'Beach'),
        (MOUNTAIN, 'Mountain'),
        (CITY, 'City'),
        (HISTORICAL, 'Historical'),
    ]


class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

