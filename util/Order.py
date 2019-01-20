class Order:
    def __init__(self, type, limit_price, amount, place_time):
        self.type = type
        self.limit_price = limit_price
        self.amount = amount
        self.state = '未成交'
        self.place_time = place_time  # 下单时间
        self.margin_level = 10
        self.stop_win_price = limit_price * 1.1
        self.stop_lose_price = limit_price * 0.9
