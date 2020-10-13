import sys



from students_files import get_student_info
from students_files import read_from_file
from students_files import search_array

get_student_info(name='Daniel')
get_student_info(name='Donald')
get_student_info(name='Dennis')
get_student_info(name='Dee')

students = 'student_info.txt'
read_from_file(students)


x = input('Press Enter to exit.')
if len(x) >= 0:
    print('\n' * 25)
    sys.exit()





if __name__ == '__main__':
    print()



