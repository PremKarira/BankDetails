from django.db import models

class Bankdetails(models.Model):
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    account_holder_name = models.CharField(max_length=100, blank=False)
    account_number = models.CharField(max_length=20, blank=False)
    ifsc_code = models.CharField(max_length=11, blank=False)
    bank_name = models.CharField(max_length=100, blank=False)
    branch_name = models.CharField(max_length=100, blank=False)
    update_allowed = models.BooleanField(default=True)

class Updaterequests(models.Model):
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    account_holder_name = models.CharField(max_length=100, blank=False)
    account_number = models.CharField(max_length=20, blank=False)
    ifsc_code = models.CharField(max_length=11, blank=False)
    bank_name = models.CharField(max_length=100, blank=False)
    branch_name = models.CharField(max_length=100, blank=False)

class UsersList(models.Model):
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(max_length=50, blank=False, null=False)

