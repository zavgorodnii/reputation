# -*- coding: utf-8 -*-

import math


import numpy


def get_reputation(history, memory=0.9, weight=0.07):
    h_len = len(history)

    if h_len < 1:
        return 0.5

    pos = 0.
    neg = 0.

    for idx in xrange(h_len):
        if history[idx] > 0:
            pos += history[idx] * math.pow(memory, h_len - idx)
        else:
            neg += math.fabs(history[idx]) * math.pow(memory, h_len - idx)

    stabilizer = numpy.mean(history)

    return (weight * pos + stabilizer) / (weight * (pos + neg) + 2 * stabilizer)


def get_max_deal_price(reputation, history, market_mu=100.0, trusted_history=5):
    if len(history) < trusted_history:
        return reputation * market_mu

    return reputation * sum(history)


def get_proposed_price(mu, std):
    price = numpy.random.normal(mu, std, 1)

    if price[0] < 0:
        return 1.

    return price[0]
