words_len: list = list(map(lambda x: len(x), input().split()))
rating: dict = {}

for wl in words_len:
    rating[wl] = rating.get(wl, 0) + 1

for key, value in sorted(rating.items()):
    print(str(key) + ':', value)
