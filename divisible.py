# 7) WAP TO PRINT 'FIZZ' IF THE GIVEN NUMBER DIVISIBLE BY 3 OR PRINT 'BUZZ' IF THE GIVEN NUMBER DIVISIBLE BY 5 OR PRINT 'FIZZ BUZZ' IF THE GIVEN NUMBER DIVISIBLE BY BOTH 3 AND 5 PRINT ELSE PRINT THE NUMBER AS IT IS.
num=int(input('enter the number: '))
if num%3==0 and num%5==0:
    print("FIZZ BUZZ")

elif num%3==0:
    print("FIZZ")
elif num%5==0:
    print("BUZZ")

else:
    print(num)
#output: enter the number: 15
#FIZZ BUZZ
