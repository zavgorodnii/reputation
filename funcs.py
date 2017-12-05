import math

def baseline(history, memory=0.9):
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
    return (pos + 1.0) / (pos + neg + 5.)

    # for idx in range(h_len):
    #     if history[idx] > 0:
    #         pos += history[idx] * math.pow(memory, h_len - idx)
    #     else:
    #         neg += math.fabs(history[idx]) * math.pow(memory, h_len - idx)
    # return (pos + 1.0) / (pos + neg + 5.)
