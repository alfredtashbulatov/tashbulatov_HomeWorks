import requests

class metods:
    
    def __init__(self, url) -> None:
        self.url = url
# aвторизация
    def auth(self, user='raphael', password='cool-but-crude'):
        creds = {
            "username": user,
            "password": password
        }   
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"] 

 # получение списка компаний
    def take_list_company(self, params_to_add=None):
        resp = requests.get(self.url + "/company")
        return resp.json() 
    
# добавление новой компании
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()

# получение конкретной компании
    def search_company_by_id(self, new_id):
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.get(self.url + "/company/"+ str(new_id), headers=my_headers)
        return resp.json()

# изменение компании
    def edit_info_conpany(self, new_id, new_name, new_descr):
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        new_company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url + "/company/"+ str(new_id), headers=my_headers, json=new_company)
        return resp.json()
    

# удаление компании
    def delete_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.get(self.url + "/company/delete/" + str(id),headers=my_headers)
        return resp.json()
    
# активация компании
    def control_company(self, id, isActive):
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.patch(self.url + "/company/status/" + str(id), headers=my_headers, json={"isActive": isActive})
        return resp.json()
    
# получить список сотрудников
    def employee_list_company(self, id):
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.get(self.url + "/employee", str(id), headers=my_headers)
        return resp.json()

# добавление сотрудника 
    def add_employee(self, new_id):
        data_empl = {
            "id": 1111,
            "firstName": "Alik",
            "lastName": "Drogin",
            "middleName": "Ashot",
            "companyId": new_id,
            "email": None,
            "url": None,
            "phone": "4 534 651 34 67",
            "birthdate": None,
            "isActive": True
            }
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.post(self.url + "/employee",  headers=my_headers, json=data_empl)
        return resp.json()
    
    # поиск сотрудника по id
    def search_employee_by_id(self, emp_id):
        my_headers = {}
        my_headers["x-client-token"] = self.auth()
        resp = requests.get(self.url + "/employee", json={"id": emp_id})
        return resp.json()
        
        
