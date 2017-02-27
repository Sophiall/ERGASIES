def moveZeros(zArray):
    intArray = []
    zerArray = []
    for integer in zArray:
        if integer != 0:
            intArray.append(integer)
        else:
            zerArray.append(integer)
    for zer in zerArray:
        intArray.append(0)
    return intArray


if __name__ == '__main__':

    print "Enter number and then press 'Enter',to move the zeros at the end press 'Enter' two times\n"

    list = []
    x = True
    while x:
        try:
            z = float(raw_input())
            list.append(z)
        except ValueError:
            x = False

    List = moveZeros(list)
    print List


