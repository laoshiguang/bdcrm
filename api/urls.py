from django.conf.urls import url
from django.contrib import admin
from api.views import wk_mip, goods

urlpatterns = [
    url(r'^receive/', wk_mip.Receive.as_view()),
    url(r'^send/', wk_mip.Send.as_view()),
    url(r'^goods/', goods.GoodsView().as_view()),
]
