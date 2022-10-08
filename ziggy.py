
#fonction de cryptage commence ici
def encrypt():

  msg=input("Veuillez saisir le message a Encrypter: ")
  cle=int(input("La clé de Chiffrement: "))

  #Creation d'une grille

  #Pour créer la grille de notre processus de cryptage, 
  #nous utilisons une liste vierge.  
  #mais pour plus de simplicité, nous avons utilisé des listes ici. 
  #La taille de la liste comme mentionné ci-dessus sera "la valeur de la clé" * "la longueur de la chaîne". 
  #Pour initialiser la liste, nous remplissons d'abord la liste avec ' '(espace simple)

#une liste vierge de taille 4*10 est créée.
  lista=[[" " for i in range(len(msg))] for j in range(cle)]
#print(lista)

#Mettre les caractère dans la grille
  flag=0
  row=0
# etape : analyser tous les caractères du texte brut et déterminer sa position dans la grille.
#L'indice de caractère sera le même que le numéro de colonne dans la grille. 
#Nous n'avons donc plus qu'à déterminer le numéro de ligne maintenant.
#Si flag=0, alors nous devons continuer vers le bas,
# et si flag=1, alors nous devons continuer vers le haut. 
#Donc, si flag=0, incrémente le numéro de ligne, et si flag=1,
#décrémente le numéro de ligne. Nous avons également besoin d'une condition pour changer la valeur des drapeaux.
#Ainsi, si le numéro de ligne du caractère actuel est 0, le drapeau sera 0, 
#et si le numéro de ligne est Key-1, c'est-à-dire. la dernière ligne, le drapeau sera 1.
  for i in range(len(msg)):
    lista[row][i]=msg[i]
    if row==0:
     flag=0
    elif row==cle-1:
      flag=1
    if flag==0:
      row+=1
    else:
      row-=1

  #affichage de la grille
  for i in range(cle):
    print("".join(lista[i]))

#Obtenir notre Text Chiffré
#nous devons lire notre grille ligne par ligne et éliminer les espaces entre chaque lettre d'affilée.
#Pour ce faire, nous allons analyser chaque caractère de chaque ligne et ajouter tous les caractères,
# qui ne sont pas des espaces, à une liste initialement vide 
    textChiffre=[]
  for i in range(cle):
    for j in range(len(msg)):
      #if lista[i][j]!=' ':
       textChiffre.append(lista[i][j])
#On convert notre liste 'textChiffre' en chaîne.
  encrypted="".join(textChiffre)

#On imprime le texte chiffré
  print("\nText Chiffré: ",encrypted)


def decrypt():
  cipher=input("Veuillez saisir le message a Decrypter: ")
  key=int(input("La clé de Chiffrement: "))
  rail = [['\n' for i in range(len(cipher))]
  for j in range(key)]
  dir_down = None
  row, col = 0, 0
  for i in range(len(cipher)):
      if row == 0:
        dir_down = True
      if row == key - 1:
        dir_down = False

  rail[row][col] = '*'
  col += 1
  if dir_down:
    row += 1
  else:
    row -= 1

  index = 0
  for i in range(key):
    for j in range(len(cipher)):
      if ((rail[i][j] == '*') and(index < len(cipher))):
        rail[i][j] = cipher[index]
        index += 1
  result = []
  row, col = 0, 0
  for i in range(len(cipher)):
    if row == 0:
      dir_down = True
    if row == key-1:
      dir_down = False

    if (rail[row][col] != '*'):
      result.append(rail[row][col])
      col += 1

    if dir_down:
      row += 1
    else:
     row -= 1
  decrypted="".join(result)

  print("\nText Déchiffré: ",decrypted)

if __name__ == '__main__':
  menu_options = {
     
    1: 'Encrypter',
    2: 'Decrypter',
    3: 'Quitter',
  }

  def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] ) 
while True:
  print('\n')
  print_menu()
  option = int(input('\nEnter your choice: ')) 
  if option == 1:
      print('\n\\\\\\\ Cryptage //////')
      encrypt()
  elif option == 2:
      print('\n\\\\\\\ Decryptage //////')
      decrypt()
  elif option == 3:
      print('Merci d''avoir utiliser mon prog')
      exit()
  else:
      print('\nChoix indisponible.Veuillez choisir entre 1 et 3.')

#print(decryptRailFence("CeopedSdey", 4))
