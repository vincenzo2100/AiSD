def foo(wyraz):
    dl = len(wyraz)
    x = dl-1
    i = 0
    while i < x:
        if wyraz[i] == wyraz[x]:
            i = i + 1
            x = x-1
            print("1")
            break
        else:
            print("0")
            break
foo("tabat")