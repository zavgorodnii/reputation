import numpy
import matplotlib.pyplot as plt
import histories
import funcs


def can_make_deal(price, history, market_mean_price):
    # возвращает ценник между mu+2sigma <= X <= mu-2sigma
    if len(history) == 0:
        mean = market_mean_price
        #стандартизированный коэффциент beta
        std = mean * 1.41
    else:
        mean = numpy.mean(history)
        std = numpy.std(history)
        if std == 0:
            std = mean * 1.41

    lower = mean - 2 * std
    upper = mean + 2 * std
    return lower <= price <= upper


def main():

    # fig 2
    # history = histories.uniform_prices(120) + histories.uniform_fuckup(10) +
    # histories.uniform_with_conflicts(32, each=10)
    history = histories.uniform_with_conflicts(120, 15)
    history_without_outliers = []
    market_mean_price = numpy.mean(history)

    for x in range(len(history)):
        if len(history_without_outliers) < 3:
            print("history without outliers:", history_without_outliers)
            hist = history[:3]
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
    print(" ".join(["(%0.3f, %0.3f)" % x for x in zip(x_axis, y_axis)]))
    plt.plot(x_axis, y_axis, label='Fraud(price)',  color="#000000")
    plt.ylabel('$Reputation$')
    plt.xlabel('$Deals$')
    plt.show()

if __name__ == "__main__":
    main()
