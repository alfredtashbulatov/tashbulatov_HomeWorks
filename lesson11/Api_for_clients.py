import requests
import allure

class Api:
    
    def __init__(self, url) -> None:
        self.url = url
# aвторизация
    @allure.step("api. Выполнить авторизацию {user}:{password}")
    def auth(self, user='raphael', password='cool-but-crude'):
        creds = {
            "username": user,
            "password": password
        }   
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"] 

    @allure.step("Api. Получить токен авторизации")
    def x_client_token(self):
        token = {}
        token["x-client-token"] = self.auth()
        return  token

 # получение списка компаний
    @allure.step("Api. Получить список всех компаний")
    def take_list_company(self, params_to_add=None):
        resp = requests.get(self.url + "/company")
        return resp.json() 
    
# добавление новой компании
    @allure.step("Api. Добавление новой компании {name}:{description}")
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        token = self.x_client_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=token)
        return resp.json()

# получение конкретной компании
    @allure.step("Api. Получить компанию по {new_id}")
    def search_company_by_id(self, new_id):
        token = self.x_client_token()
        resp = requests.get(self.url + "/company/"+ str(new_id), headers=token)
        return resp.json()

# изменение компании
    @allure.step("Api. Редактирование данных компании {new_id}:{new_name}:{new_descr}")
    def edit_info_conpany(self, new_id, new_name, new_descr):
        token = self.x_client_token()
        new_company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + "/company/"+ str(new_id), headers=token, json=new_company)
        return resp.json()
    
# удаление компании
    def delete_company(self, id):
        token = self.x_client_token()
        resp = requests.delete(self.url + "/company/delete/" + str(id),headers=token)
        return resp.json()
    
# активация компании
    @allure.step("Api. Aктивировать компаниюю {id}:{isActive}")
    def control_company(self, id, isActive):
        token = self.x_client_token()
        resp = requests.patch(self.url + "/company/status/" + str(id), headers=token, json={"isActive": isActive})
        return resp.json()
    
# получить список сотрудников для компании
    @allure.step("Api. Получить список сотрудников для компании{id}")
    def employee_list_company(self, id):
        token = self.x_client_token()
        resp = requests.get(self.url + "/employee"+ str(id), headers=token)
        return resp.json()

# добавление сотрудника 
    @allure.step("Api. Добавление сотрудника{new_id}:{firstName}:{lastName}:{phone}")
    def add_employee(self, new_id, firstName, lastName, phone):
        data_empl = {
            "id": 1111,
            "firstName": firstName,
            "lastName": lastName,
            "middleName":  None,
            "companyId": new_id,
            "email": None,
            "url": None,
            "phone": phone,
            "birthdate": None,
            "isActive": True
            }
        token = self.x_client_token()
        resp = requests.post(self.url + "/employee",  headers=token, json=data_empl)
        return resp.json()
    
# поиск сотрудника по id
    @allure.step("Api. Поиск сотрудника по {id}")
    def search_employee_by_id(self, id):
        token = self.x_client_token()
        resp = requests.get(self.url + "/employee/" + str(id), headers=token)
        return resp.json()
    
# изменить информацию о сотруднике 
    @allure.step("Api. Изменение данных сотрудника{id}:{new_name}:{new_mail}:{new_phone}:{isActive}")
    def edit_info_employee(self, id, new_name, new_mail, new_phone, isActive):
        edit_emp =  {
            "lastName": new_name,
            "email": new_mail,
            "url": None,
            "phone": new_phone,
            "isActive": isActive
            }   
        token = self.x_client_token()
        resp = requests.patch(self.url + "/employee/" + str(id), headers=token, json=edit_emp)
        return resp.json()
