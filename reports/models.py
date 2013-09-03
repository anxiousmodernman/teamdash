from django.db import models
from jsonfield import JSONField


class Report(models.Model):
    name = models.CharField(max_length=200)
    source_code = models.TextField()
    language = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    schema = JSONField()


