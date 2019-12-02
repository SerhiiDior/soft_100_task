words = input().split()
word = sorted(set(words))

for i in word:
    print("{}:{}".format(i,words.count(i)))
