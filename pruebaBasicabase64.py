import base64
file = open('output.txt', 'r', encoding='utf-8')
data = file.read()
numero = int(input('Introduce el numero de veces a realizar: '))
for i in range(1, numero+1):
    data = base64.b64decode(data)
    print(data)
