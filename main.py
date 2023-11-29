
etel_lista=["Rakott krumpli","Spenótos tészta","Franciahagymaleves","Barackkrémleves"]
etel_ar=[1600,1400,1250,1300]
rendeles=[]
etlap_lista=["Étel","Főétel","Levesek"]

import etlap
etlap_meret: int = 36

'''def etlap():
    kiiras:int=0
    for i in range(0, len("*", etlap_meret), 1):
        print("*", etlap_meret)

    szoveg:int=0
    for i in range(0, len(etlap_lista), 1):
        print("*", etlap_lista[i], "*", etlap_meret)

       
    
    kis_szoveg:int=0
    for i in range(0, len("*", etel_lista[i], etel_ar[i], "*", etlap_meret)):
        print("*", etel_lista[i], etel_ar[i], "*", etlap_meret)

        return kis_szoveg'''

etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", etlap_lista[1], "*", etlap_meret)






etlap.kis_szöveg("*", etel_lista[1], etel_ar[1], "*", etlap_meret)












'''
etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", "Étlap", "*", etlap_meret)

etlap.kiiras("*", etlap_meret)

etlap.szöveg("*", "Főétel", "*", etlap_meret)

etlap.kiiras("*", etlap_meret)

 for i in range(0, len(etel_lista)):
    etlap.kis_szöveg("*", etel_lista[i],str(etel_ar[i])+"Ft", "*", etlap_meret)

   

etlap.kiiras4("*", etlap_meret)

etlap.szöveg3("*", "Levesek", "*", etlap_meret)

etlap.kiiras5("*", etlap_meret)

etlap.kis_szöveg3("*", "Franciahagymaleves:", "300Ft", "*", etlap_meret)

etlap.kis_szöveg4("*", "Barackkrémleves:", "300Ft", "*", etlap_meret)'''





import rendeles
rendeles.foetel("*", etlap_meret)
rendeles.leves("*", etlap_meret)


import rendelesosszegzes
rendelesosszegzes.szamla("Barackrémleves",300,"Francia hagymaleves",300)

import kozos_eljaras
kozos_eljaras.focim("*", 36)
kozos_eljaras.szoveg_kiiaras("*", "Rendelés", "*")
kozos_eljaras.focim("*", 36)

kozos_eljaras.foetelek(f"", "300Ft")
kozos_eljaras.foetelek("Rakot Krumpli", "300Ft")

kozos_eljaras.focim("*", 36)
rendelesosszegzes.szoveg_kiiras("*","Köszönjük hogy a vendégünk volt","*")
kozos_eljaras.focim("*", 36)



