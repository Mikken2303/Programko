def sm(vstup):
    platidla, out = [500,200,100,50,20,10,5,2,1],[]
    for i in platidla:
        out.append(vstup//i)
        vstup = vstup % i
    return out
print(sm(864))
