import sys
sys.path.append(r"C:\Users\DELL\OneDrive\Desktop\OFFICE\Validations")
from name import *
from pickle import load,dump

def Update():
    l = list()
    with open('EMP', 'rb') as e:
        while True:
            try:
                R=load(e)
                l.append(R)
            except EOFError:
                break
    with open('EMP','wb') as e:
        try:
            a=int(input('Enter EmpID:'))
            print('-'*50)
            for i in l:
                if i['EmpID']==a:
                    print('Employee Found...')
                    print(str(i).strip('{}'))
                    print("""
                    1.For Update EmpName
                    2.For Update EmpSalary
                    3.Exit""")
                    print('-' * 50)
                    b=input('Entre Option:')
                    print('-' * 50)
                    match b:
                        case '1':
                            c=l.index(i)
                            try:
                                d=valid(input('Entre New EmpName:'))
                                l[c]['EmpName']=d
                            except EmptyError:
                                print(''.center(50, '-'))
                                print("Don't Leave Name Field Empty...")
                                print(f'Try Again {chr(128257)}...')
                                print(''.center(50, '-'))
                            except AlphaError:
                                print(''.center(50, '-'))
                                print("Don't Entre Special_symbols or Digits as Name...")
                                print(f'Try Again {chr(128257)}...')
                                print(''.center(50, '-'))
                            except SpaceError:
                                print(''.center(50, '-'))
                                print("Don't Entre Only Spaces as Name...")
                                print(f'Try Again {chr(128257)}...')
                                print(''.center(50, '-'))
                            except ValueError:
                                print(''.center(50, '-'))
                                print('Entre Valid ID')
                                print(f'Try Again {chr(128257)}...')
                                print(''.center(50, '-'))
                            else:
                                print('-' * 50)
                                print(f'EmpName Updated Successfully{chr(0x1F60D)}...')
                                break
                        case '2':
                            c = l.index(i)
                            d = input('Entre New EmpSalary:')
                            if d.isdigit():
                                l[c]['EmpSalary'] = d
                                print(f'Emp Salary Updated Successfully{chr(0x1F60D)}...')
                                break
                            else:
                                print(f'Invalid Salary Input...{chr(0x1F622)}')
                                print('-' * 50)
                            print('-' * 50)
                        case '3':
                            print(f'Nothing Changed...{chr(0x2757)}')
                            break
                        case _:
                            print(f'Invalid option...{chr(0x1F622)}')
                    break
            else:
                print(f'Employee Not Found...{chr(0x1F622)}')

        except ValueError:
            print(f'Invalid EmpID...{chr(0x1F622)}')
        finally:
            for i in l:
                dump(i,e)
