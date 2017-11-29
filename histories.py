# -*- coding: utf-8 -*-

import random


def uniform_ideal(count):
    return [random.uniform(5.0, 10.0) for _ in range(count)]


def uniform_fuckup(count):
    return [-1. * random.uniform(5.0, 10.0) for _ in range(count)]


def uniform_ideal_restored(ideal_count=100, fuckup_count=50, restore_count=500):
    return uniform_ideal(ideal_count) + uniform_fuckup(fuckup_count) + uniform_ideal(restore_count)


def uniform_oscillate(count):
    return [random.uniform(5.0, 10.0) if x % 2 else -1 * random.uniform(5.0, 10.0) for x in range(count)]
