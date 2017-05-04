from statistics import mode

from django.contrib.admin import models
from django.db import models
from django.utils import timezone

# Create your models here.
from postgresql.driver.dbapi20 import dbapi_type


class Company(models.Model):
    name = models.CharField(db_column='Name', max_length=250, blank=True, null=True)
    telephone = models.CharField(db_column='Telephone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='Url', unique=True, max_length=500, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=400, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='Site', max_length=200, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    category1 = models.CharField(db_column='Category1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    category2 = models.CharField(db_column='Category2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    category3 = models.CharField(db_column='Category3', max_length=200, blank=True, null=True)  # Field name made lowercase.
    category4 = models.CharField(db_column='Category4', max_length=200, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dateparsed = models.DateField(db_column='Dateparsed', blank=True, null=True)  # Field name made lowercase.
    Inn = models.CharField(db_column='Inn', max_length=12, blank=True, null=True)
    Kpp = models.CharField(db_column='Kpp', max_length=12, blank=True, null=True)
    Ogrn = models.CharField(db_column='Ogrn', max_length=15, blank=True, null=True)

    class Meta:
        db_table ='company'

class People(models.Model):
    FirstName = models.CharField(db_column='FirstName',max_length=200 )
    SecondName = models.CharField(db_column='SecondName',max_length=200)
    LastName = models.CharField(db_column='LastName', max_length=200)


    class Meta:
        db_table ='people'

class Sources(models.Model):
    Name = models.CharField(db_column = 'Name', max_length = 200)
    Url =  models.CharField(db_column='Url', max_length=200)
    Type = models.CharField(db_column='Type',max_length=30)
    Description = models.TextField(db_column='Description', blank = True, null = True)

    class Meta:
        db_table = 'source'

class Posts (models.Model):
    Body = models.CharField(db_column = 'Body', max_length = 200)
    Url =  models.CharField(db_column='Url',max_length=200, unique=True)
    Type = models.CharField(db_column='Type',max_length=30)
    DataCreated = models.DateField(db_column='DateCreated')
    Author = models.ForeignKey('People',on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'


class ParsingPlan (models.Model):
    NameTask = models.CharField(db_column = 'Nametask', max_length = 30)
    Parametr = models.CharField(db_column='Parametr', max_length=200)
    Starturl =  models.CharField(db_column='Starturl', max_length=200, unique=True)
    DateCreated = models.DateField(db_column='Datecreated')
    Source_FK = models.ForeignKey('Sources')

    class Meta:
        db_table = 'parsing'

class Avatars (models.Model):
    ProfileUrl = models.CharField(db_column='ProfileUrl', max_length=400, blank=True, null=True,unique=True)
    Url = models.CharField(db_column='Url', max_length=400, blank=True, null=True)
    ParsingUrl_FK = models.ForeignKey('ParsingPlan',null=True, blank=True)
    People_FK = models.ForeignKey('People',null=True,blank=True)
    Company_FK = models.ForeignKey('Company', null=True,blank=True)
    DateParsed = models.DateTimeField(db_column='Dateparsed', null=True, blank=True)
    DateCreated =models.DateTimeField(db_column='Datecreated',auto_now_add=True, null=True, blank=True)
    Organization = models.CharField(db_column='Organization', max_length=400, blank=True, null=True)
    Name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'avatars'

