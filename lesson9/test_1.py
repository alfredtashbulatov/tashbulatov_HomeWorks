from Api_metod import Api
import allure 
from data_base import CompanyTable
import requests
import pytest
api = Api("https://x-clients-be.onrender.com")
db = CompanyTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# сооздание компании\
@allure.title("Создание компании")
@allure.description("Тест создает компанию, проверяет, что в списке компаний она отоброжаеться, после чего компания удаляется ")
def test_add_new_company():
    with allure.step("Задать название компании"):
        name = "alfred"
        with allure.step("Вызвать DB метод для создания компаниии"):
            res= db.create_compayny(name)
            with allure.step("Вызвать метод 'Поиск максимального ID' для поиска id новой компании" ):
                new_id = db.search_max_id()
    with allure.step("Вызвать API метод для получения списка компаний"):            
        body = api.take_list_company()
    with allure.step("вызвать DB метод удаления компании"):    
        db.delete_company(new_id)

    with allure.step("Сравнить название послкдней компании из списка c именем новой компании"):
        assert body[-1]["name"] == name
    with allure.step("Сравнить ID последней компании из списка с ID новой созданной компании"):
        assert body[-1]["id"] == new_id

# поиск компании по id
@allure.title("поиск компании по id")
def test_search_company():
    name = "coffe"
    db.create_compayny(name)
    new_id = db.search_max_id()
    res = api.search_company_by_id(new_id)
    db.delete_company(new_id)

    assert res["id"] == new_id
    assert res["name"] == name
    assert res["isActive"] == True    

# деактивация компании
@allure.title("Деактивация компании и активация компании")
def test_diactivate_and_activate():
    name = "bravo"
    db.create_compayny(name)
    new_id = db.search_max_id()
    api.control_company(new_id, False)
    res = api.control_company(new_id, True)
    db.delete_company(new_id)
    assert res["isActive"] == True 

# получение списка компаний 
@allure.title("Получение списка компаний")
def test_employee_list_company_db():
    name = "rolldol"
    desc = "ikra"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"
    res = api.create_company(name, desc)
    new_id = res["id"]
    resp = api.add_employee(new_id, f_Name, l_Name, ph)
    e_id = resp["id"]
    result = db.get_employee(new_id)

    db.delete_employee(e_id)
    db.delete_company(new_id) 

# Удаление компании
@allure.title("Удаление компании")
def test_delete_comp():
    name = "ruderius"
    desc = "labirint-cyti"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"
    res= api.create_company(name, desc)
    new_id = res["id"]
    c_id = res["id"]
    resp = api.add_employee(c_id, f_Name, l_Name, ph)
    emp_id = resp["id"]
    db.delete_employee(emp_id)
    db.delete_company(new_id)  

# Добавление сотрудника 
@allure.title("Добавление сотрудника")
def test_add_employe_in_company():
    name = "test mp3"
    desc = "nwe rosk"
    firstName = "vadik"
    lastName = "shageev"
    phone = "9 999 999 99 99"
    res = api.create_company(name, desc)
    new_id = res["id"]
    resp = api.add_employee(new_id, firstName, lastName, phone)
    emp_id = resp["id"]
    assert new_id == res["id"]
    assert emp_id == resp['id']    

# Поиск компании по id
@allure.title("Поиск компании по id")
def test_search_company():
    name = "coffe"
    db.create_compayny(name)
    new_id = db.search_max_id()
    res = api.search_company_by_id(new_id)
    db.delete_company(new_id)

    assert res["id"] == new_id
    assert res["name"] == name
    assert res["isActive"] == True

# Диактивация компании
@allure.title("Диактивация компании")
def test_diactivate_and_activate():
    name = "bravo"
    db.create_compayny(name)
    new_id = db.search_max_id()
    api.control_company(new_id, False)
    res = api.control_company(new_id, True)
    db.delete_company(new_id)
    assert res["isActive"] == True

# Добавление сотрудника
@allure.title("Добавление сотрудника")
def test_add_employe():
    name = "test mp3"
    f_Name = "garick"
    l_Name = "okinava"
    ph = "9 999 999 99 99"
    db.create_compayny(name)
    new_id = db.search_max_id()
    db.add_new_employee(new_id, f_Name, l_Name, ph)
    emp_id = db.search_max_id_emp(new_id)
    db.delete_employee(emp_id)
    db.delete_company(new_id)

# Получение списка сотрудников 
@allure.title("Получение списка сотрудников")
def test_employee_list_company_db():
    name = "rolldol"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"
    db.create_compayny(name)
    new_id = db.search_max_id()
    resp = api.add_employee(new_id, f_Name, l_Name, ph)
    e_id = resp["id"]
    result = db.get_employee(new_id)

    db.delete_employee(e_id)
    db.delete_company(new_id)
    assert len(resp) > 0

# 2
@allure.title("Получение списка сотрудников (2 test)")
def test_employee_list_company_db():
    name = "rolldol"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"
    
    db.create_compayny(name)
    new_id = db.search_max_id()
    
    db.add_new_employee(new_id, f_Name, l_Name, ph)
    emp_id = db.search_max_id_emp(new_id)
    
    db.delete_employee(emp_id)
    db.delete_company(new_id)

# Получение сотрудника по id 
@allure.title("Получение сотрудника по id")
def test_search_employee_by_id():
    name = "rolldol"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"

    db.create_compayny(name)
    new_id = db.search_max_id()

    db.add_new_employee(new_id, f_Name, l_Name, ph)
    emp_id = db.search_max_id_emp(new_id)


    db.delete_employee(emp_id)
    db.delete_company(new_id)

#редактирования сотрудника 
@allure.title("редактирования сотрудника ")
def test_update_employee():
    name = "rolldol"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"

    db.create_compayny(name)
    new_id = db.search_max_id()

    db.add_new_employee(new_id, f_Name, l_Name, ph)
    emp_id = db.search_max_id_emp(new_id)


    new_name = "parebrick"
    db.update_employee(new_name, emp_id)

    db.delete_employee(emp_id)
    db.delete_company(new_id)        