def all_variants(text):
    for s in range(len(text)):
        for p in range(len(text) - s):
            yield text[p:p + s + 1]


a = all_variants("abc")
for i in a:
    print(i)
