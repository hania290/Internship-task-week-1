while True:
    print ('for lenght option 1')
    print ('for weight option 2')
    print ('for temperature option 3')
    choice=input('choose')

    if choice=='1':
   
        print('1: meter to feet')
        print ('2: feet to meter')
        choose=input('choose')
        value=float(input('give some number '))


        if choose=='1': 
            answer = value*3.28084
            print(answer)

        elif choose=='2':
            answer = value/3.28084
            print(answer)

        else:
            print ('invalid option')

   
    elif choice=='2':
  
        print('1: kilogram to pound')
        print('2: pound to kilogram')
        choose=input('choose')
        value=float(input('enter value. '))

        if choose=='1':
            answer = value*2.20462
            print(answer)

        elif  choose=='2':
            answer = value/2.20462
            print(answer)

        else:
            print('invalid option ')


    elif choice=='3':

        print('1: celcius to farenheit')
        print('2:farenheit to celcius')
        choose=input('choose')
        value=float(input('enter value. '))

        if choose=='1':
            answer = (value*9/5)+32
            print(answer)

        elif choose=='2':
            answer = (value-32)*5/9
            print(answer)

        else:
            print('invalid option. ')

    else:
            print('invalid option choose again')

