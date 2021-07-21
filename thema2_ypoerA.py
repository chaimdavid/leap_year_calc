protein_name=str(input('Submit protein name: '))
protein_disc_date=int(input('Submit year of discovery: '))
print(protein_name,'has been known for',((2020-protein_disc_date+1)*365*24),'hours')
if ((protein_disc_date%4)==0)and(protein_disc_date%100!=0)or(protein_disc_date%400==0):
	print ('The discovery year of',protein_name,'is leap')
else:
	print ('The discovery year of',protein_name,'is not leap')
 
