from Api_for_clients import Api
from data_base_for_clients import CompanyTable
import requests
import sqlalchemy
import postgres
import pytest
import allure
api = Api("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("CREATE")
@allure.title("Добавление новой компании")
@allure.description("Тест создает компанию, с параметром name = 'Технология-Света'")
def test_add_new_company():
    with allure.step("Создать компанию"):
        with allure.step("Задать название компании"):
            name = "'Технология-Света'"
        with allure.step("Вызвать DB-метод для создания компании"):
            db.create_compayny(name)
            with allure.step("Получить Id новой компании"):
                with allure.step("Вызвать DB-метод, для получения максимального id"):
                    new_id = db.search_max_id()
        
        with allure.step("Получить список компаний"):
            with allure.step("Вызвать api-метод, для получения списка компаний"):
                body = api.take_list_company()

        with allure.step("Удалить из БД созданную компанию"):
            with allure.step("Вызвать DB-метод, для удаления компании"):
                db.delete_company(new_id)

        with allure.step("ВЫполнить проверки"):
            with allure.step("Проверить, что имя последней организации из списка\
                              равна имени созданной организации"):
                assert body[-1]["name"] == name
            with allure.step("Проверить, что Id последней организации из списка\
                             равна id созданной организации"):
                assert body[-1]["id"] == new_id

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("SEARCH")
@allure.title("Поиск помпании по id")
@allure.description("Тест создает компанию с парамеетром name = Max motion, \
                     выполняет ее поиск по полученному id")
def test_search_company():
    with allure.step("Создать компанию"):
        with allure.step("Задать название компании"):
            name = " Max motion"
        with allure.step("Вызвать DB-метод, для создания компании"):
            db.create_compayny(name)
            with allure.step("Получить Id новой компании"):
                with allure.step("Вызвать DB-метод, для получения максимального id"):
                    new_id = db.search_max_id()
        with allure.step("Поиск компании по id"):
            with allure.step("Вызвать Api-метод, для получения компании по id"):
                res = api.search_company_by_id(new_id)
        with allure.step("Удалить из БД созданную компанию"):
            with allure.step("Вызвать DB-метод, для удаления компании"):
                db.delete_company(new_id)

        with allure.step("ВЫполнить проверки"):
            with allure.step("Проверить, что id полученной компании равна id созданной компании"):        
                assert res["id"] == new_id
            with allure.step("Проверить, что название полученной компании равна названию созданной компании"):
                assert res["name"] == name
            with allure.step("Проверить, что параметр 'isActive' полученной компании равна 'True"):
                assert res["isActive"] == True    

@allure.severity(allure.severity_level.BLOCKER)
@allure.feature("CONTROL ACTIVATE")
@allure.title("деаетивация и активация компании")
@allure.description("Тест создает компанию с параметром name = aura extra,\
                    деактивирует затем активирует созданную компанию")
def test_diactivate_and_activate():
    with allure.step("Создать компанию"):
        with allure.step("Задать название компании"):
            name = "aura extra"
        with allure.step(""):
            db.create_compayny(name)
            with allure.step("Получить Id новой компании"):
                with allure.step("Вызвать DB-метод, для получения максимального id"):
                    new_id = db.search_max_id()
        
        with allure.step("Деактивировать и активировать компанию"):
            with allure.step("Вызвать Api-метод с параметром 'isActive = False'"):
                api.control_company(new_id, False)
            with allure.step("Вызвать Api-метод с параметром 'isActive = True'"):
                res = api.control_company(new_id, True)

        with allure.step("Удалить из БД созданную компанию"):
            with allure.step("Вызвать DB-метод, для удаления компании"):
                db.delete_company(new_id)
        
        with allure.step("ВЫполнить проверки"):
            with allure.step("Проверить, что параметр 'isActive' полученной компании равна 'True"):
                assert res["isActive"] == True 

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("CREATE")
@allure.title("Добавление сотрудника")
@allure.description("Тест создает компанию с параметрами: 'name = КАМФЛОТ',  'description = Грузоперевозки по реке Каме.\
                    Добавляет в него сотрудника с параметрами: 'first_name = Данила', last_name = Сакерин,\
                    'phone = 9 999 999 99 99'.")
def test_add_employe_in_company():
    with allure.step("Создать компанию"):
        with allure.step("Задать данные компании"):
            name = "КАМФЛОТ"
            desc = "Грузоперевозки по реке Каме"
        with allure.step("Вызвать Api-метод, для создания компании"):
            res = api.create_company(name, desc)
            new_id = res["id"]
        
        with allure.step("Добавление сотрудника"):
            with allure.step("Задать данные для сотрудника"):
                firstName = "Данила"
                lastName = "Сакерин"
                phone = "9 999 999 99 99"
            with allure.step("Вызвать Api-метод для создания сотрудника"):
                resp = api.add_employee(new_id, firstName, lastName, phone)
                emp_id = resp["id"]

        with allure.step("Выполнить проверки"):
            with allure.step("Проверить, что записанный id равен id созданной компании"):
                assert new_id == res["id"]
            with allure.step("Проверить, что записанный id равен id добавленного сотрудника"):
                assert emp_id == resp['id']  

@allure.severity(allure.severity_level.NORMAL)
@allure.feature("SEARCH LIST EMPLOYEE")
@allure.title("Получение списка сотрудников для компании")
@allure.description("Тест создает компанию с параметрами: 'name = Везем',  'description = Быстрая доставка от 15 минут'.\
                    Добавляет в него сотрудника с параметрами: 'first_name = Владимир', last_name = Борисов,\
                    'phone = 9 999 999 99 99'. Получает список сотрудников для компании.")
def test_employee_list_company_db():
    with allure.step("Создать компанию"):
        with allure.step("Задать данные компании"):
            name = "Везем"
            desc = "Быстрая доставка от 15 минут"
        with allure.step("Вызвать Api-метод, для создания компании"):
            res = api.create_company(name, desc)
            new_id = res["id"]

        with allure.step("Добавление сотрудника"):
            with allure.step("Задать данные для сотрудника"):
                f_Name = "Владимир"
                l_Name = "ford"
                ph = "9 999 999 99 99"
            with allure.step("Вызвать Api-метод для создания сотрудника"):
                resp = api.add_employee(new_id, f_Name, l_Name, ph)            
                e_id = resp["id"]
    
        with allure.step("Получения списка сотрудников для компании"):
            with allure.step("Вызвать DB-метод, для получения списка сотрудников в компании"):
                result = db.get_employee(new_id)

        with allure.step("Удаление сотрудника и компании"):
            with allure.step("Вызвать DB-метод, для удаления сотрудника из БД"):
                db.delete_employee(e_id)

            with allure.step("Вызвать DB-метод, для удаления компании из БД"):
                db.delete_company(new_id) 

@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("UPDATE EMPLOYEE")
@allure.title("Редактирование данных сотрудника")
@allure.description("Тест создает компанию с параметрами: 'name = ГК Самолет'.\
                    Добавляет в него сотрудника с параметрами: 'first_name = Михаил', last_name = Голованов,\
                    'phone = 9 999 999 99 99'. Получает список сотрудников для компании")
def test_update_employee():
    with allure.step("Создать компанию"):
        with allure.step("Задать название компании"):
            name = "ГК Самолет"
        with allure.step("Вызвать DB-метод, для создания компании"):
            db.create_compayny(name)
        with allure.step("Вызвать DB-метод, для получения id созданной компании"):
            new_id = db.search_max_id()

        with allure.step("Добавление сотрудника"):
            with allure.step("Задать данные для сотрудника"):
                f_Name = "Михаил'"
                l_Name = "Голованов"
                ph = "9 999 999 99 99"
            with allure.step("Вызвать DB-метод для добавления сотрудника"):
                db.add_new_employee(new_id, f_Name, l_Name, ph)
            with allure.step("Вызвать DB-метод, для получения id добавленного сотрудника"):
                emp_id = db.search_max_id_emp(new_id)

        with allure.step("Редактирование сотрудника"):
            with allure.step("Задать новые данные для сотрудника"):
                new_name = "parebrick"
            with allure.step("Вызвать DB-метод для редактирования сотрудника"):
                db.update_employee(new_name, emp_id)

        with allure.step("Удаление сотрудника и компании"):
            with allure.step("Вызвать DB-метод, для удаления сотрудника из БД"):
                db.delete_employee(emp_id)
            with allure.step("Вызвать DB-метод, для удаления компании из БД"):
                db.delete_company(new_id)        


@allure.feature("SEARCH EMPLOYEE")
@allure.title("Получение сотрудника id")
@allure.description("Тест создает компанию с параметрами: 'name = (ПАО) ВТБ'.\
                    Добавляет в него сотрудника с параметрами: 'first_name = Александр', last_name = Киселев,\
                    'phone = 9 999 999 99 99'. Получает список сотрудников для компании")
@allure.severity(allure.severity_level.NORMAL)
def test_search_employee_by_id():
    with allure.step("Создать компанию"):
        with allure.step("Задать название компании"):
            name = "(ПАО) ВТБ"
        with allure.step("Вызвать DB-метод, для создания компании"):
            db.create_compayny(name)
        with allure.step("Вызвать DB-метод, для получения id созданной компании"):
            new_id = db.search_max_id()

        with allure.step("Добавление сотрудника"):
            with allure.step("Задать данные для сотрудника"):
                f_Name = "Александр"
                l_Name = "Киселев"
                ph = "9 999 999 99 99"
            with allure.step("Вызвать DB-метод для добавления сотрудника"):
                db.add_new_employee(new_id, f_Name, l_Name, ph)
            with allure.step("Вызвать DB-метод, для получения id добавленного сотрудника"):
                emp_id = db.search_max_id_emp(new_id)

        with allure.step("Удаление сотрудника и компании"):
            with allure.step("Вызвать DB-метод, для удаления сотрудника из БД"):
                db.delete_employee(emp_id)
            with allure.step("Вызвать DB-метод, для удаления компании из БД"):
                db.delete_company(new_id)
