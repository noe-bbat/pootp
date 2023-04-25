import math
import random
from abc import abstractmethod
from tkinter import*
import tkinter as tk

''' 頑張る'''

class Personnage:
	#@abstractmethod
	nom_possibles=['Sigurd','Joueur du Grenier','Neco-Arc','Battler','Quoikoubaka','湯者様','Stéphane Plaza','Jack Givre','Alex Eagleston','Ky','Dejiko','Le gentil San Gohan','Lancelot','Sylvain','Abel','Freddy Fazbear','Simon','Arturia','Shizuka','Maria','Asuka','Amaterasu','Amuro']
	def __init__(self,nom='Nameless',pv=300):
		#Personnage.cptp+=1
		if nom=="Nameless":
			self.__nom = Personnage.nom_possibles[random.randint(0,21)] #le personnage obtient le cpt ieme nom de la liste
		else:
				self.__nom=nom
		if pv==300:
			self.__pv=pv+(random.randint(-25,30)) #donne un bonus/malus de vie aléatoire entre -25 et +30 pv
		else:
				self.__pv=pv
	@property
	def nom(self):
		return self.__nom
	@property
	def pv(self):
		return self.__pv	
	def sante(pv):
		return (pv>=0)
	
	def prise_de_degat(self,pv_restants):
		self.__pv=pv_restants
	def healing(self,pv_restaurés):
		self.__pv=pv_restaurés
	def all_info(self):
		informateur = vars(self)
		print(', '.join("%s: %s" % item for item in vars(self).items()))
		
class Attaque:
	@abstractmethod
	def attaquer(self,atk,vie):
		return(vie-atk)
	
	
class Soin:	
	@abstractmethod
	def soigner(self,pv,soin):
		return(vie+soin)

class Guerrier(Personnage,Attaque):
	boost_atk=25
	def __init__(self,nom='Nameless',pv=300,point_atk=40):
		Personnage.__init__(self,pv,nom)
		if point_atk==40:
			self.__point_atk=point_atk+Guerrier.boost_atk+(random.randint(-9,9))
		else:
			self.__point_atk=point_atk+Guerrier.boost_atk
	@property
	def point_atk(self):
		return self.__point_atk
	def attaquer(self,atk,vie):
		return(vie-atk)
		
	
class Paladin(Personnage,Attaque,Soin):
	def __init__(self,nom='Nameless',pv=300,point_atk=30,point_soin=25):
		Personnage.__init__(self,pv,nom)
		if point_atk==30:
			self.__point_atk=point_atk+(random.randint(-5,5))
		else:
			self.__point_atk=point_atk
		if point_soin==25:
			self.__point_soin=point_soin+(random.randint(-5,5))
		else:
			self.__point_soin=point_soin
	@property
	def point_atk(self):
		return self.__point_atk
	@property
	def point_soin(self):
		return self.__point_soin
	def attaquer(self,atk,vie):
		return(vie-atk)
	def soigner(self,pv,soin):
		return(pv+soin)
	
class Soigneur(Personnage,Soin):
	boost_soin=25
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Personnage.__init__(self,pv,nom)
		if point_soin==25:
			self.__point_soin=point_soin+Soigneur.boost_soin+(random.randint(-9,9))
		else:
			self.__point_soin=point_soin
	@property
	def point_soin(self):
		return self.__point_soin
	def soigner(self,pv,soin):
		return(pv+soin)

class Barbare(Guerrier):
	boost_barbare=25
	malus_barbare=30
	def __init__(self,pv=300,nom='Nameless',point_atk=40):
		Guerrier.__init__(self,pv,nom,point_atk)
		self.__point_atk=point_atk+Barbare.boost_barbare
		self.__pv=pv-Barbare.malus_barbare
	
	
class General(Guerrier):
	boost_general=30
	malus_general=15
	def __init__(self,nom='Nameless',pv=300,point_atk=40):
		Guerrier.__init__(self,pv,nom,point_atk)
		self.__point_atk=point_atk-General.malus_general
		self.__pv=pv+General.boost_general
	
