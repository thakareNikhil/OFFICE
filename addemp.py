import sys
from pickle import dump,load
sys.path.append(r"C:\Users\DELL\OneDrive\Desktop\OFFICE\Validations")
from name import *
def List():
    l=list()
    with open('EMP','rb') as e:
        while True:
            try:
                R=load(e)
                for k,v in R.items():
                    if k=='EmpID':
                        l.append(v)
            except EOFError:
                break
    return l
x=List()
def Add():
    global x
    with open('EMP', 'ab') as f:
        r=int(input('How many Employees Want To Add?:'))
        b=1
        while b<=r:
            try:
                print(f'Employee No :{b}')
                a={'EmpID':int(input('Enter EmpID No:')),'EmpName':valid(input('Entre EmpName:')),'EmpSalary':input('Entre Salary:')}
                if a['EmpID'] not in x:
                    if a['EmpSalary'].isdigit():
                        dump(a,f)
                        x.append(a)
                    else:
                        print('Invalid Salary')
                        break
                else:
                    print('-'*50)
                    print(f"""
                    Employee No:{b}
                    ID = {a['EmpID']}
                    Name = {a['EmpName']}
                    Salary= ${a['EmpSalary']}.00
                    Already Exists""")
                    break
                b+=1
            except EmptyError:
                print(''.center(50,'-'))
                print("Don't Leave Name Field Empty...")
                print(f'Try Again {chr(128257)}...')
                print(''.center(50,'-'))
            except AlphaError:
                print(''.center(50,'-'))
                print("Don't Entre Special_symbols or Digits as Name...")
                print(f'Try Again {chr(128257)}...')
                print(''.center(50,'-'))
            except SpaceError:
                print(''.center(50,'-'))
                print("Don't Entre Only Spaces as Name...")
                print(f'Try Again {chr(128257)}...')
                print(''.center(50,'-'))
            except ValueError:
                print(''.center(50,'-'))
                print('Entre Valid ID')
                print(f'Try Again {chr(128257)}...')
                print(''.center(50,'-'))
        else:
            print(f'Employee Added Successfully {chr(128077)}')

