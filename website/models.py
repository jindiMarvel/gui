from __future__ import unicode_literals
from django.db import models
# Create your models2 here.
class IMG(models.Model):
    img = models.ImageField(upload_to='upload')
    
    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url
