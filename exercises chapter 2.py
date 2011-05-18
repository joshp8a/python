
2.2
name = raw_input("Enter your name: ")
print "Hi " + name + ", welcome!"

RUN
Enter your name: Josh
Hi Josh, welcome!

2.3

A
hrs = raw_input('Hours? ')
pay = raw_input('Rate? ')
iHrs = int(hrs)
fPay = float(pay)
print 'Pay is', iHrs*fPay

RUN
Hours? 35
Rate? 2.75
Pay is 96.25

B
hrs = raw_input('Hours? ')
pay = raw_input('Rate? ')
iHrs = int(hrs)
fPay = float(pay)
print 'Pay is', round(iHrs*fPay,2);

RUN
Hours? 10
Rate? 1.11111
Pay is 11.11

2.4
width = 17
height = 12.0

1 - width/2 = 8 and type int
2 - width/2.5 = 8.5 and type float
3 - height/3 = 4.0 and type float
4 - 1+2*5 = 11 and type int

2.5
cel = raw_input("Temp. in Celsius? ")
print "Fahrenheit: ", (9/5)*float(cel)+32

RUN
Temp. in Celsius? 0
Fahrenheit:  32.0
