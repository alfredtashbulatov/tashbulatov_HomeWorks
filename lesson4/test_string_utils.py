import pytest
from stringUtils import StringUtils

stringUtils = StringUtils()

def capitilize(self, string: str) -> str:
    stringUtils = StringUtils()
    return string.capitalize()
def test_capitilize():
    assert StringUtils().capitilize("skypro") == "Skypro"
    assert StringUtils().capitilize("") == ""

def capitilize(self, string: str) -> str:
    stringUtils = StringUtils()
    return string.capitalize()
def test_nig_capitilize():
    assert StringUtils().capitilize("to day") == "today"
    assert StringUtils().capitilize("") == ""    


def trim(self, string: str) -> str:
    stringUtils = StringUtils()
    whitespace = " "
    while (string.startswith(whitespace)):
        string = string.removeprefix(whitespace)
    return string
def test_trim():
    assert StringUtils().trim("  today") == "today"
    assert StringUtils().trim("") == ""

def trim(self, string: str) -> str:
    stringUtils = StringUtils()
    whitespace = " "
    while (string.startswith(whitespace)):
        string = string.removeprefix(whitespace)
    return string
def test_nig_trim():
    assert StringUtils().trim("  to day") == "today"
    assert StringUtils().trim("") == ""


def to_list(self, string: str, delimeter = ",") -> list[str]:
    strungUtils = StringUtils()
    if(self.is_empty(string)):
        return []
def test_to_list():
    assert StringUtils().to_list("1, 2, 3") == ["1", "2", "3"]
    # assert StringUtils().to_list("") == ["", ""]
             
def contains(self, string: str, symbol: str) -> bool:
    strungUtils = StringUtils()
    res = False
    try:
        res = string.index(symbol) > -1
    except ValueError:
        pass

    return res
def test_contains():
    assert StringUtils().contains("SkyPro", "S") == True

def contains(self, string: str, symbol: str) -> bool:
    strungUtils = StringUtils()
    res = False
    try:
        res = string.index(symbol) > -1
    except ValueError:
        pass

    return res
def test_contains_nig():
    assert StringUtils().contains("SkyPro", "u") == False

def delete_symbol(self, string: str, symbol: str) -> str:
    strungUtils = StringUtils()
    if(self.contains(string, symbol)):
        string = string.replace(symbol, "")    
    return string
def test_delete_symbol():
    assert StringUtils().delete_symbol("SkyPro", "k") == "SyPro"

def delete_symbol(self, string: str, symbol: str) -> str:
    strungUtils = StringUtils()
    if(self.contains(string, symbol)):
        string = string.replace(symbol, "")    
    return string
def test_delete_symbol_nig():
    assert StringUtils().delete_symbol("SkyPro", "Pro") == "Sky"

def starts_with(self, string: str, symbol: str) -> bool:
    stringUtils = StringUtils()
    return string.startswith(symbol)
def test_starts_with():
    assert StringUtils().starts_with("SkyPro", "S") == True

def starts_with(self, string: str, symbol: str) -> bool:
    stringUtils = StringUtils()
    return string.startswith(symbol)
def test_starts_with_nig():
    assert StringUtils().starts_with("SkyPro", "P") == False 

def end_with(self, string: str, symbol: str) -> bool:
    stringUtils = StringUtils()
    return string.endswith(symbol)
def test_end_with():
    assert StringUtils().end_with("SkyPro", "o") == True

def end_with(self, string: str, symbol: str) -> bool:
    stringUtils = StringUtils()
    return string.endswith(symbol)
def test_end_with_nig():
    assert StringUtils().end_with("SkyPro", "y") == False

def is_empty(self, string: str) -> bool:
    stringUtils = StringUtils
    string = self.trim(string)
    return string == ""
def test_is_empty():
    assert StringUtils().end_with("") == True

def is_empty(self, string: str) -> bool:
    stringUtils = StringUtils
    string = self.trim(string)
    return string == ""
def test_is_empty_nig():
    assert StringUtils().end_with("SkyPro") == False  

def list_to_string(self, lst: list, joiner=", ") -> str:
    stringUtils = StringUtils
    string = ""
    length = len(lst)
        
    if length == 0: 
        return string 
        
    for i in range(0, length-1):
        string += str(lst[i]) + joiner
        
    return string + str(lst[-1])
def test_list_to_string():
    assert StringUtils().list_to_string([1,2,3,4]) == "1, 2, 3, 4"
def list_to_string(self, lst: list, joiner=", ") -> str:
    stringUtils = StringUtils
    string = ""
    length = len(lst)
        
    if length == 0: 
        return string 
        
    for i in range(0, length-1):
        string += str(lst[i]) + joiner
        
    return string + str(lst[-1])
def test_list_to_string_nig():
    assert StringUtils().list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
# u