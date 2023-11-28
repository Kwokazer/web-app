# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Countries(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'countries'


class Offices(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    countryid = models.ForeignKey(Countries, models.DO_NOTHING, db_column='CountryID')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=50)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'offices'


class Roles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    roleid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=150)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    officeid = models.ForeignKey(Offices, models.DO_NOTHING, db_column='OfficeID', blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
