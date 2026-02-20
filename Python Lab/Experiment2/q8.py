name= input('Enter your name: ')
rollno = input('Enter your roll number: ')
sapid= input('Enter your SAPID: ')
sem = input('Enter your semester: ')
course = input('Enter your course: ')
m1= int(input('Enter marks of PDS: '))
m2= int(input('Enter marks of Python: '))
m3= int(input('Enter marks of Chemistry: '))
m4= int(input('Enter marks of English: '))
m5= int(input('Enter marks of Physics: '))
percent= (m1+m2+m3+m4+m5)/5
cgpa= percent /10
print(name
      ,rollno
      ,sapid
      ,sem
      ,course)
print('Subject Name, Marks')
print('PDS', m1)
print('Python', m2)
print('Chemistry', m3)
print('English', m4)
print('Physics',m5)
print('Percentage:', percent)
print('CGPA:', cgpa)
if cgpa>=9.1:
    print('O grade')
elif cgpa>=8.1 and cgpa<=9:
    print('A+ grade')
elif cgpa>=7.1 and cgpa<=8:
    print('A grade')
elif cgpa>=6.1 and cgpa<=7:
    print('B+ grade')
elif cgpa>=5.1 and cgpa<=6:
    print('B grade')
elif cgpa>=3.5 and cgpa<=5:
    print('C+ grade')
else:
    print('F grade')
