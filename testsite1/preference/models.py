from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Choice(models.Model):
    text = models.CharField(max_length=300)
    score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    
    def streakchange(self):
        return 1
        # changes the streak - either increased by 1, decreased by 1, or taken to 0
    def scorechange(self):
        return 1
        # increases or decreases the score of the choice by 2^(streak)
    def rankchange(self):
        return 1
        # not sure if this is necessary, or if I can just find the rank of everything by sorting the scores. 
        # honestly not sure if ranks are necessary. 
    def __str__(self):
        return self.text
