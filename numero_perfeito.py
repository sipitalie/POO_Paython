def numero_perfeito(num):
    soma=[]
    for i in range(1, num):
        if num % i == 0 :
            soma.append(i)
    x=sum(soma)
    if x == num:
        return True
    else:
        return False
saida=numero_perfeito(28)

def tupla_par(tupla):
    lis=[]
    for i in range(len(tupla)):
        if i % 2 == 0 :
            lis.append(tupla[i])
    tup=tuple(lis)

    return tup
tupla=('não', 'quero', 'mais', 'nada', 'contigo')
saida= tupla_par(tupla)
print (saida)
        
