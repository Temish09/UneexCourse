s = input()
pat = input()

Found = False
for i in range(len(s)-len(pat)+1):
    Found = True
    for j, ch_pat in enumerate(pat):
        if ch_pat != '@' and ch_pat != s[i+j]:
            Found = False
            break
    if Found:
        print(i)
        break
if not Found:
    print(-1)