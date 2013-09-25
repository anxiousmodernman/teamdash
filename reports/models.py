from django.db import models
from jsonfield import JSONField
from reportsettings import REPORTS_PATH


class Report(models.Model):

    name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    version = models.CharField(max_length=20, blank=True)  # can be blank
    author = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    schema = JSONField()
    #schedule = models.ManyToManyField('Schedule')

    def getPath(self):
        path = REPORTS_PATH + self.path
        return path

    def __unicode__(self):
        return self.name  # TODO upgrade this string representation?


class Schedule(models.Model):
    schedule_pattern = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.schedule_pattern

# todo is this needed?
class Script(models.Model):

    path = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    def __unicode__(self):
        return self.description






