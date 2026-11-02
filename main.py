from addemp import *
from viewemp import View,Search,Count
from delete import Delete
from update import Update
while True:
    print('>'*50)
    print(f'{chr(128525)}WELCOME TO EMPLOYEE MANAGEMENT SYSTEM{chr(128525)}'.center(50))
    print('<'*50)
    print("""
    1.Add Employee
    2.View All Employees
    3.Search Employee by ID
    4.Update Employee Details
    5.Delete Employee
    6.Count Total Employees
    7.Exit""")
    print('-'*50)
    a=input('Entre Option:')
    match a:
        case '1':
            Add()
        case '2':
            View()
        case '3':
            Search()
        case '4':
            Update()
        case '5':
            Delete()
        case '6':
            Count()
        case '7':
            print(f'Thank You{chr(128522)}     '.center(20))
            print(f'Visit Again{chr(129309)}....'.center(20))
            exit()
        case _:
            print('Invalid Option You Entered ')

