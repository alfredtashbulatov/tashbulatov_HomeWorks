from  smartphone import  Smartphone
catalog = []
phone1 = Smartphone('samsung', 'A 54 5G', '+7 999 999 99 99')
phone2 = Smartphone('samsung', 'S 24 ULTRA', '+7 888 888 88 88')
phone3 = Smartphone('Xiaoni', '9 PRO', '+7 777 777 77 77')
phone4 = Smartphone('Realmi', '12 Ligt', '+7 666 666 66 66')
phone5 = Smartphone('Ipnone', '15 RPO MAX', '+7 555 555 55 55')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print( f"{phone.brand} - {phone.model}, {phone.phone_number} " )