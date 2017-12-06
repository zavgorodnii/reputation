import histories

def main():
    s1 = histories.Deals(500)
    s2 = histories.Deals(500, 0.1, 100, 0)
    s3 = histories.Deals(500, 0.05, 5, 100)
    s4 = histories.Deals(1000, 0.1)


    qq = histories.Deals()
    # ебашим сценарии здесь
    qq.ok(10).fuck(5).ok(3).ok(10).fuck(3).ok(100).fuck(15).ok(200).fuck(20).ok(30).ok(100)
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