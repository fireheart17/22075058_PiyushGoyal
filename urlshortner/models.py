from django.db import models
from django.core.validators import URLValidator
# Create your models here.
class OptionalSchemeURLValidator(URLValidator):
    def __call__(self, value):
        if '://' not in value:
            value = 'http://' + value
        super(OptionalSchemeURLValidator, self).__call__(value)
        
class ShortURL(models.Model):
    original_url = models.URLField(max_length=700,validators=[OptionalSchemeURLValidator()])
    short_url = models.CharField(max_length=100)
    time_date_created = models.DateTimeField()
    
    def __str__(self):
        return self.original_url