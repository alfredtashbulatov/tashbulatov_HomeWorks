from sqlalchemy import create_engine
import requests
import allure
from sqlalchemy.sql import text
import sqlite3
from sqlalchemy import Text
class CompanyTable:

    __scripts = {
        "select": "select * from company where deleted_at is null",
        "select employee": text("select * from employee where id =:c_id"),
        "select only active": "select * from company where \"is_active\" = true  and deleted_at is null",
        "delete by id": text("delete from company where id =:id_to_delete"),
        "delete employee": text("delete from employee where id =:id_to_delete"),
        "insert new": text("insert into company(\"name\") values (:new_name)"),
        "get new id": "select MAX(\"id\") from company where deleted_at is null",
        "get new e": text("select MAX(\"id\") from employee where company_id =:c_id"),
        "update employee" : text('update employee set first_name =:f_name where id =:emp_id'),
        "get new employee" : text(
            'insert into employee (company_id, first_name, last_name, phone) values (:c_id, :f_name, :l_name, :ph)')
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)


    @allure.step("DB. Получение списка компаний")
    def get_companies(self):
        request = self.__db.execute(self.__scripts["select"])
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall()
        
    @allure.step("DB. Создание компании{name}")
    def create_compayny(self, name):
        request = self.__db.execute(self.__scripts["insert new"], new_name = name)
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall

    @allure.step("DB. Получение списка активных компаний")
    def get_active_companies(self):
        request = self.__db.execute(self.__scripts["select only active"])
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall
    

    @allure.step("DB. Удаление компании{id}")
    def delete_company(self, id:int):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete=id)


    @allure.step("DB. Получение максимального значения ID")
    def search_max_id(self):
        request =  self.__db.execute(self.__scripts["get new id"])
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall()[0][0] 

    @allure.step("DB. Получение списка сотрудников{id}")
    def get_employee(self, id:int):
        self.__db.execute(self.__scripts["select employee"], c_id=id)

    @allure.step("DB. Получение максимального значения ID сотрудника{company_id}")
    def search_max_id_emp(self, company_id: int):
        request = self.__db.execute(self.__scripts["get new e"], c_id=company_id)
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall()[0][0] 

    @allure.step("DB. Добавление нового сотрудника{company_id}: {first_name}:{last_na}:{phone}")
    def add_new_employee(self, company_id: int, first_name: str, last_name: str, phone: str):
        request = self.__db.execute(self.__scripts["get new employee"],
                                 c_id=company_id, 
                                 f_name=first_name, 
                                 l_name=last_name, 
                                 ph=phone)
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall
  
    @allure.step("DB. Удаление сотрудника{id}")
    def delete_employee(self, id):
        request = self.__db.execute(self.__scripts["delete employee"], id_to_delete=id)
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request

    @allure.step("DB. Поиск сотрудника по {id}")
    def search_employee_by_id(self, id):
        self.__db.execute(self.__scripts["select employee"], emp_id=id)

    @allure.step("DB. Изменение информации сотрудника{first_name}:{id}")
    def update_employee(self, first_name:str, id:int):
        request = self.__db.execute(self.__scripts["update employee"],f_name=first_name,
                           emp_id=id)
        allure.attach(str(request.context.cursor.request), 'SQL', allure.attachment_type.TEXT)
        return request.fetchall