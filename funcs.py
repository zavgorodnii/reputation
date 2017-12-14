import math

import numpy


def get_reputation(history, memory=0.9, weight=0.3):
    if not history:
        return 0.5
    h_len = len(history)
    pos = .0
    neg = .0
    idx = 0

    for item in history:
        if item > 0:
            pos += item * math.pow(memory, h_len - idx)
        else:
            neg += math.fabs(item) * math.pow(memory, h_len - idx)
        idx += 1

    stabilizer = numpy.mean(history)
    return (weight * pos + stabilizer) / ((weight * pos) + neg + 2. + stabilizer)


def get_max_deal_price(reputation, history, market_mu=100.0, trusted_history=5):
    if len(history) < trusted_history:
        return reputation * market_mu
    return reputation * sum(history)


# цены на рынке
def get_proposed_price(mu, std):
    price = numpy.random.normal(mu, std, 1)
    if price[0] < 0:
        return 1.
    return price[0]
