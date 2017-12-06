# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import funcs
import histories


def plot_reputation(history, reputation_func):
    y_axis = [reputation_func(history[:x], memory=0.99) for x in xrange(len(history))]
    x_axis = [x for x in xrange(len(history))]

    plt.plot(x_axis, y_axis, 'ro')

    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()

    plt.show()


def plot_max_price(reputation_func, max_price_func, num_tries=500):
    market_mu = 100.
    market_std = 50.

    y_axis, history = [], []
    for x in xrange(num_tries):
        reputation = reputation_func(history[:x], memory=0.99)
        max_price = max_price_func(reputation, history, market_mu=market_mu)
        proposed_price = funcs.get_proposed_price(market_mu, market_std)

        print("rep:", reputation, "max_price", max_price, "proposed_price", proposed_price, "<--", len(history))

        y_axis.append(max_price)

        if proposed_price <= max_price:
            history.append(proposed_price)

    x_axis = [x for x in xrange(num_tries)]

    plt.plot(x_axis, y_axis, 'ro')

    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()

    plt.show()


def main():
    # plot_reputation(histories.uniform_ideal(100), funcs.get_reputation)
    # plot_max_deal_cost(200, funcs.get_reputation, funcs.get_max_deal_price)

    # plot_reputation(histories.uniform_ideal_restored(), funcs.get_reputation)
    # plot_reputation(histories.uniform_ideal_restored(ideal_count=30, fuckup_count=6, restore_count=30), funcs.get_reputation)
    # plot_reputation(histories.uniform_ideal(100) + histories.uniform_oscillate(100), funcs.get_reputation)

    plot_max_price(funcs.get_reputation, funcs.get_max_deal_price)




if __name__ == "__main__":
    main()
