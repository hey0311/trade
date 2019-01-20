class Account:
    def __init__(self):
        self.orders = []
        self.blance = 100
        self.plots=[]
        self.cur_plot_pos=[]

    def add_order(self, order):
        will_add = True
        for o in self.orders:
            if o.type == 'buy':
                will_add = False
        if will_add:
            self.orders.append(order)
            self.blance -= order.amount
            self.cur_plot_pos.append(order.place_time)
            print('已成交', self.blance)

    def deal_order(self, price,time):
        for o in self.orders:
            if o.state == '未成交':
                if o.type == 'buy' and price < o.limit_price:
                    o.state = '已成交'
            if o.state == '已成交':
                if price < o.stop_lose_price or price > o.stop_win_price:
                    rate = (price - o.limit_price) / o.limit_price * 100
                    self.blance += (o.amount * (1 + rate * o.margin_level / 100))
                    del self.orders[0]
                    self.cur_plot_pos.append(time)
                    self.plots.append(self.cur_plot_pos)
                    self.cur_plot_pos=[]
                    print('结束订单', self.blance)
