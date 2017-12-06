# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import funcs
import histories


def plot_reputation(history, reputation_func):
    y_axis = [reputation_func(history[:x], memory=0.99) for x in xrange(len(history))]
    x_axis = [x for x in xrange(len(history))]

    plt.plot(x_axis, y_axis, 'ro')

    ax = plt.gca()
    # recompute the ax.dataLim
    ax.relim()
    # update ax.viewLim using the new dataLim
    ax.autoscale_view()

    plt.show()


def plot_max_deal_cost(num_tries, reputation_func, max_price_func):
    history = []
    y_axis = []
    for x in xrange(num_tries):
        rep = reputation_func(history[:x], memory=0.99)
        price = funcs.propose_deal()
        max_price = max_price_func(rep, history[:x])
        y_axis.append(max_price)

        print("rep:", rep, "max price:", max_price, "proposed price:", price)

        if price <= max_price:
            history.append(price)

    # x_axis = [x for x in xrange(num_tries)]
    #
    # plt.plot(x_axis, y_axis, 'ro')
    #
    # ax = plt.gca()
    # # recompute the ax.dataLim
    # ax.relim()
    # # update ax.viewLim using the new dataLim
    # ax.autoscale_view()
    #
    # plt.show()


def main():
    # plot_reputation(histories.uniform_ideal(100), funcs.baseline)
    # plot_max_deal_cost(200, funcs.get_reputation, funcs.get_max_deal_price)

    plot_reputation(histories.uniform_ideal_restored(), funcs.get_reputation)
    # plot_reputation(histories.uniform_ideal_restored(ideal_count=30, fuckup_count=6, restore_count=30), funcs.baseline)
    # plot_reputation(histories.uniform_ideal(100) + histories.uniform_oscillate(100), funcs.reputation)




if __name__ == "__main__":
    main()
