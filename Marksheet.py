print('\n**********Marksheet Assignment**********')

#Input marks of 5 subjects, calculate total, calculate individual % age of subjects, calculate

def subjectdetails(total_subjects):  #function to get subjects details i.e. name of each subject, total marks of each subject, obtained marks of each subject from user
    i = 1

    subject_names = [None] * total_subjects
    subject_max_marks = [None] * total_subjects
    subject_obtained_marks = [None] * total_subjects

    while i<=total_subjects: 
        print("\n****Subject " + str(i) + "****")
        subject_names[i-1] = input('Name: ')
        subject_max_marks[i-1] = input('Maximum Marks: ')
        subject_obtained_marks[i-1] = input('Obtained Marks: ')
        i+=1
    return subject_names, subject_max_marks, subject_obtained_marks


def printing(student_name, student_class, subject_details): #function to print the marks sheet

    subject_names = subject_details[0]
    numeric_subject_maximum_marks = [int(num) for num in subject_details[1]]  #string to int conversion of list containing subject max marks
    numeric_subject_obtained_marks = [int(num) for num in subject_details[2]]  #string to int conversion of list containing subject max marks

    total_maximum_marks = sum(numeric_subject_maximum_marks)  #Course total maximum marks
    total_obtained_marks = sum(numeric_subject_obtained_marks)  #Course total obtained marks
    
    counter=0
        
    print('\n\n************  Marksheet  ************')
    print('\nName: ' + student_name + '              Class: ' + student_class)
    print('\nSubject        Maximum Marks        Obtained Marks')
    
    while counter<len(subject_names): #loop to print all subjects details
        print('\n'+subject_names[counter]+'        '+str(numeric_subject_maximum_marks[counter])+'        '+str(numeric_subject_obtained_marks[counter]) )
        counter+=1

    print('\n\nTotal Marks: ' + str(total_maximum_marks) + '        Obtained Marks: ' + str(total_obtained_marks))  #printing total maximum and obtained marks of course
    return()



def marksheet():  #Main function to start 
    student_name = input("\nEnter your name: ")
    student_class = input('\nEnter you class: ')

    total_subjects = input("\nEnter total numbers of subjects to print on marksheet: ") #Total numbers of subjects to print on marksheet
    if total_subjects.isdigit()==False:   #check if user entered a numeric value
        print('please enter numeric value')
        marksheet()
    else:
        print("\n******Enter details of your subjects******")
        subject_details = subjectdetails(int(total_subjects))   #call to subjectdetails function to get details of all subjects from user
        printing(student_name, student_class, subject_details)   #call to printing function to print the marksheet
    return

marksheet() #call to marksheet function to start program  