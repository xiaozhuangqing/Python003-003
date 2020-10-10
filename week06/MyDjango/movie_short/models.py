from django.db import models

# Create your models here.

class MovieShort(models.Model):
    short = models.CharField(max_length=500, blank=True, null=True)
    starts = models.IntegerField(blank=True, null=True)
    date = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie_short'
