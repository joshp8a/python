try:
    grade = float(raw_input('Enter score: '))

    if grade < 0.0 or grade > 1.0:
        print 'Bad score'
    elif grade >= 0.9:
        print 'A'
    elif grade >= 0.8:
        print 'B'
    elif grade >= 0.7:
        print 'C'
    elif grade >= 0.6:
        print 'D'
    elif grade < 0.6:
        print 'F'    
except:
    print 'Bad score'