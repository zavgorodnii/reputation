import random
# import matplotlib.pyplot as plt
# import funcs
# import numpy


def uniform_price(minimum=5, maximum=10):
    # предложенная сделка
    # return 42.0
    return random.uniform(minimum, maximum)


def uniform_prices(count):
    return [uniform_price() for _ in range(count)]


def uniform_fuckup(count):
    return [-1. * uniform_price() for _ in range(count)]


def uniform_ideal_restored(ideal_count=100, fuckup_count=50, restore_count=500):
    return uniform_prices(ideal_count) + uniform_fuckup(fuckup_count) + uniform_prices(restore_count)


def uniform_oscillate(count):
    return [uniform_price() if x % 2 else -1 * uniform_price() for x in range(count)]


def uniform_with_conflicts(count, each=3):
    return [uniform_price() if x < 2 or x % each else -1 * uniform_price() for x in range(count)]


# class Deal:
#     price = .0
#     is_ok = False
#     buyer = None
#     supplier = None
#
#     def __init__(self, is_ok=True, price=100.0, buyer=None, supplier=None):
#         self.price = price
#         self.is_ok = is_ok
#         self.buyer = buyer
#         self.supplier = supplier


# class Deals:
#     deals = []
#     history_prices = 0
#     reputation = 0.5
#
#     fuckup_level = 5
#     price_low = 0
#     price_high = 0
#
#     row, fuck_row = list(), list()
#     history, well_deals = [], []
#     oks = 0
#     fucks = 0
#
#     def __init__(self, reputation_func, deals=None, fuckup_level=5, price_low=1, price_high=5):
#         self.deals = deals
#
#         prices = []
#         for deal in deals:
#             prices.append(deal.price)
#             if self.can_make_deal(deal.price, prices):
#                 self.history_prices += deal.price
#
#         self.reputation = reputation_func(prices)

        # # reputation = reputation_func(self.history[:x], memory=0.99)
        # if self.can_make_deal(proposed_price, self.row):
        #     # если цена сделки входит в доверительный интервал, то добавляем цену сделки и повышаем рейтинг
        #     # иначе - пропускаем ход
        #     proposed_price = funcs.get_proposed_price(market_mu, market_std)
        #     self.history.append(proposed_price)
        #     deals.append(Deal(reputation))
        #     deals.append(Deal(self.propose_deal_price(), self.ok(10)))
        #     # self.items.append(Deal(random.uniform(0, 1) > fuckup_level, random.uniform(price_lo, price_hi)))

        # self.oks = len([x for x in deals if x.is_ok])
        # self.fucks = len(deals) - self.oks

        # saving items values for plotting
        # self.deals_for_plot = deals

    # def get_fraud_expectancy(self, price):
    #     # ожидает мошенничества
    #     if (self.reputation * self.history_prices) == 0:
    #         return 0
    #     return price / (self.reputation * self.history_prices)

    # def can_make_deal(self, price, history):
    #     # возвращает ценник между mu+2sigma <= X <= mu-2sigma
    #     mu = numpy.mean(history)
    #     std = numpy.std(history)
    #
    #     print('history:', history)
    #     print('mean:', mu)
    #     print('std:', std)
    #
    #     lower = self.get_fraud_expectancy(mu - 2 * std)
    #     upper = self.get_fraud_expectancy(mu + 2 * std)
    #     print("lower: ", lower)
    #     print("fraud: ", self.get_fraud_expectancy(price))
    #     print("upper: ", upper)
    #
    #     return lower < self.get_fraud_expectancy(price) < upper

    # def __plot_reputation(self, history, reputation_func):
    #     y_axis = [reputation_func(history[:x], memory=0.99) for x in range(len(history))]
    #     x_axis = [x for x in range(len(history))]
    #
    #     plt.plot(x_axis, y_axis, 'ro',
    #              label='Rating(Q)',
    #              linewidth=2,
    #              linestyle='dashed',
    #              marker='o',
    #              markersize=2,
    #              markerfacecolor='blue')
    #     plt.ylabel('$f(x)$')
    #     plt.xlabel('$Q$')
    #     plt.title(u"Dependence f(x) on the moment in the history of deals")
    #     plt.legend()
    #     plt.show()

    # def ok(self, n=1):
    #     self.row.extend(uniform_prices(n))
    #     return self
    #
    # def fuck(self, n=1):
    #     self.fuck_row.extend(uniform_fuckup(n))
    #     self.row.extend(uniform_fuckup(n))
    #     return self
    #
    # def plot(self):
    #     # self.__plot_reputation(self.row, funcs.get_reputation)
    #     self.__plot_reputation(funcs.get_reputation, funcs.get_proposed_price)

# # isFuckedUp returns value of fraud of this customer for proposed order
# # address - customer ethereum address
# # order - mapping of systemIn `order` params
# def isFuckedUp(address, order):
#     deals = get_deals(address)
#     return calculate_fraud(deals, order)
#
#
# def get_deals(address):
#     return []
#
#
# def calculate_fraud(deals, order):
#     fraud_rate = 0
#     return fraud_rate
