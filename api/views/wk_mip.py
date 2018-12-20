from api import models
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
import datetime, requests
from api.serializers.wk_mip import ReceiveModelSerializers


# Create your views here.
class Receive(APIView):
    def post(self, request):
        msg_id = request.data.get("msgid")
        dev_id = request.data.get("devid")
        cmd = request.data.get("cmd")
        data = request.data.get("data")
        ret = {}
        try:
            models.Receive.objects.create(msg_id=msg_id, dev_id=dev_id, cmd=cmd, data=data)
            if cmd == "test":
                ret["code"] = "ok"
            if cmd == "online":
                models.Device.objects.filter(dev_id=dev_id).update(status=1)
            if cmd == "offline":
                models.Device.objects.filter(dev_id=dev_id).update(status=2)
            if cmd == "41":
                pass
            if cmd == "42":
                pass
        except Exception as e:
            ret["code"] = 1001

        return Response(ret)


class Send(APIView):
    def post(self, request):
        url = "http://api1.wkmip.cn/api/push"
        msg_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        dev_id = ""
        data = ""
        token = "xdkbcpfwJ3HgjTzvJHRqrm4y9CwRwHMUmtsdETtgwJD"
        data = {"msgid": msg_id, "devid": dev_id, "data": data, "token": token}
        ret = requests.post(url, data)
        return Response("ok")
