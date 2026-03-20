def fonction(M,L,alpha,J) :
    return (M*L)/(alpha*J)
print(fonction(187.5,400,3,40.25))
def fonction2(N,x):
    return Longueur[N]/x * 40.25 #Ptit problème de calcul

Longueur = [200,400]
L = [187.5,375,562.5,750,937.5,1125,1312.5,1500]
A = [3,6,9,11.5,15,16.5,19,21]#pour 400mm
Laiton = [6,10,13,16,18,21,23,25]#pour 400mm
Acier = [0.5,1,1.5,2.5,4.5,5.5,6.5,7]#pour 400mm

Alu200 = [1,3.5,5,8,9.5,10,12,14]
Laiton200 = [5,9,10,11,13,15,17,19]
Acier200 = [0.0000000001,0.5,1,1.5,2.5,3,3.5,4]

Liste = []
#print(len(Acier))
#for i in range(8):
 #   print(fonction(L[i],400,A[i],40.25))
print("=====ALUMINIUM 400mm=====")
for i in range(8):
    #print(f"\n"+f"{A[i]/L[i]}")
    Liste.append(A[i]/L[i])
    
    #print(f"G = {fonction2(0,A[i]/L[i])}")
print(f"G = {fonction2(0,sum(Liste)/len(Liste))}")
print(f"Moyenne = {sum(Liste)/len(Liste)}")
Liste = []
print("====LAITON 400mm====")
for i in range(8):
    #print("\n"+f"{Laiton[i]/L[i]}")
    Liste.append(Laiton[i]/L[i])
    #print(f"G = {fonction2(0,Laiton[i]/L[i])}")
print(f"G = {fonction2(0,sum(Liste)/len(Liste))}")
print(f"Moyenne = {sum(Liste)/len(Liste)}")
Liste = []
print("====ACIER 400mm ====")
for i in range(8):
    #print("\n"+f"{Acier[i]/L[i]}")
    Liste.append(Acier[i]/L[i])
    #print(f"G = {fonction2(0,Acier[i]/L[i])}")
print(f"G = {fonction2(0,sum(Liste)/len(Liste))}")
print(f"Moyenne = {sum(Liste)/len(Liste)}")
Liste = []
print("====ALUMINIUM 200mm====")
for i in range(8):
    #print("\n"+f"{Alu200[i]/L[i]}")
    Liste.append(Alu200[i]/L[i])
    #print(f"G = {fonction2(1,Alu200[i]/L[i])}")
print(f"G = {fonction2(1,sum(Liste)/len(Liste))}")
print(f"Moyenne = {sum(Liste)/len(Liste)}")
Liste = []
print("====LAITON 200mm====")
for i in range(8):
    #print("\n"+f"{Laiton200[i]/L[i]}")
    Liste.append(Laiton200[i]/L[i])
    #print(f"G = {fonction2(1,Laiton200[i]/L[i])}")
print(f"G = {fonction2(1,sum(Liste)/len(Liste))}")
print(f"Moyenne = {sum(Liste)/len(Liste)}")
Liste = []
print("====ACIER 200mm====")
for i in range(8):
    #print("\n"+f"{Acier200[i]/L[i]}")
    Liste.append(Acier200[i]/L[i])
    #print(f"G = {fonction2(1,Acier200[i]/L[i])}")
#print(f"==== MOYENNE====")
print(f"Moyenne = {sum(Liste)/len(Liste)}")
print(f"G = {fonction2(1,sum(Liste)/len(Liste))}")
Liste = []