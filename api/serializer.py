from rest_framework import serializers
from .models import Accounts, Profile, Sales, Subscription,Stock

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields=["name","email","country","eaccount","device_name","epp_version","ip_address","date","token","sub_status","user_id","status"]

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields=["name","user_id","sub_plan","sub_status"]

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields=["name","customer_name","total_amount","items","date"]

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields=["name","stock_name","quantity","unit_price","date","status","cartegory"]
