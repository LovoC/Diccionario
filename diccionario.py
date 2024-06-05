import time
while True:
    genz = {
        "CRINGE": "Algo realmente vergonzoso",
        "LOL": "Respuesta a algo gracioso",
        "XD": "Algo realmente gracioso",
        "F": "Respuesta a algo que salio mal",

    }    
    print ("Te puedo decir que significa: 1. CRINGE, 2. LOL, 3. XD, 4. F""\n")
    time.sleep(1)
    
    word = input("Dime una palabra que no entiendas (MAYUSCULAS)")

    if word in genz.keys():
        print (genz[word])
        time.sleep(1)
        print ("\n""espera 3 segundos para continuar.")
        time.sleep(1)
        print ("1")
        time.sleep(1)
        print ("2")
        time.sleep(1)
        print ("3""\n")
        time.sleep(1)
     
    
    else:
        print ("No se que sifnifica eso")
        time.sleep(1)
        print ("espera 3 segundos para continuar.")
        time.sleep(1)
        print ("1")
        time.sleep(1)
        print ("2")
        time.sleep(1)
        print ("3")
        time.sleep(1)
