def contador(num):
    num -= 1
    if num > 0:
        print(num)
        contador(num)
    else:
        print("BOOMMMMM !!!")
   

contador(11)
