a = [1, 2]
b = [2, 3]
elementos_iguais=[]

i=0;
for numero in a:
    if b[i] in a:
        elementos_iguais.append(b[i])
    i+=1
        
print(elementos_iguais)