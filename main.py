import histories
from collections import Counter

def main():
    s1 = histories.Deals(500)
    s2 = histories.Deals(500, 0.1, 100, 0)
    s3 = histories.Deals(500, 0.05, 5, 100)
    s4 = histories.Deals(1000, 0.1)

    qq = histories.Deals()
    # ебашим сценарии здесь

    cur = qq = qq.fuck(10).ok(13).fuck(5).ok(52).fuck(10)
    # если число вызовов факов превышает какое-то значение, то график меняет цвет (на это моменте происходит бан)
    # как посчитать вызовв функции и значения аргументов в них??
    qq.plot()
    # for x in range(1000):
    #     if x % 1:
    #         qq.ok(10)
    #     else:
    #         qq.fuck(2)
if __name__ == "__main__":
    main()


'''
Main scenarious:
 1) first fuckup
 2) second fuckup
 3) use beta - dictribution
 4) depend on time 
 '''