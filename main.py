# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import funcs
import numpy
import histories


def plot_reputation(history, reputation_func):
    y_axis = [reputation_func(history[:x], memory=0.99) for x in xrange(len(history))]
    x_axis = [x for x in xrange(len(history))]

    plt.plot(x_axis, y_axis, '.', color="#000000")

    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()

    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip(x_axis, y_axis)]))

    # plt.show()


def plot_max_price(reputation_func, max_price_func, num_tries=100):
    market_mu = 100.
    market_std = 50.

    history, max_price_history, reps = [], [], []
    for x in xrange(num_tries):
        reputation = reputation_func(history[:x], memory=0.99)
        max_price = max_price_func(reputation, history, market_mu=market_mu)
        proposed_price = funcs.get_proposed_price(market_mu, market_std)

        if proposed_price <= max_price:
            print("rep:", reputation, "max_price", max_price, "proposed_price", proposed_price, "<--", len(max_price_history), "---", sum(history))
            max_price_history.append(max_price)
            history.append(proposed_price)
            reps.append(reputation)

    x_axis = [x for x in xrange(len(max_price_history))]

    plt.plot(x_axis, max_price_history, '.', color="#000000")

    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip(x_axis, max_price_history)]))

    print("\n\n\n\n")

    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip([i for i in xrange(len(reps))], reps)]))

    print(">>>>>>>>>>>>", numpy.mean(history), sum(history))

    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()

    plt.show()


def main():
    # plot_reputation(histories.uniform_ideal(30), funcs.get_reputation)

    # # Plot reputation build-up, then [1..6] conflicts.
    # for x in range(1, 7):
    #     plot_reputation(histories.uniform_ideal_restored(ideal_count=80, fuckup_count=x, restore_count=30), funcs.get_reputation)
    #     print("\n")
    plot_reputation(histories.uniform_ideal(80) + histories.uniform_with_conflicts(40, each=5), funcs.get_reputation)
    # plot_reputation(histories.uniform_with_conflicts(120, each=5), funcs.get_reputation)

    # plot_max_price(funcs.get_reputation, funcs.get_max_deal_price)


if __name__ == "__main__":
    main()
