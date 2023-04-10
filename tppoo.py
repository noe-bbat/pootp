import math
import random
from abc import abstractmethod


''' 頑張る'''

class Personnage:
	#@abstractmethod
	nom_possibles=['Sigurd','Jack Givre','Alex Eagleston','Ky','Dejiko','Le gentil San Gohan','Lancelot','Sylvain','Abel','Freddy Fazbear','Simon','Arturia','Shizuka','Maria','Asuka','Amaterasu','Amuro']
	def __init__(self,nom='Nameless',pv=300):
		#Personnage.cptp+=1
		if nom=="Nameless":
			self.__nom = Personnage.nom_possibles[random.randint(0,15)] #le personnage obtient le cpt ieme nom de la liste
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
		self.__point_atk=point_atk+Guerrier.boost_atk
	@property
	def point_atk(self):
		return self.__point_atk
	def attaquer(self,atk,vie):
		return(vie-atk)
		
	
class Paladin(Personnage,Attaque,Soin):
	def __init__(self,nom='Nameless',pv=300,point_atk=30,point_soin=25):
		Personnage.__init__(self,pv,nom)
		self.__point_atk=point_atk
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
			self.__point_soin=point_soin+Soigneur.boost_soin
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
	def __init__(self,pv=300,nom='Nameless',point_atk=30):
		Guerrier.__init__(self,pv,nom,point_atk)
		self.__point_atk=point_atk+boost_barbare
		self.__pv=pv-malus_barbare
	
	
class General(Guerrier):
	boost_general=30
	malus_general=15
	def __init__(self,nom='Nameless',pv=300,point_atk=30):
		Guerrier.__init__(self,pv,nom,point_atk)
		self.__point_atk=point_atk-malus_general
		self.__pv=pv+boost_general
	
class Soldat(Guerrier):
	def __init__(self,nom='Nameless',pv=300,point_atk=30):
		Guerrier.__init__(self,pv,nom,point_atk)
		
	
class Chevalier_Sacre(Paladin):
	malus_sacre=15
	bonus_force_sacre=15
	bonus_vie_sacre=50
	def __init__(self,nom='Nameless',pv=300,point_atk=30,point_soin=25):
		Paladin.__init__(self,pv,nom,point_atk,point_soin)
		self.__point_atk=point_atk+bonus_force_sacre
		self.__pv=pv+bonus_vie_sacre
		self.__point_soin=point_soin-malus_sacre
	
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
		self.__point_atk=point_atk+bonus_force_gry
		self.__pv=pv-malus_pv_gry
		self.__point_soin=point_soin+bonus_soin_gry
	
class Pretre(Soigneur):
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Soigneur.__init__(self,pv,nom,point_soin)
		
	
class Chamane(Soigneur):
	bonus_vie_chamane=25
	malus_soin_cha=10
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Soigneur.__init__(self,pv,nom,point_soin)
		self.__point_soin=point_soin-malus_soin_cha
		self.__pv=pv+bonus_vie_chamane
	
	
class Mage_Blanc(Soigneur):
	bonus_soin_blanc=30
	malus_pv_blanc=25
	def __init__(self,nom='Nameless',pv=300,point_soin=25):
		Soigneur.__init__(self,pv,nom,point_soin)
		self.__point_soin=point_soin+Mage_Blanc.bonus_soin_blanc
		self.__pv=pv-Mage_Blanc.malus_pv_blanc

if __name__ == '__main__':
	MB = Mage_Blanc()
	SL= Soldat()
	MN= Moine()
	SL.all_info()
	print("Le personnage s'appelle "+str(MN.nom)+" et a "+str(MN.pv)+" pv")
	#print(MB.nom+" fera face à "+MN.nom)
	#print(MN.nom+" a "+str(MN.point_atk)+" point d'attaque")
	#SL.attaquer(SL.point_atk,MN.pv)
	MN.healing(MB.soigner(MN.pv,MB.point_soin))
	#MN.prise_de_degat(SL.attaquer(SL.point_atk,MN.pv))
	#print(SL.nom+" a inflingé "+str(SL.point_atk)+" à "+MN.nom+" qui n'a plus que "+str(MN.pv)+" points de vie.")
	print(MB.nom+" a restauré "+str(MB.point_soin)+" à "+MN.nom+" qui a maintenant "+str(MN.pv)+" points de vie.")
