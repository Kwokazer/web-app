from django.db import models

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    office_id = models.ForeignKey(
        'Office',  
        on_delete=models.CASCADE,
    )
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthdate = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Offices(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.ForeignKey(
        'Countries',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name