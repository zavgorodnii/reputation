import histories

def main():
    s1 = histories.Deals(500)
    s2 = histories.Deals(500, 0.1, 100, 0)
    s3 = histories.Deals(500, 0.05, 5, 100)
    s4 = histories.Deals(1000, 0.1)

    qq = histories.Deals()
    qq = qq.fuck(10).ok(13).fuck(5).ok(52).fuck(10).fuck(10)
    print(len(histories.Deals.fuckrow))
    qq.plot()

if __name__ == "__main__":
    main()
