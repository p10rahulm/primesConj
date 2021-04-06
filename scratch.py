import numpy as np


def maxPayout(payouts, cooldown):
    n = len(payouts)
    payouts = payouts
    cooldown = cooldown
    opt = np.zeros([n, n])
    print(opt)
    for t in range(n):
        for j in range(n):
            if j == n - 1 - t:
                opt[j][t] = payouts[n - 1 - j]
                # print("j=%d,t=%d,opt[j][t]=%d" % (j, t, opt[j][t]))
                # print(opt)
            elif j > n - 1 - t:
                opt[j][t] = max(opt[j - 1][t], payouts[n - 1 - j] + opt[j -1- cooldown[n - 1 - j]][t])
                # print("j=%d,t=%d,opt[j-1][t]=%d,opt[j][t]=%d,payouts[n-1-j]=%d,cooldown[n-1-j]=%d,"
                #     "j -1- cooldown[n-1-j] = %d,opt[j -1- cooldown[n - 1 - j]][t]=%d" % (
                #         j, t, opt[j - 1][t], opt[j][t], payouts[n - 1 - j], cooldown[n - 1 - j],
                #         j -1- cooldown[n - 1 - j], opt[j -1- cooldown[n - 1 - j]][t]))
    print(opt)


payouts = [2, 1, 4, 9, 6]
cooldown = [1, 0, 1, 2, 3]
maxPayout(payouts, cooldown)
