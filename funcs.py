# -*- coding: utf-8 -*-

import math


def baseline(history, memory=0.9):
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
