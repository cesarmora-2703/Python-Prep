import os
print(os.getcwd())
if(not os.path.isdir('Carpeta_prueba')):
    os.makedirs('Carpeta_prueba')

if(os.path.isdir('Carpeta_prueba')):
    os.chdir('Carpeta_prueba')
    print('Me cambie a: ', os.getcwd())

os.chdir('..')
print('Me cambie a: ', os.getcwd())

if os.path.isfile('README.md'):
    print(os.path.getsize('README.md'))

#Eliminar archivo
os.remove(os.getcwd() + '/datos.txt')

if(os.path.isdir('Carpeta_prueba')):
    os.rmdir('Carpeta_prueba')

print(os.listdir())