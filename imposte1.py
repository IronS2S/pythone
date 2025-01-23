reddito = float(input( "inserisci il tuo reddito"))
ALIQUOTA_1 = 0.23
ALIQUOTA_2 = 0.35
ALIQUOTA_3 = 0.
if reddito < 28000 : 
    print ("la tua imposta è", reddito*ALIQUOTA_1)
if reddito > 28000 and reddito < 50000: 
    print ("la tua imposta è", reddito*ALIQUOTA_2)
if reddito > 50000 : 
    print ("la tua imposta è", reddito*ALIQUOTA_3)