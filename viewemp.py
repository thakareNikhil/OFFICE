from pickle import load
def View():
    with open('EMP','rb') as f:
        b=1
        while True:
            try:
                a=load(f)
                for k,v in a.items():
                    print(f'{k} = {v}',end=' ')
                print()
            except EOFError:
                print(''.center(50,'-'))
                print(f'{chr(128077)} DONE...'.center(50))
                break
            b+=1
def Search():
    c=[]
    with open('EMP','rb') as f:
        try:
            a=int(input('Enter Employee ID:'))
            print(''.center(50,'-'))
            while True:
                try:
                    b=load(f)
                    for k in b.values():
                        if k==a:
                            c.append(b)
                            print(f'Employee Found!{chr(128525)}')
                            for m,n in b.items():
                                print(f'{m} = {n}')
                except EOFError:
                    if len(c) == 0:
                        print(''.center(50, '-'))
                        print(f'Employee Not Found {chr(128546)}...')
                        break
                    else:
                        print(''.center(50,'-'))
                        print(f'{chr(128077)} DONE...'.center(50))
                        break
            else:
                if len(c) == 0:
                    print('Employee Not Found..')

        except ValueError:
            print('Entre Valid ID...')
def Count():
    with open('EMP','rb') as f:
        b=1
        while True:
            try:
                a=load(f)
                for k,v in a.items():
                    k,v
            except EOFError:
                print(''.center(50,'-'))
                break
            b+=1
        print('Total Employees:',b-1)
