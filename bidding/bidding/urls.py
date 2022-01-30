
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bidding_app.urls', namespace='bidding_app')),
    path('user/', include('user.urls', namespace='user')),
]
