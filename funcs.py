import math


import numpy


def get_reputation(history, memory=0.9, weight=0.4):
    h_len = len(history)

    if h_len < 1:
        return 0.5

    pos = 0.
    neg = 0.

    for idx in range(h_len):
        if history[idx] > 0:
            pos += history[idx] * math.pow(memory, h_len - idx)
        else:
            neg += math.fabs(history[idx]) * math.pow(memory, h_len - idx)

    stabilizer = numpy.mean(history)

    return (weight * pos + stabilizer) / ((weight * pos) + neg + 2 * stabilizer)


def get_max_deal_price(reputation, history, market_mu=100.0, trusted_history=5):
    if len(history) < trusted_history:
        return reputation * market_mu

    return reputation * sum(history)


def can_make_deal(price, history, market_mean_price):
    if len(history) == 0:
        mean = market_mean_price
        #стандартизированный коэффциент beta
        std = mean * 1.25
    else:
        mean = numpy.mean(history)
        std = numpy.std(history)
        if std == 0:
            std = mean * 1.25

    lower = mean - 2 * std
    upper = mean + 2 * std
    print("upper: ", upper, "lower: ", lower, "std: ", std, "mean: ", mean)
    print(price)
    return lower <= price <= upper


def get_proposed_price(mu, std):
    price = numpy.random.normal(mu, std, 1)

    if price[0] < 0:
        return 1.

    return price[0]
