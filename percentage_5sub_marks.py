# 9) WAP TO CONSOLIDATE THE STUDENT GRADE FROM 5 SUBJECT MARKS. PRINT 'A' GRADE IF THEIR PERCENTAGE IS >90 OR PRINT 'B' GRADE IF THEIR PERCENTAGE IS >75 AND <=90 OR PRINT 'C' GRADE IF THEIR PERCENTAGE IS >65 AND <=75 OR PRINT 'D' GRADE IF THEIR PRECENTAGE IS <=65.
sub1=int(input("enter mark1: "))
sub2=int(input("enter mark2: "))
sub3=int(input("enter mark3: "))
sub4=int(input("enter mark4: "))
sub5=int(input("enter mark5: "))
percentage=(sub1+sub2+sub3+sub4+sub5)*100/500
print("percentage=",percentage)
if percentage>90:
    print('Grade-A')
elif 75<percentage<=90:
    print('Grade-B')
elif 65<percentage<=75:
    print('Grade-C')
else:
    print('Grade-D')



output:
enter mark1: 74
enter mark2: 96
enter mark3: 84
enter mark4: 69
enter mark5: 81
percentage= 80.8
Grade-B
