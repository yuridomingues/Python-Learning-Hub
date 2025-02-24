x = 4.5
x.as_integer_ratio()
# will show (9, 2) dois numeros inteiros quando 
# divididos que dão o numero

x.is_integer() 
# if is a integer number in the math pattern
# will show false
# 4.0 will show True

y = 4.9
int(y) # will be 4


######### STRING METHODS

s = 'abc'
# dir(s) to show methods

palavra = 'Olá MunDo!'
palavra.upper() # all to uppercase
palavra.lower() # all to lowercase

arquivo = '2025_04_01_Namoro.pdf'
arquivo.endswith('.pdf') # will show True

arquivo.startswith('2025') # will show true

if arquivo.startswith('2025') and arquivo.endswith('.pdf'):
    print('Founded')

text = 'Hoje em todo dia é um novo dia.'
print(text.count('e')) # will show 2
print(text.count('dia')) # will show 2

text.lower().count('hoje')

seq = 'aaaaaaabaaaaaaaab'
seq.find('b') # the first position
# if there is no one, will show -1

# but you can use .index to show a error

seq[seq.find('b'):]

s1 = '3123123123123'
s1.isdigit() # will show true

s2 = 'ASDdqwodwqkdqodkqodkwq'

s2.isalpha() # will show true

frase = 'estou estudand python'
frase.replace('estou', 'estava')
print(frase.replace('estou', 'estava'))