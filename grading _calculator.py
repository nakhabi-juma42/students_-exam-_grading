print("student analyzer calculator")
name =input ("Enter the student's name: ).title()
marks= float(input("enter student's marks: ))

Physics= float(input("enter physics marks: ))
Chemistry= float( input( "enter chemistry marks: ))
Biology= float(input("entry biology marks: ))

subjects =[Physics, Chemistry, Biology]
# subject.append()

total= 0 
for subject in subjects:
   total+= subject 
average = subject/3

if average >= 80:
  print ("Kudos {name}! you got A")
elif average >= 70:
  print ("{name} you got B")
elif average >= 60:
  print ("{name} you got C")
elif average >= 50: 
  print ({name} you got D")
else:
  print ({name} you can do better,you got E)

