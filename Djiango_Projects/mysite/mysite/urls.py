
from django.contrib import admin
from django.urls import path
from django.urls import include, path
import polls_app.views
urlpatterns = [
    path('', polls_app.views.index),
    path('admin/', admin.site.urls),
]
