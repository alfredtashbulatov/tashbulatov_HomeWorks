from Clients_method import metods
import requests
import pytest
metod = metods("https://x-clients-be.onrender.com")

# сооздание компании
def test_add_new_company():
    name = "alfred"
    desc = "tashbulatov"
    res= metod.create_company(name, desc)
    new_id = res["id"]

    body = metod.take_list_company()

    assert body[-1]["name"] == name
    assert body[-1]["description"] == desc
    assert body[-1]["id"] == new_id

# удаление компании
def test_edit_company():
    name = "australia"
    desc = "kingguru"
    res= metod.create_company(name, desc)
    new_id = res["id"]

    new_name = "big"
    new_desr = "boss"
    edit = metod.edit_info_conpany(new_id, new_name, new_desr)
    assert edit["id"] == new_id
    assert edit["name"] == new_name
    assert edit["description"] == new_desr

# поиск конкретной компании
def test_search_company_dy_id():
    name = "ruderius"
    desc = "labirint-cyti"
    res= metod.create_company(name, desc)
    new_id = res["id"]
    result = metod.search_company_by_id(new_id)
    assert result["name"] == "ruderius"

# деактивация компании
def test_diactivate_company():
    name = "ruderius"
    desc = "labirint-cyti"
    res= metod.create_company(name, desc)
    new_id = res["id"]
    result = metod.control_company(new_id, False)
    assert result["isActive"] == False

# получение списка сотрудников 
def test_employee_list_company():
    body = metod.take_list_company()
    id = body[-1]["id"]
    res = metod.employee_list_company(id)

    
# добавление сотрудника 
def test_add_employe():
    name = "alik"
    desc = "tashbulatov"
    res = metod.create_company(name, desc)
    new_id = res["id"]
    resp = metod.add_employee(new_id)
    emp_id = resp["id"]
    assert new_id == res["id"]
    assert emp_id == resp['id']
    

    # поиск сотрудника по id

def test_search_employee_by_id():
    # получим список компаний 
    body = metod.take_list_company()
    id = body[0]["id"]
    # получим список сотрудников для компании
    resp = metod.employee_list_company(id)
    emp_id = resp["id"]
    result = metod.search_employee_by_id(emp_id)
    # r = result["id"]
    # assert r == emp_id
    

    
# смоук тетс добавление сотрудниа в компанию
def test_smoyk_add_employee():
    name = "new company"
    desc = ""
    res= metod.create_company(name, desc)
    new_id = res["id"]
    # создаем сотрудника 
    resp = metod.add_employee(new_id)
    emp_id = resp["id"]
    result = metod.search_employee_by_id(emp_id)



