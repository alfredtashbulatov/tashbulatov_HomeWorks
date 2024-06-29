from Clients_method import Api
from db import CompanyTable
import requests
import pytest
api = Api("https://x-clients-be.onrender.com")
db = CompanyTable("postgres://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# сооздание компании
def test_add_new_company():
    name = "alfred"
    res= db.create_compayny(name)
    new_id = db.search_max_id()
    body = api.take_list_company()
    db.delete_company(new_id)

    assert body[-1]["name"] == name
    assert body[-1]["id"] == new_id

# поиск компании по id
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
def test_diactivate_and_activate():
    name = "bravo"
    db.create_compayny(name)
    new_id = db.search_max_id()
    api.control_company(new_id, False)
    res = api.control_company(new_id, True)
    db.delete_company(new_id)
    assert res["isActive"] == True 

# получение списка компаний 
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

# удаление компании
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

# добавление сотрудника 
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

# поиск компании по id
def test_search_company():
    name = "coffe"
    db.create_compayny(name)
    new_id = db.search_max_id()
    res = api.search_company_by_id(new_id)
    db.delete_company(new_id)

    assert res["id"] == new_id
    assert res["name"] == name
    assert res["isActive"] == True

# диактивация компании
def test_diactivate_and_activate():
    name = "bravo"
    db.create_compayny(name)
    new_id = db.search_max_id()
    api.control_company(new_id, False)
    res = api.control_company(new_id, True)
    db.delete_company(new_id)
    assert res["isActive"] == True

# добавление сотрудника
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

# получение списка сотрудников 
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

# получение сотрудника по id 
def test_search_employee_by_id():
    name = "rolldol"
    f_Name = "tom"
    l_Name = "ford"
    ph = "9 999 999 99 99"

    db.create_compayny(name)
    new_id = db.search_max_id()

    db.add_new_employee(new_id, f_Name, l_Name, ph)
    emp_id = db.search_max_id_emp(new_id)

    # db.search_employee_by_id(emp_id)

    db.delete_employee(emp_id)
    db.delete_company(new_id)

#редактирования сотрудника 
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