# Crie um código que conta o número de vogais de um bloco de texto
# qualquer. O código deve desconsiderar letras maiúsculas/minúsculas
# isto é, "a" e "A" contam da mesma forma.
# O texto pode ser colado diretamente como um string no código

text = "hello my name is yuri and i am learning python"
text = text.lower()

a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'

vowel = text.count(a)
print(f"Há {vowel} letras A no texto")
vowel = text.count(e)
print(f"Há {vowel} letras E no texto")
vowel = text.count(i)
print(f"Há {vowel} letras I no texto")
vowel = text.count(o)
print(f"Há {vowel} letras O no texto")
vowel = text.count(u)
print(f"Há {vowel} letras U no texto")

## OR you can make a more slower resolution

vowels = {
    'A': 0,
    'E': 0,
    'I': 0,
    'O': 0,
    'U': 0
}

text = text.upper() 

for char in text: 
    if char == 'A':
        vowels['A'] += 1
    if char == 'E':
        vowels['E'] += 1
    if char == 'I':
        vowels['I'] += 1
    if char == 'O':
        vowels['O'] += 1
    if char == 'U':
        vowels['U'] += 1

for vowel, counting in vowels.items():
    print(f'Há {counting} letras {vowel} no texto')
