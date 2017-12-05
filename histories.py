import random
import matplotlib.pyplot as plt
import funcs

def uniform_ideal(count):
    return [random.uniform(5.0, 10.0) for _ in range(count)]

def uniform_fuckup(count):
    return [-1. * random.uniform(5.0, 10.0) for _ in range(count)]

def uniform_ideal_restored(ideal_count=100, fuckup_count=50, restore_count=500):
    return uniform_ideal(ideal_count) + uniform_fuckup(fuckup_count) + uniform_ideal(restore_count)

def uniform_oscillate(count):
    return [random.uniform(5.0, 10.0) if x % 2 else -1 * random.uniform(5.0, 10.0) for x in range(count)]

class Deal:
    price = .0
    is_ok = False
    def __init__(self, ok=True, price=100.0):
        self.price = price
        self.is_ok = ok

class Deals:
    items = list()
    oks = 0
    fucks = 0

    def __init__(self, how_many_counts=100, fuckup_level=0.05, price_lo=5.0, price_hi=10.0):
        for x in range(how_many_counts):
            self.items.append(Deal(random.uniform(0, 1) > fuckup_level, random.uniform(price_lo, price_hi)))
        self.oks = len([x for x in self.items if x.is_ok])
        self.fucks = len(self.items) - self.oks

    def __plot_reputation(self, history, func):
        y_axis = [func(history[:x], memory=0.99) for x in range(len(history))]
        x_axis = [x for x in range(len(history))]
        # y_axis = list()
        # for x in range(len(history)):
        #     s = history[:x]
        #     f = func(s, memory=0.99)
        #     y_axis.append(f)

        plt.plot(x_axis, y_axis, 'ro',
                 label='Rating(Q)',
                 linewidth=2,
                 linestyle='dashed',
                 marker='o',
                 markersize=2,
                 markerfacecolor='blue')
        plt.ylabel('$f(x)$')
        plt.xlabel('$Q$')
        plt.title(u"Dependence f(x) on the moment in the history of deals")
        plt.legend()

        # ax = plt.gca()
        # # recompute the ax.dataLim
        # ax.relim()
        # # update ax.viewLim using the new dataLim
        # ax.autoscale_view()
        plt.show()

    def plot(self):
        history = uniform_ideal_restored(
            ideal_count=self.oks,
            fuckup_count=self.fucks,
            restore_count=0)
        self.__plot_reputation(history, funcs.baseline)

    """ For web visualization"""

    def fucks_generator(self):
        """A generator for fucks numbers"""

    def oks_generator(self):
        """A generator for oks numbers"""

