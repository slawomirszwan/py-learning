# print(str(5))


def sprawdzPesel(pesel):
    # if not isinstance(pesel, str):
    #     return False

    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    # print(pesel,list(pesel[0:10]),wagi)
    # a= dict(zip(wagi, list(pesel[0:9])))
    # print(a)

    # for x,y in zip(wagi, ])

    # print(pesel[:-1])

    print(list(zip(wagi, pesel[:-1])))

    sum=0
    for w,v in zip(wagi, pesel[:-1]):
        print( (w*int(v))%10)
        sum += (w*int(v))%10


    x= (int(pesel[10]) == (100000 - sum(x * int(y) for x, y in zip(wagi, pesel))) % 10)

    return True

sprawdzPesel('02070803628')
