from django.db import models


class URLDATA(models.Model):
    Long_URL  = models.CharField(max_length=250)
    Short_URL = models.CharField(max_length=10,unique=True)

    def __str__(self):
            return f"Long URL => {self.Long_URL} Short URL => {self.Short_URL}"