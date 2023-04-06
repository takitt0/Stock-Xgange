from random import randint

def ginp(type=None, txt=None):
        if not type:
            return input(f"{txt}: ")
        
        return type(input(f"{txt}: "))

def abreviation(txt):
    if len(txt) < 3:
        raise Exception("Menos de 3 caracteres en abreviation(txt)")
    
    if len(txt.split()) > 1:
        return (''.join([x[0] for x in txt.split()])).upper() + str(randint(1, 9))
    else:
        return (txt[0] + txt[len(txt) // 2] + txt[-1]).upper() + str(randint(1, 9))
    