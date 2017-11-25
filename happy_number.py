#check happy number

def happy_number(number):

    old_number = number
    visited = set()
    while True:
        if number == 1:
            print(old_number,'is a happy number. ')
            break
        else:
            number = sum( int(c)**2 for c in str(number))
            if number in visited:
                print(old_number,'is sad number. ')
                break
            visited.add(number)

happy_number(10)