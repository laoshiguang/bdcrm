from django.conf.urls import url
from django.contrib import admin
from api.views import wk_mip
urlpatterns = [
    url(r'^receive/', wk_mip.Receive.as_view()),
]
