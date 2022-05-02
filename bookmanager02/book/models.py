from django.db import models

# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)