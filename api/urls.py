
from django.urls import path, include
from .views import profile, sales, subscription
urlpatterns = [
    path('profile/',profile ),
    path('sales/',sales ),
    path('subscription/',subscription ),
]