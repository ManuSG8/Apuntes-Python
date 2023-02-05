def array_diff(a,b):

    """lista = []

    for i in b:     
        for j in a:
            if j != i:
                lista.append(j)
                
    return lista""" # Non funciona eh, pero para que vexas cal é o problema no futuro

    for z in range(len(b)+1):
        for i in b:     
            for j in a:
                if j == i:
                    a.remove(j)
        
    return a


print(array_diff([1, 2, 2, 2, 3, 4], [2, 3]))



# Otras soluciones

def array_diff(a, b):
    return [x for x in a if x not in b]



def array_diff(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a