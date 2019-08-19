class GoodsModel:
    def __init__(self,dict_commodity_info):
        self.dict_commodity_info = dict_commodity_info


class GoodsController:
    list_order = []

    def __init__(self,dict_commodity_info):
        self.dict_commodity_info = dict_commodity_info

    def buying(self):
        """
            购买
        """
        self.print_commodity_info()
        self.create_order()

        print("添加到购物车。")

    def print_commodity_info(self):
        """
            打印商品信息
        """
        for key, value in self.dict_commodity_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

    def create_order(self):
        """
            创建订单
        """
        cid = self.input_commodity_id()
        count = int(input("请输入购买数量："))
        order = {"cid": cid, "count": count}
        GoodsController.list_order.append(order)

    def input_commodity_id(self):
        """
            获取商品订单
        """
        while True:
            cid = int(input("请输入商品编号："))
            if cid in self.dict_commodity_info:
                break
            else:
                print("该商品不存在")
        return cid

    def settlement(self):
        """
            结算
        """
        self.print_orders()
        total_price = self.calculate_total_price()
        self.paying(total_price)

    def calculate_total_price(self):
        """
            计算总价格
        """
        total_price = 0
        for order in GoodsController.list_order:
            commodity = self.dict_commodity_info[order["cid"]]
            total_price += commodity["price"] * order["count"]
        return total_price

    def print_orders(self):
        """
            打印订单
        """
        for order in GoodsController.list_order:
            commodity = self.dict_commodity_info[order["cid"]]
            print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], order["count"]))

    def paying(self,total_price):
        """
            支付过程
        :param total_price: 需要支付的价格
        """
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                GoodsController.list_order.clear()
                break
            else:
                print("金额不足.")


class GoodsView:
    def __init__(self,dict_commodity_info):
        self.__controller = GoodsController(dict_commodity_info)

    def main(self):
        """
            选择菜单
        """
        while True:
            item = input("1键购买，2键结算。")
            if item == "1":
                self.__controller.buying()
            elif item == "2":
                self.__controller.settlement()


dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
deal = GoodsView(dict_commodity_info)
deal.main()