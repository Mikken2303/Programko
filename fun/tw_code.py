num = "0"
n = str(int(num,8))
l1 = ["I","He","She","They","Mike","John","Kelly","Bob"]
b = " just came "
l2 = ["Home","to the store","from the store","from the vacation","from Daves","to say hello","across the secret"]
enc = l1[int(n[0])] + b + l2[int(n[1])]
print(enc)