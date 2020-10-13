"""

Program: student_files.py

Author: Donald Butters

Last date modified: 10/12/2020

The purpose of the program is to tie together seemingly unrelated tuple and arbitrary arguments list
to perform file input and output


 :param parameter_1: use arbitrary arguments list and unrelated tuples
 :param parameter_2: perform file input and output
 :call in main: call the functions in main with key to end

"""
def write_to_file(data):
    f = open('student_info.txt', 'a')
    f.write(str(data) + '\r')
    f.close()

def get_student_info(**passname):
    scores = []
    #print(name)
    for key, value in passname.items():
        scores.append(value)
        print(scores)
    count = int(input('How many scores would you like to enter?:  '))
    for i in range(0, count):
        x = input('Please Enter a Test Score: ')
        scores.append(x)
    print('Finished')
    write_to_file(tuple(scores))

def read_from_file(file):
    f = open(file, 'r')
    for r in f:
        print(r)

def search_array(file):
    name = input('Enter the name of a student :')
    f = open(file,'r')
    if name in f.read().split():
        print('Student found')
    else:
        print('Student not found')




    #accepts a tuple to be added to the end of a file
    #Opens the file for appending "student_info.txt"
    #Write the tuple on one line(include any new line characters)
    #close the file"""
