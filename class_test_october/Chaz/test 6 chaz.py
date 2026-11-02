#6
user=(input('enter either the day , weather or date'))
if user=='weather':
    weather=(input('good choice is it sunny or rainy'))
    if weather=='sunny':
        print('it is a happy day')
        if weather=='rainy':
            print('it is a sad day')
elif user=='day':
    day=(input('what day of the week is it'))
    if day=='sunday' or day=='saturday':
        print('it is a happy day')
elif user=='date':
    date=int(input('what date of the month is it'))
    if date%2==0:
        print('it is a happy day')
else:
    print('it is a sad day')
        