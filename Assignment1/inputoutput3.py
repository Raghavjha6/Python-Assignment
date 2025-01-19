'''Q. If the marks obtained by a student in five different subjects are input through the keyboard,
find out the aggregate marks and percentage marks obtained by the student. Assume that the
maximum marks that can be obtained by a student in each subject is 100.'''

sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))
aggregate_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (aggregate_marks / 500) * 100
print("Aggregate Marks: ", aggregate_marks)
print("Percentage: ", percentage, "%")
