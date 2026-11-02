class SpaceError(Exception):pass
class EmptyError(Exception):pass
class AlphaError(Exception):pass

def valid(n):
    a=n.title().split()
    if len(n)==0:
        raise EmptyError
    else:
        if n.isspace():
            raise SpaceError
        else:
            b=True
            for i in a:
                if not i.isalpha():
                    b=False
                    raise AlphaError
                    break
            else:
                if b:
                    return ' '.join(a)
