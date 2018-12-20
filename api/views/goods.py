from api import models

from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers.goods import GoodsModelSerializers


class GoodsView(APIView):
    def get(self, request):
        dev_id = request.GET.get("dev_id")
        print(dev_id)
        goods_list = models.Goods.objects.filter(device=dev_id)
        gs = GoodsModelSerializers(instance=goods_list, many=True)
        print(gs.data)
        return Response(gs.data)
