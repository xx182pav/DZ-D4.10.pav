from django.contrib import admin
from django.urls import path
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redactions/', views.redactions),
]
