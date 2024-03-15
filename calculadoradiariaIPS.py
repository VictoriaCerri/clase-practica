porc = 0.287479
print ('Ingrese el numero de base: ')
n = float(input())
res = porc * n / 100 
print ('El' ,porc, 'porciento de' ,n, ' es' , round(res, 2))
pDiario = res
sT = pDiario + n
print ('el resultado actual es:' ,sT)
input('presione Enter para continuar:')

nD = sT
res = porc * nD / 100 
print ('El' ,porc, 'porciento de' ,nD, ' es' , round(res, 2))
pDiario = res
sTD = pDiario + nD
print ('el resultado actual 2 es:' ,sTD)
input('presione Enter para continuar:')

nT = sTD
res = porc * nT / 100 
print ('El' ,porc, 'porciento de' ,nT, ' es' , round(res, 2))
pDiario = res
sTT = pDiario + nT
print ('el resultado actual 3 es:' ,sTT)
input('presione Enter para continuar:')
        
nC = sTT 
res = porc * nC / 100
print ('El', porc, 'porciento de' , nC, ' es' , round(res, 2))
pDiario = res
sTC = pDiario + nC
print ('el resultado actual 4 es:' ,sTC)
input('presione Enter para continuar:')
#########################################################################3
nQ = sTC
res = porc + nQ / 100 
print ('El', porc, 'porciento de', nQ , 'es' , round(res, 2))
pDiario = res
sTQ = pDiario + nQ 
print ('el resultado actual 5 es:', sTQ)
input ('presione Enter para continuar:')

nS = sTQ
res = porc + nS / 100
print('El' ,porc , 'porciento de' , nS , 'es' , round(res, 2))
pDiario = res
sTS = pDiario + nS 
print ('el resultado actual 6 es:', sTS)
input ('presione Enter para continuar:')

nSi = sTS
res = porc + nSi / 100
print('El' ,porc , 'porciento de' , nSi , 'es' , round(res, 2))
pDiario = res
sTSi = pDiario + nSi 
print ('el resultado actual 6 es:', sTSi)
input ('presione Enter para continuar:')


        