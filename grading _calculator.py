print("student analyzer calculator")
name =input ("Enter the student's name: ).title()


def get_valid_marks (subject):
  marks = float(input (f" enter {subject} marks: "))
  
  while marks < 0 or marks > 100:
      print ("invalid marks!! enter a value between 0 and 100")
      marks = float( input(f"enter {subject} marks: ")) 
      return marks


Physics= get_valid_ marks("physics")

Chemistry= get_ valid_ marks(" chemistry ")
Biology= get_valid_ marks("Biology")

subjects =[Physics, Chemistry, Biology]
# subject.append()

total= 0 
for subject in subjects:
   total+= subject 
average = subject/len (subjects)

if average >= 80:
   grade= A
elif average >= 70:
   grade= B
elif average >= 60:
   grade= C
elif average >= 50: 
   grade= D
else:
   grade= E
print (f"Grade:{grade})
if average >= 50:
    status= "PASS"
else:
    status= "FAIL"
print(f"Status: {status}")

print ("\n___Student Results ___)
print (f"Name: {name}")
print (f"Total marks: {total})
print (f"Average: {average:.2f}

