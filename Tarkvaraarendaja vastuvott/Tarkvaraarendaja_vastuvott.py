from minumoodul import *
sonastik={}
sonastik2={}
koik=[]
vastuvoetud=[]
eisoobi=[]
koik = loe_faelist(koik,"koik.txt")
print(koik)
while True:
    try:
        txttodictionary(sonastik,sonastik2,"vastus.txt")
        nimi=input("kirjuta siinu eesnimi ja perenimi ")
        menu=int(input(f"{nimi} te soovite testi teha, \n1-yah \n2-ei"))
        if menu==1:
            koik=test(sonastik,sonastik2,nimi,koik)
            sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")
        if menu==2:
            sorter(koik,vastuvoetud,eisoobi,"koik.txt","vastuvoetud.txt","eisoobi.txt")
            break
    except:
        print("viga")
print("Vastuvoetud:")
printfile("vastuvoetud.txt")
print("eisoobi:")
printfile("Eisoobi.txt")


