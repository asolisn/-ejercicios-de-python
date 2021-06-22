#while validacion
vocal=input("Ingrese la vocal")
while vocal not in ('a','e','i','o','u'):
    if vocal== '.':
        break
    vocal=input("Vocal:")
    print('Su vocal o punto es:{}'.format(vocal))
    