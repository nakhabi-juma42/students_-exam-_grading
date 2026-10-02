


def get_valid_marks (subject):
  while True:
        try:
           marks = float(input (f" enter {subject} marks: "))
  
           if 0 <= marks <= 100:
             return marks 
           else:
             print ("invalid marks!! enter a value between 0 and 100")
        except ValueError:
             print ("please enter a number")
def analyze_student:    
  name = input( "Enter the student's name: ").title()
subjects={}
  while True:
    subject_name = input ("enter subject name (or type 'done' to finish: ").strip().title()
    if subject_name == 'Done':
       break
    if not subject_name:
       print("subject cannot be empty,please enter subject's name")
       continue 
    if subject in subject_name:
       print ("You have already entered the subject,please enter another subject ")
       continue 
   marks= get_valid_marks ( subject_name)
    subjects[subject_name]= marks
    
   total= sum(subjects.values())
   average = total/len (subjects)

   if average >= 80:
      grade= "A"
   elif average >= 70:
      grade= "B"
   elif average >= 60:
      grade= "C"
   elif average >= 50: 
      grade= "D"
   else:
      grade= "E"

   print("\n" + "=" * 35)
   print("  STUDENT RESULTS")
   print("=" * 35)

   if average >= 50:
    status= "PASS"
   else:
    status= "FAIL"

   print (f"Name: {name}")

   print ("\n___Student Results ___")
   for subject,marks in subjects.items():
   print (f"{subject} : {marks}")

   print (f"Total marks: {total}")
   print (f"Average: {average:.2f}")
   print (f"Grade:{grade}")
   print (f"Status: {status}")

   print("=" * 35)
 
while True:
   analyze_student()
   again= input ("\n analyze another student?( yes/ no): ").lower()

   if again != "yes":
print ("Thank you for using students performance analyzer!")
     #break 
 