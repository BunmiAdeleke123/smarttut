from django.shortcuts import render,  redirect
from django.http import HttpResponse, JsonResponse
def profile(request):
    return redirect("/api/profile/")
