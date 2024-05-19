from address import Address
from mailing import Mailing

to_address = Address('111024','Москва', 'Душинская', '16', '25')
from_address = Address('122445', 'Уфа', 'Проспект октября', '15', '56')
Mailing = Mailing(to_address, from_address, 1234, 'Коробка 500гр')

print(f"Отправление {Mailing.track} из {Mailing.from_address.index}, {Mailing.from_address.Sity,}"
      f"{Mailing.from_address.street}, {Mailing.from_address.house} - {Mailing.from_address.apartment}"
      f"{Mailing.to_address.index}, {Mailing.to_address.Sity}, {Mailing.to_address.street}, {Mailing.to_address.house} - {Mailing.to_address.apartment}"
      f"Стоимость {Mailing.Cots} Рублей")