from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse, JsonResponse
from .models import Accounts, Profile, Sales, Subscription,Stock
from  .serializer import ProfileSerializer,SubscriptionSerializer,SalesSerializer,StockSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = ProfileSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status = 400)
    elif request.method == "GET":
        print(request.headers)
        try:
            try:
                a = Profile.objects.get(name=request.user)
            except:
                d = TokenAuthentication().authenticate(request)
                print(d[0])
                a = Profile.objects.get(name=d[0])

        except:
            return JsonResponse({"message":"You're not authenticated"}, status=500)

        print(a)
        serializer = ProfileSerializer(a)
        return JsonResponse(serializer.data, safe= False)
    return Response({"message":"You're not authenticated"}, status=500)
@csrf_exempt
def sales(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = SalesSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status = 400)
    elif request.method == "GET":
        a = Sales.objects.get(name=request.user)
        serializer = SalesSerializer(a, many=True)
        return JsonResponse(serializer.data, safe= False)


@csrf_exempt
def subscription(request):

    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = SubscriptionSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status = 400)
    elif request.method == "GET":
        a = Subscription.objects.get(name=request.user)
        serializer = SubscriptionSerializer(a, many=True)
        return JsonResponse(serializer.data, safe= False)


@csrf_exempt
def stock(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = StockSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status = 400)
    elif request.method == "GET":
        a = Stock.objects.get(name=request.user)
        serializer = StockSerializer(a, many=True)
        return JsonResponse(serializer.data, safe= False)