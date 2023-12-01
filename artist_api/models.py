from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    SOCIAL_LINKS=[('YT','Youtube'),('IG','Instagram'),('OT','Other')]
    link = models.URLField()
    workType = models.CharField(max_length=2,choices=SOCIAL_LINKS)

    def __str__(self):
        return self.link

class Artist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    work = models.ManyToManyField(Work)

    def __str__(self):
        return self.name

