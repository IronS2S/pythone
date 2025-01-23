reddito = float(input( "inserisci il tuo reddito"))
ALIQUOTA_1 = 0.77
ALIQUOTA_2 = 0.65
ALIQUOTA_3 = 0.57
if reddito < 28000 : 
    print ("il tuo reddito netto è", reddito*ALIQUOTA_1)
if reddito > 28000 and reddito < 50000: 
    print ("il tuo reddito netto è", reddito*ALIQUOTA_2)
if reddito > 50000 : 
    print ("il tuo reddito netto è", reddito*ALIQUOTA_3)