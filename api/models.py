# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TodoItem(models.Model):
    state = models.IntegerField(max_length=50, default=0)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return '%d: %s' % (self.id,  self.escription)
