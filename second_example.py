A = float(input("Entrez la valeur de A : "))
B = float(input("Entrez la valeur de B : "))
Op = input("Entrez l'opérateur (+, -, *, /, %) : ")
if  Op == "+" :
   print("le resultat est;",A + B)
elif Op == "-" :
   print("le resultat est:",A - B)
elif Op == "*" :
   print("le resultat est;" ,A * B)
elif Op == "/" :
   print ("le resultat est:",A / B)
elif Op == "%" :
    print("le resultat est:", A % B)
else:
    print("Opérateur invalide !")