d = {}
while True:
    bf = input('enter the bf name : ')
    gf = input('entre your gf name : ')
    d[bf] = gf

    choice = input('do you want to add more item [Y/N]')
    if choice == 'N':
        break

while True:
    bf = input('enter bf name to get gf name : ')
    gf = d.get(bf, 0)

    if gf == 0:
        print('Sry bf name is not availbale')
    else:
        print(f'Hi {bf} your gf name is {gf}')

    choice = input('do you want to serach more item [Y/N]')

    if choice == 'N':
        break
