import re
from datetime import datetime

def matchTexte(texte):

    patron = 'ab*?'

    if re.search(patron, texte):
        return 'trouvé !'
    else:
        return 'rien trouvé !'

print(matchTexte("acdddd"))
print(matchTexte("ab"))
print(matchTexte("abbc"))
print(matchTexte("a0b"))

def minusculeMajuscule(texte):

    patron = '[A-Z]+[a-z]+$'

    if re.search(patron, texte):
        return 'trouvé !'
    else:
        return 'rien trouvé !'

print('\n')
print(minusculeMajuscule('Virgile'))
print(minusculeMajuscule('vIrgile'))
print(minusculeMajuscule('python'))
print(minusculeMajuscule('Python'))

def a_to_b(texte):

    patron = 'a.*?b$'
    if re.search(patron, texte):
        return 'trouvé !'
    else:
        return 'rien trouvé !'

print('\n')
print(a_to_b('aVirgileb'))
print(a_to_b('Virgile'))
print(a_to_b('aCartierc'))

def z_midDetector(texte):

    patron = '\Bz\B'
    if re.search(patron, texte):
        return 'trouvé !'
    else:
        return 'rien trouvé !'

print('\n')
print(z_midDetector('Je suis un zèbre.'))
print(z_midDetector("J'ai bien peur que la lettre recherché soit absente ici...."))

print('\n')
texte = 'Il est certain que\nla lettre était placée*bien trop haut pour être trouvée.'
print(re.split('; |, |\*|\n',texte))

texte = 'abnormally and slowly, our friend is usefully being lightly lost.'

for r in re.finditer(r"\w+ly", texte):
    print('%d-%d : %s' % (r.start(), r.end(), r.group(0)))

print('\n')
texte = 'Il est terriblement grand pour son âge. Il ne faut se leurrer, voilà qui est affreusement anormal !'

for r in re.finditer(r"\w+ment", texte):
    print('%d-%d : %s' % (r.start(), r.end(), r.group(0)))

date_fr = "25-12-2021 l'année heureuse des personnes heureuses ! !!!"
date_us = "2021-05-06 one of the absolute greatest year ever !! "

print('\n')
def dateUS(texte):
    datePotentielle = re.search(r'\d{4}-\d{2}-\d{2}', texte)
    date = datetime.strptime(datePotentielle.group(), '%Y-%m-%d').date()
    return str(date)

print(dateUS(date_us))

print('\n')

def dateFR(texte):
    datePotentielle = re.search(r'\d{2}-\d{2}-\d{4}', texte)
    date = datetime.strptime(datePotentielle.group(), '%d-%m-%Y').date()
    return str(date)

print(dateFR(date_fr))
