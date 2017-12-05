import histories

def main():
    s1 = histories.Deals(500)
    s2 = histories.Deals(500, 0.1, 100, 0)
    s3 = histories.Deals(500, 0.05, 5, 100)
    s4 = histories.Deals(500, 0.2, 100, 0)
    s4.plot()

if __name__ == "__main__":
    main()