class Soldat(Guerrier):
	def __init__(self,nom='Nameless',pv=300,point_atk=40):
		Guerrier.__init__(self,pv,nom,point_atk)
		
	
class Chevalier_Sacre(Paladin):
	malus_sacre=15
	bonus_force_sacre=15
	bonus_vie_sacre=50
	def __init__(self,nom='Nameless',pv=300,point_atk=30,point_soin=25):
		Paladin.__init__(self,pv,nom,point_atk,point_soin)
		self.__point_atk=point_atk+Chevalier_Sacre.bonus_force_sacre
		self.__pv=pv+Chevalier_Sacre.bonus_vie_sacre
		self.__point_soin=point_soin-Chevalier_Sacre.malus_sacre
	
class Moine(Paladin):
	malus_force_moine=20
	bonus_vie_moine=20
	bonus_soin_moine=20
	def __init__(self,nom='Nameless',pv=300,point_atk=30,point_soin=25):
		Paladin.__init__(self,pv,nom,point_atk,point_soin)
		self.__point_atk=point_atk-Moine.malus_force_moine
		self.__pv=pv+Moine.bonus_vie_moine
		self.__point_soin=point_soin+Moine.bonus_soin_moine
	
class Chevalier_Gryffon(Paladin):
	bonus_force_gry=10
	bonus_soin_gry=10
	malus_pv_gry=10
	def __init__(self,nom='Nameless',pv=300,point_atk=30,point_soin=25):
		Paladin.__init__(self,pv,nom,point_atk,point_soin)
		self.__point_atk=point_atk+Chevalier_Gryffon.bonus_force_gry
		self.__pv=pv-Chevalier_Gryffon.malus_pv_gry
		self.__point_soin=point_soin+Chevalier_Gryffon.bonus_soin_gry
	
class Pretre(Soigneur):
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Soigneur.__init__(self,pv,nom,point_soin)
		
	
class Chamane(Soigneur):
	bonus_vie_chamane=25
	malus_soin_cha=10
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Soigneur.__init__(self,pv,nom,point_soin)
		self.__point_soin=point_soin-Chamane.malus_soin_cha
		self.__pv=pv+Chamane.bonus_vie_chamane
	
	
class Mage_Blanc(Soigneur):
	bonus_soin_blanc=30
	malus_pv_blanc=25
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Soigneur.__init__(self,pv,nom,point_soin)
		self.__point_soin=point_soin+Mage_Blanc.bonus_soin_blanc
		self.__pv=pv-Mage_Blanc.malus_pv_blanc
		
class Generation_Personnage(Mage_Blanc,Chamane,Barbare,Chevalier_Gryffon,Chevalier_Sacre,Pretre,Soldat,General,Moine):
	#Cette interface génère un personnage de façon aléatoire
	@abstractmethod
	def generation():
		sel=random.randint(1,9)
		if sel==1:
			MB = Mage_Blanc()
			return MB
		elif sel==2:
			SL= Soldat()
			return SL
		elif sel==3:
			GN=General()
			return GN
		elif sel==4:
			PR=Pretre()
			return PR
		elif sel==5:
			CS=Chevalier_Sacre()
			return CS
		elif sel==6:
			CG=Chevalier_Gryffon()
			return CG
		elif sel==7:
			BR=Barbare()
			return BR
		elif sel==8:
			MN= Moine()
			return MN
		elif sel==9:
			CH=Chamane()
			return CH
			
		
		
		

