from api import models
from rest_framework.serializers import ModelSerializer


class ReceiveModelSerializers(ModelSerializer):
    """
       订阅消息序列化
       """

    class Meta:
        model = models.Receive
        fields = "__all__"


class SendModelSerializers(ModelSerializer):
    """
    平台发送数据序列化
    """

    class Meta:
        model = models.Send
        fields = "__all__"
