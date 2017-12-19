import matplotlib.pyplot as plt

import funcs
import numpy
import histories


def plot_reputation(history, reputation_func):
    y_axis = [reputation_func(history[:x], memory=0.99) for x in range(len(history))]
    x_axis = [x for x in range(len(history))]

    plt.plot(x_axis, y_axis, '.', color="#000000")
    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()

    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip(x_axis, y_axis)]))


def plot_fraud(history, reputation_func):
    history_without_outliers = []
    market_mean_price = numpy.mean(history)
    market_mu = 100.
    market_std = 49.
    accumulation_period = market_mu - 2 * market_std

    for x in range(len(history)):
        if len(history_without_outliers) < numpy.fabs(accumulation_period):
            cas = int(numpy.fabs(accumulation_period))
            print("cas: ", cas)
            print("history without outliers:", history_without_outliers)
            hist = history[:cas]
        else:
            hist = history_without_outliers[:cas]

        if reputation_func(numpy.fabs(history[x]), hist, market_mean_price):
            history_without_outliers.append(history[x])
            print("MMP :", market_mean_price)
        else:
            print(x)
            history_without_outliers.append(history_without_outliers[-1])
            #возвращает последний элемент
    y_axis = [funcs.get_reputation(history_without_outliers[:x], memory=0.99)
              for x in range(len(history_without_outliers))]
    x_axis = [x for x in range(len(history_without_outliers))]
    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip(x_axis, y_axis)]))
    plt.plot(x_axis, y_axis, label='Fraud(price)', color="#000000")
    plt.ylabel('$Reputation$')
    plt.xlabel('$Deals$')
    plt.show()


def plot_max_price(reputation_func, max_price_func, num_tries=100):
    market_mu = 100.
    market_std = 50.

    history, max_price_history, reps = [], [], []
    for x in range(num_tries):
        reputation = reputation_func(history[:x], memory=0.99)
        max_price = max_price_func(reputation, history, market_mu=market_mu)
        proposed_price = funcs.get_proposed_price(market_mu, market_std)

        if proposed_price <= max_price:
            print("rep:", reputation, "max_price", max_price, "proposed_price", proposed_price, "<--", len(max_price_history), "---", sum(history))
            max_price_history.append(max_price)
            history.append(proposed_price)
            reps.append(reputation)

    x_axis = [x for x in range(len(max_price_history))]

    plt.plot(x_axis, max_price_history, '.', color="#000000")

    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip(x_axis, max_price_history)]))

    print("\n\n\n\n")

    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip([i for i in range(len(reps))], reps)]))

    print(">>>>>>>>>>>>", numpy.mean(history), sum(history))

    ax = plt.gca()
    ax.relim()
    ax.autoscale_view()

    plt.show()


def main():
    # plot_reputation(histories.uniform_ideal(120), funcs.get_reputation)

    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    #
    # # Plot reputation build-up, then [1..6] conflicts.
    # for x in range(1, 7):
    #     plot_reputation(histories.uniform_ideal_restored(ideal_count=80, fuckup_count=x, restore_count=26), funcs.get_reputation)
    #     print("\n")
    plot_fraud(histories.uniform_ideal(120) + histories.uniform_with_conflicts(120, each=15), funcs.can_make_deal)
    # plot_reputation(histories.uniform_ideal(80) + histories.uniform_with_conflicts(40, each=10), funcs.get_reputation)
    # plot_reputation(histories.uniform_with_conflicts(120, each=10), funcs.get_reputation)

    # plot_max_price(funcs.get_reputation, funcs.get_max_deal_price)


if __name__ == "__main__":
    main()