class Application(Generation_Personnage):
	#def __init__(self):
	#	tk.Tk.__init__(self)
     #   self.widgets()
	#def widgets(self):
		
	
	
	
	#Grid
	EnsembleCast={}
	DeckJ1={}
	DeckJ2={}
	prt = Tk()
	prt.geometry("600x400")
	 #création des deux listes
	Deck1= Label(prt,text="Deck joueur 1")
	Deck2= Label(prt,text="Deck joueur 2")
	BA = Button(prt, text = "Attaquer",)
	BS = Button(prt, text = "Soigner",)
	
	
	ListeJ1=Listbox(prt,height=10,width=20,bg="#e0d0a2",selectmode="SINGLE",fg="#210103",cursor="target",font="Arial",highlightcolor="#e0dfa2")
	def idUn(self,event):
		self.iun = event.ListeJ1.curselection()
	
	for i in range(1,31):
		EnsembleCast[i]=Generation_Personnage.generation()
	for i in range(1,11):
		DeckJ1[i]=EnsembleCast[random.randint(1,21)]
		ListeJ1.insert(i,DeckJ1[i].nom)
	
	ListeJ2=Listbox(prt,height=10,width=20,bg="#a4a2e0",selectmode="SINGLE",fg="#04011c",cursor="target",font="Arial",highlightcolor="#a4a9e0")
	for i in range(1,11):
		DeckJ2[i]=EnsembleCast[random.randint(1,21)]
		ListeJ2.insert(i,DeckJ2[i].nom)
	
	
	Deck1.grid(row = 0, column = 0, sticky = W, pady = 2)
	Deck2.grid(row = 0, column = 4, sticky = E, pady = 2)
	BA.grid(row = 0, column = 1, sticky = W, pady = 2)
	BS.grid(row = 1, column = 1, sticky = W, pady = 2)
	ListeJ1.grid(row=1, column=0,sticky = W, pady = 2)
	ListeJ2.grid(row=1, column=4,sticky = E, pady = 2)
	Decke1 = Label(prt,text=DeckJ1[1].nom+"( "+str(type(DeckJ1[1]).__name__)+" )"+": "+str(DeckJ1[1].pv)+" points de vie")
	Decke2 = Label(prt,text=DeckJ2[1].nom+"( "+str(type(DeckJ1[1]).__name__)+" )"+": "+str(DeckJ2[1].pv)+" points de vie")
	Decke1.grid(row = 4, column = 0, sticky = W, pady = 2)
	Decke2.grid(row = 4, column = 4, sticky = E, pady = 2)
	
	#ListeJ1.bind("<<ListboxSelect>>", self.idUn)

	prt.mainloop()



if __name__ == '__main__':
	MB = Mage_Blanc()
	SL= Soldat()
	MN= Moine()
	BR=Barbare()
	CH=Chamane()
	CG=Chevalier_Gryffon()
	CS=Chevalier_Sacre()
	PR=Pretre()
	GN=General()
	#SL.all_info()
	#print("Le personnage s'appelle "+str(MN.nom)+" et a "+str(MN.pv)+" pv")
	#print(MB.nom+" fera face à "+MN.nom)
	#print(MN.nom+" a "+str(MN.point_atk)+" point d'attaque")
	#SL.attaquer(SL.point_atk,MN.pv)
	#MN.healing(MB.soigner(GN.pv,MN.point_soin))
	#MN.prise_de_degat(SL.attaquer(SL.point_atk,MN.pv))
	#print(SL.nom+" a inflingé "+str(SL.point_atk)+" à "+MN.nom+" qui n'a plus que "+str(MN.pv)+" points de vie.")
	#print(MN.nom+" a restauré "+str(MN.point_soin)+" à "+GN.nom+" qui a maintenant "+str(GN.pv)+" points de vie.")
	'''i=0 ##incrément pour déterminér la durée de la partie
	while MB.sante and SL.sante and i<10:
		i=i+1;
		if i==1:
			print("La partie va commencer!")
			print(MB.nom+" contre "+GN.nom)
		MB.prise_de_degat(GN.attaquer(GN.point_atk,MB.pv))
		print(GN.nom+" a inflingé "+str(GN.point_atk)+" à "+MB.nom+" qui n'a plus que "+str(MB.pv)+" points de vie.")
		MB.healing(MB.soigner(MB.pv,MB.point_soin))
		print(MB.nom+" a restauré "+str(MB.point_soin)+" à "+MB.nom+" qui a maintenant "+str(MB.pv)+" points de vie.")
		if MB.pv<=0:
			print(MB.nom+" a perdu.")
		if GN.pv<=0 or i==10:
			print(GN.nom+" a perdu.")'''
	a=Application
		
		
