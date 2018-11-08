from django.db import models
from django.conf import settings

# Create your models here.


class TM(models.Model):
    talker = models.CharField(max_length=40, blank=False)
    message = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.talker + " " + self.message


class Concept(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()


class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    is_sym = models.BooleanField


class RelationEntry(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE)
    related_concepts = models.ManyToManyField(Concept)
    f_id = models.CharField(max_length=20)
    s_id = models.CharField(max_length=20)
    f_is_s = models.CharField(max_length=20)
    s_is_f = models.CharField(max_length=20)






