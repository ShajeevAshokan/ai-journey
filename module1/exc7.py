counts = {}
with open("sample.txt","w",encoding="utf-8")as f:
    f.write("A function is a naming word which help other word as a function also a function.")
with open("sample.txt", "r",encoding="utf-8")as f:
    for line in f:
        for word in line.lower().split():
            word = word.strip(".,!?:;'\"")
            if word:
                counts[word] = counts.get(word,0) + 1

def by_count(item):
    return item[1]

top3 = sorted(counts.items(),key=by_count,reverse=True)[:3]
for word,n in top3:
    print(word,n) 

