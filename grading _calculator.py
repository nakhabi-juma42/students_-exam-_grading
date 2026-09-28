print("student analyzer calculator")
name =input ("Enter the student's name: ).title()


def get_valid_marks (subject):
    while True:
        try:
  marks = float(input (f" enter {subject} marks: "))
  
  while marks < 0 or marks > 100:
      print ("invalid marks!! enter a value between 0 and 100)
        except Value error:
           print ("please enter a number")
      marks = float( input(f"enter {subject} marks: ")) 
      return marks
subject={}
while True:
    subject_name = input ("enter subject name (or type 'done' to finish: ").title()
    if subject_name == 'Done':
       break
     marks= 
   get_valid_marks ( subject_name)
       subjects[subject_name]= marks
    

if not subjects:
   print("no subject was entered ")
else: 
    total= sum(subjects.values())
    average = subject/len (subjects)
print("\n" + "=" * 35)
print(". STUDENT RESULTS")
print("=" * 35)
for subject,marks in student.items():
  print (f"{subject} : {marks}")

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

if average >= 50:
    status= "PASS"
else:
    status= "FAIL"


print ("\n___Student Results ___)
print (f"Name: {name}")
print (f"Total marks: {total})
print (f"Average: {average:.2f}
print (f"Grade:{grade})
print (f"Status: {status}")

print("=" * 35)
