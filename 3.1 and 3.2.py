
hrs = raw_input('Hours? ')
pay = raw_input('Rate? ')

try:
    iHrs = int(hrs)
except:
    print 'ERROR, please enter a numeric input'
    sys.exit()
    
try:
    fPay = float(pay)
except:
    print 'ERROR, please enter a numeric input'
    sys.exit()
    
if iHrs > 40:
    print 'Pay is', ((iHrs-40)*fPay*1.5)+(fPay*40)
else:
    print 'Pay is', iHrs*fPay