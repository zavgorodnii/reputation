# -*- coding: utf-8 -*-

import math


import numpy


def get_reputation(history, memory=0.9):
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

    return (pos + 1.0) / (pos + neg + 5.)


def get_max_deal_price(reputation, history, start_mu=2.):
    if len(history) < 1:
        return reputation * start_mu

    return reputation * numpy.mean(history) + 0.2 * numpy.mean(history)


def propose_deal():
    price = numpy.random.normal(15, 30, 1)

    if price[0] < 0:
        return 5.

    return price[0]
