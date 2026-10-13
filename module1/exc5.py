with open("notes.txt", "w", encoding= "utf-8") as f:
    f.write("One\ntwo\nthree\njs\ntrfg")
with open("notes.txt","r", encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines))