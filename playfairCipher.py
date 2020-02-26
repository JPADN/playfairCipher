
# Palavra-chave: BEATRIZ
tabelaChave = [['B','E','A','T','R'],
               ['I','Z','C','D','F'],
               ['G','H','K','L','M'],
               ['N','O','P','Q','S'],
               ['U','V','W','X','Y']]

txtPleno = str(input('Digite a palavra a ser encriptada: '))

# Preparando a string 
txtPleno = txtPleno.replace(' ','')
txtPleno = txtPleno.upper()

digrafos = []
for i in range(0,len(txtPleno),2):
    try:    
        if digrafos[i] == digrafos[i+1]:
            
        digrafos.append(txtPleno[i]+txtPleno[i+1])
    except IndexError:
        digrafos.append(txtPleno[i] + 'X')

print(digrafos)

for pair in digrafos:
    if pair[i] == pair[i+1]:
        pair = pair[i]+'X'

