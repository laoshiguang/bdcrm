from api import models
from rest_framework.serializers import ModelSerializer


class GoodsModelSerializers(ModelSerializer):
    """
       商品序列化
       """

    class Meta:
        model = models.Goods
        fields = ["id", "title", "old_price", "new_price", "desc"]
