# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

import funcs
import histories


def plot_reputation(history, func):
    y_axis = [func(history[:x], memory=0.99) for x in xrange(len(history))]
    x_axis = [x for x in xrange(len(history))]

    plt.plot(x_axis, y_axis, 'ro')

    ax = plt.gca()
    # recompute the ax.dataLim
    ax.relim()
    # update ax.viewLim using the new dataLim
    ax.autoscale_view()

    plt.show()


def main():
    # plot_reputation(histories.uniform_ideal(100), funcs.baseline)
    # plot_reputation(histories.uniform_ideal_restored(), funcs.baseline)
    # plot_reputation(histories.uniform_ideal_restored(ideal_count=30, fuckup_count=6, restore_count=30), funcs.baseline)
    plot_reputation(histories.uniform_ideal(100) + histories.uniform_oscillate(100), funcs.baseline)


if __name__ == "__main__":
    main()
