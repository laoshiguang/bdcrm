from api import models
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class Receive(APIView):
    def get(self, request):
        msgid = request.data.get("msgid")
        devid = request.data.get("devid")
        cmd = request.data.get("cmd")
        data = request.data.get("data")
        print(request.data)
        print(msgid)
        print(devid)
        print(cmd)
        print(data)
        ret = {"code": 1000}
        if cmd == "test":
            ret["code"] = "ok"
        return Response(ret)
