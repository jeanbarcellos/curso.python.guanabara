# Curso Python #09 - Manipulando Texto

frase = 'Curso em Vídeo Python'

print(frase)
print(frase[3])  # s
print(frase[3:13])  # so em Víde
print(frase[:13])  # Curso em Víde
print(frase[13:])  # o Python
print(frase[1:15])  # urso em Vídeo
print(frase[1:15:2])  # us mVdo
print(frase[1::2])   # us mVdoPto
print(frase[::2])  # Croe íe yhn

print("""Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
'when an unknown printer took a galley of type and scrambled it\n\n""")

print(frase.count('O'))  # 0
print(frase.upper().count('O'))  # 3

print(len(frase))  # 21

print(frase.replace('Python', 'Android'))  # Curso em Vídeo Android

print('Curso' in frase)  # True

print(frase.find('Curso'))  # 0 (posição)
print(frase.find('Vídeo'))  # 9 (posição)
print(frase.find('video'))  # -1 (não existe)

dividido = frase.split()
print(dividido)  # ['Curso', 'em', 'Vídeo', 'Python']
print(dividido[0])   # Curso
print(dividido[0][3])  # s


