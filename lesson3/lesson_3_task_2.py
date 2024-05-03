from  Smartphone import  smartphone
Catalog = []
phone1 = smartphone('samsung', 'A 54 5G', '+7 999 999 99 99')
phone2 = smartphone('samsung', 'S 24 ULTRA', '+7 888 888 88 88')
phone3 = smartphone('Xiaoni', '9 PRO', '+7 777 777 77 77')
phone4 = smartphone('Realmi', '12 Ligt', '+7 666 666 66 66')
phone5 = smartphone('Ipnone', '15 RPO MAX', '+7 555 555 55 55')

Catalog.append(phone1)
Catalog.append(phone2)
Catalog.append(phone3)
Catalog.append(phone4)
Catalog.append(phone5)

for phone in Catalog:
    print( f"{phone.Brand} - {phone.model}, {phone.phonenumber} " )
