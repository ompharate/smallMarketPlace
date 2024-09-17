
from django.contrib import admin
from django.urls import path
from cre.views import index
from cre.views import contact

urlpatterns = [
    path("",index,name="index"),
    path('admin/', admin.site.urls),
    path("contact/",contact,name="contact"),
]
