
from django.contrib import admin
from django.urls import path
from django.urls import include, path
import polls_app.views
urlpatterns = [
    path('polls/', include('polls_app.urls')),
    path('admin/', admin.site.urls),
]
