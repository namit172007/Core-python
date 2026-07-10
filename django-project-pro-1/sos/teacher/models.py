from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    login_id = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    joining_date = models.DateField(max_length=20)
    address = models.CharField(max_length=50)

    class Meta:
        db_table = 'sos_user2'


from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
