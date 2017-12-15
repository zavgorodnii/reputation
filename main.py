import numpy
import matplotlib.pyplot as plt
import histories
import funcs


def can_make_deal(price, history, market_mean_price):
    # возвращает ценник между mu+2sigma <= X <= mu-2sigma
    if len(history) == 0:
        mean = market_mean_price
        #стандартизированный коэффциент beta
        std = mean * 1.25
    else:
        mean = numpy.mean(history)
        std = numpy.std(history)
        if std == 0:
            std = mean * 1.25
    #         1.41

    lower = mean - 2 * std
    upper = mean + 2 * std
    print("upper: ", upper, "lower: ", lower, "std: ", std, "mean: ", mean)
    print(price)
    return lower <= price <= upper


def main():
    history = histories.uniform_prices(10) + histories.uniform_with_conflicts(120, 15)
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

        if can_make_deal(numpy.fabs(history[x]), hist, market_mean_price):
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
    plt.plot(x_axis, y_axis, label='Fraud(price)',  color="#000000")
    plt.ylabel('$Reputation$')
    plt.xlabel('$Deals$')
    plt.show()

if __name__ == "__main__":
    main()
