#odredivanje prijestupne godine

godina = int(input('Unesite godinu: '))
if godina%4==0:
	print ('Godina',godina, 'je prijestupna') 
else :
	print ('Godina', godina,'nije prijestupna')

#izracunavanje koliko je dana proslo od datuma do datuma


print('Unesite prvi datum')
d1=int(input('Dan: '))
m1=int(input('Mjesec: '))
g1=int(input('Godina: '))

print ('Unesite drugi datum')
dan2=int(input('Dan:'))
mj2=int(input('Mjesec: '))
god2=int(input('Godina'))

mj1=(m1+9)%12
god1=g1-m1//10

mjesec2=(mj2+9)%12
godina2=god2-mj2//10

n1=365*god1+god1//4-god1//400+(mj1*306+5)//10+d1-1
n2=365*godina2+godina2//4-godina2//400+(mjesec2*306+5)//10+dan2-1

n=n2-n1

print ('Broj dana izmedu datuma: ',d1,'.',m1,'.',g1,' i datuma: ',dan2,'.',mj2,'.',god2,' je ',n)

#igra- pogodi broj
import random
max_pokusaja=5
print ('\nIgra pogadanja broja')
max_br=int(input('Unesite maksimalni broj: '))
print ('Pokusajte pogoditi broj od 1 do',max_br,' u',max_pokusaja,'pokusaja')

broj=random.randrange(1,max_br)
br=0
while True:
	br+=1
	pokusaj=int(input('\nPokusajte pogoditi broj:'))
	if pokusaj==broj:
		print('Cestitam, pogodili ste broj!')
		break
	elif pokusaj>broj:
		print ('Upisani broj je veci od trazenog')
	else: 
		print ('Upisani broj je manji od trazenog')
	if br==max_pokusaja:
		print ('Nazalost niste uspjeli pogoditi broj', broj, 'u', max_pokusaja,'pokusaja')
		break
print ('Hvala na igri!')

#izracun BMI

tezina=float(input('Unesite svoju tezinu: '))
visina=float(input('Unesite svoju visinu(u metrima): '))

BMI=tezina/(visina**2)

if (BMI<18.5):
	print ('Vas BMI je',BMI,' i vi ste podhranjeni!')
elif(BMI>25):
	print('Vas BMI je',BMI, ' i vi ste pretili!')
else : print('Vas BMI je',BMI,' i imate normalnu tjelesnu tezinu!')




