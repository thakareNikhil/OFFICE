from pickle import load, dump
def Delete():
    l = list()
    with open('EMP', 'rb') as e:
        while True:
            try:
                R=load(e)
                l.append(R)
            except EOFError:
                break
    with open('EMP', 'wb') as e:
        try:
            a=int(input('Enter EmpID:'))
            print('-'*50)
            for i in l:
                if i['EmpID']==a:
                    l.remove(i)
                    print(f'Deleted Successfully{chr(0x1F9F9)}...')
            else:
                print(f'Employee Not Found...{chr(0x1F622)}')
        except ValueError:
            print(f"Invalid EmpID...{chr(0x1F622)}")
        finally:
            for i in l:
                dump(i,e)
