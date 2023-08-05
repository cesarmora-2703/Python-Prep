def es_primo(num):
    if num < 2:
        return False
    for i in range(2,num):
        print("num, i, modulo:", num, "--", i, "--", str(num%i))
        if num%i == 0:
            return False
    return True

for num in range(0, 31):
    if(es_primo(num)):
        print(num)