from django.db import models
from datetime import datetime

# Create your models here.
# Just like we did with listings we want a main field for the realtor, and we're gonna use their name.
# Thus, we did the method and linked it to "name" in our class. 

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name

# Now we wanna put this all into the database. So, we need to make a migration and run it. 
    
