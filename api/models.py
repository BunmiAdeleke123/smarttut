from django.db import models
from django_mysql.models import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from rest_framework.authtoken.models import Token

# Create your models here.
class Profile(models.Model):
    name =models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    eaccount = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    epp_version = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    sub_status = models.BooleanField(default=False)
    user_id = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default="inactive")


    def __str__(self):
        return(self.user_id)

class Subscription(models.Model):
    name =models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    sub_plan = models.CharField(max_length=100)
    sub_status = models.BooleanField(default=False)
    def __str__(self):
        return(self.user_id)


class Stock(models.Model):
    name =models.ForeignKey(User, on_delete=models.CASCADE)
    stock_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    date= models.CharField(max_length=100)
    status =models.CharField(max_length=100)
    cartegory = models.CharField(max_length=100)

    def __str__(self):
        return(self.name)

class Sales(models.Model):
    name =models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=100)
    total_amount = models.IntegerField()
    items = JSONField()
    date = models.CharField(max_length=100)  
    def __str__(self):
        return(self.name)


class Accounts(models.Model):
    name =models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    def __str__(self):
        return(self.name)

@receiver(post_save, sender=User)
def createauthtoken(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        try:
            Profile.objects.get(name=instance)
        except:
            a = Token.objects.get(user=instance)
            print(a)
            Profile.objects.create(name=instance, token=a.key)

