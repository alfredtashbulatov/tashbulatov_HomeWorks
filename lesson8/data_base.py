from sqlalchemy import create_engine 
import requests
from sqlalchemy.sql import text
import sqlite3
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
        # "update employee" : text('update employee set (first_name, id) where (:f_name, :emp_id)'),
        "update employee" : text('update employee set first_name =:f_name where id =:emp_id'),
        # "update employee" : text('update employee set (\"first_name\")(\"id\") where (:f_name, :emp_id)'),
        "get new employee" : text(
            'insert into employee (company_id, first_name, last_name, phone) values (:c_id, :f_name, :l_name, :ph)')
    }


    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

# получение компании
    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select only active"]).fetchall()
# удаление компании
    def delete_company(self, id:int):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete=id)
# сoздание компании
    def create_compayny(self, name):
        return self.__db.execute(self.__scripts["insert new"], new_name = name).fetchall
# поиск максимального id 
    def search_max_id(self):
        return self.__db.execute(self.__scripts["get new id"]).fetchall()[0][0] 


# получение списка сотрудников
    def get_employee(self, id:int):
        self.__db.execute(self.__scripts["select employee"], c_id=id)

#максимальное id для сотрудника  
    def search_max_id_emp(self, company_id: int):
        return self.__db.execute(self.__scripts["get new e"], c_id=company_id).fetchall()[0][0] 
    
# создание сотрудника 
    def add_new_employee(self, company_id: int, first_name: str, last_name: str, phone: str):
        return self.__db.execute(self.__scripts["get new employee"],
                                 c_id=company_id, 
                                 f_name=first_name, 
                                 l_name=last_name, 
                                 ph=phone
                                 ).fetchall
    
# удаление сотрудника    
    def dellete_employee(self, id):
        return self.__db.execute(self.__scripts["delete employee"], id_to_delete=id )
    
# получение сотрудника по id
    def search_employee_by_id(self, id):
        self.__db.execute(self.__scripts["select employee"], emp_id=id)

# редактирование сотрудника
    def update_employee(self, first_name:str, id:int):
        return self.__db.execute(self.__scripts["update employee"],f_name=first_name,
                           emp_id=id).fetchall

    