# Explain your work

studentInfo = {'MidtermGrade': [], 'ProjectGrade': [], 'FinalGrade': [], 'PassingGrade': []}  # Declare Dictionary

for i in range(5):  # Take input from user
    print('Enter Student ', i + 1, ' details')
    midterm = float(input('Enter Midterm Grade: '))
    project = float(input('Enter Project Grade: '))
    final = float(input('Enter Final Grade: '))

    studentInfo['MidtermGrade'].append(midterm)
    studentInfo['ProjectGrade'].append(project)
    studentInfo['FinalGrade'].append(final)
    studentInfo['PassingGrade'].append(0.3 * midterm + 0.3 * project + 0.4 * final)

for i in range(5):  # Display Details of Student
    print('Student ', i + 1, ' details:')
    print('Midterm Grade: ', studentInfo['MidtermGrade'][i])
    print('Project Grade: ', studentInfo['ProjectGrade'][i])
    print('Final Grade : ', studentInfo['FinalGrade'][i])
    print('Passing Grade: ', studentInfo['PassingGrade'][i])
    print('-----------------------------------------')

print('\n')

for i in range(5):  # Sort the dictionary data based on passing grade
    for j in range(i + 1, 5):
        if studentInfo['PassingGrade'][j] < studentInfo['PassingGrade'][i]:
            studentInfo['MidtermGrade'][j], studentInfo['MidtermGrade'][i] = studentInfo['MidtermGrade'][i], \
                                                                             studentInfo['MidtermGrade'][j]
            studentInfo['ProjectGrade'][j], studentInfo['ProjectGrade'][i] = studentInfo['ProjectGrade'][i], \
                                                                             studentInfo['ProjectGrade'][j]
            studentInfo['FinalGrade'][j], studentInfo['FinalGrade'][i] = studentInfo['FinalGrade'][i], \
                                                                         studentInfo['FinalGrade'][j]
            studentInfo['PassingGrade'][j], studentInfo['PassingGrade'][i] = studentInfo['PassingGrade'][i], \
                                                                             studentInfo['PassingGrade'][j]

print('Data arranged in Increasing order of Passing Grade')
for i in range(5):  # Print details after sorting
    print('Student ', i + 1, ' details:')
    print('Midterm Grade: ', studentInfo['MidtermGrade'][i])
    print('Project Grade: ', studentInfo['ProjectGrade'][i])
    print('Final Grade : ', studentInfo['FinalGrade'][i])
    print('Passing Grade: ', studentInfo['PassingGrade'][i])
    print('-----------------------------------------')
