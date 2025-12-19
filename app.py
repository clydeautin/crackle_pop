def cracklePop():
    i = 1

    while i <= 100:
        if (i % 3 == 0) and (i % 5 == 0):
            print('CracklePop')
        elif i % 3 == 0:
            print('Crackle')
        elif i % 5 == 0:
            print('Pop')
        else:
            print(i)
        i += 1
        
cracklePop()