import numpy
import matplotlib.pyplot as plt
import histories
import funcs


def can_make_deal(price, history, market_mean_price):
    # возвращает ценник между mu+2sigma <= X <= mu-2sigma
    if len(history) == 0:
        mean = market_mean_price
        std = mean * 1.41
    else:
        mean = numpy.mean(history)
        std = numpy.std(history)
        if std == 0:
            std = mean * 1.41

    lower = mean - 2 * std
    upper = mean + 2 * std
    return lower < price < upper


def main():
    history = histories.uniform_prices(120) + histories.uniform_with_conflicts(20, each=3)
    # history = histories.uniform_prices(120) + histories.uniform_fuckup(30)
    history_without_outliers = []
    market_mean_price = numpy.mean(history)

    for x in range(len(history)):
        if len(history_without_outliers) < 12:
            print("history without outliers:", history_without_outliers)
            hist = history[:12]
        else:
            hist = history_without_outliers[:x]

        if can_make_deal(numpy.fabs(history[x]), hist, market_mean_price):
            history_without_outliers.append(history[x])
        else:
            print(x)
            history_without_outliers.append(history_without_outliers[-1])

    y_axis = [funcs.get_reputation(history_without_outliers[:x], memory=0.99)
              for x in range(len(history_without_outliers))]
    x_axis = [x for x in range(len(history_without_outliers))]

    plt.plot(x_axis, y_axis, 'ro',
             label='Rating(Q)',
             linewidth=2,
             linestyle='dashed',
             marker='o',
             markersize=2,
             markerfacecolor='blue')
    plt.ylabel('$Fraud (price)$')
    plt.xlabel('$Q$')
    plt.title(u"Dependence f(x) on the moment in the history of deals")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
