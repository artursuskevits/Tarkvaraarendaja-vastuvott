from minumoodul import *
sonastik={}
sonastik2={}
koik=[]
vastuvoetud=[]
eisoobi=[]
koik = loe_faelist(koik,"koik.txt")
print(koik)
while True:
    #try:
    


    
    file=open("vastus.txt", "r", encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split("-")
        sonastik[k.strip()] = v.strip()
        file=open("vastus.txt", "r", encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split("-")
        sonastik2[v.strip()] = k.strip()
        file=open("vastus.txt", "r", encoding="utf-8-sig")
    nimi=input("kirjuta siinu eesnimi ja perenimi ")
    menu=int(input(f"{nimi} mida te tahate, \n1-test \n2-valja"))
    if menu==1:
        koik=test(sonastik,sonastik2,nimi,koik)
    if menu==2:
        break
    if menu==3:
        sorter(koik,eisoobi,vastuvoetud,"koik.txt")
    #except:
    #    print("viga")



