
from bson import ObjectId
from pressure.server import MockServer

server = MockServer(lang="zh_CN").agent


def gen_order_params():
    """
    生成订单参数
    :return:
    """

    return {
        "order_id": ObjectId(),
        "name": server.name(),
        "phone": server.phone_number(),
        "address": server.address(),
        "job": server.job(),
        "color": server.color(),
        "company": server.company()
    }
