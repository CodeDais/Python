phy=int(input('enter phy mark'))
chem=int(input('enter chem mark'))
math=int(input('enter math mark'))
bio=int(input('enter bio mark'))
it=int(input('enter it mark'))
eng=int(input('enter eng mark'))

totalmark=phy+chem+math+bio+it+eng

avgmark=totalmark/6

print('------------------------')
print('Total Mark is ',totalmark)
print('Avg Mark is ',avgmark)

if avgmark>=90:
    print('O Grade')
elif avgmark>=80 and avgmark<=89:
    print('E Grade')
elif avgmark>=70 and avgmark<=79:
    print('A Grade')
elif avgmark>=60 and avgmark<=69:
    print('B Grade')
elif avgmark>=50 and avgmark<=59:
    print('C Grade')
elif avgmark>=40 and avgmark<=49:
    print('D Grade')    
else:
    print('Fail - Better Luck Next Time')