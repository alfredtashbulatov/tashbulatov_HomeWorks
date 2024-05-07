import pytest
from stringUtils import StringUtils

stringUtils = StringUtils()

def test_pozitive_capitilize():
    stringUtils = StringUtils()
    def capitilize(self, string: str) -> str:
        return string.capitalize()


def test_pozitive_trim():
    stringUtils = StringUtils()
    def trim(self, string: str) -> str:
        whitespace = " "
        while (string.startswith(whitespace)):
            string = string.removeprefix(whitespace)
        return string

def test_to_list():
    strungUtils = StringUtils()
    def to_list(self, string: str, delimeter = ",") -> list[str]:
         if(self.is_empty(string)):
            return []


def test_contains():
    strungUtils = StringUtils()
    def contains(self, string: str, symbol: str) -> bool:
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

def test_delete_symbol():
    strungUtils = StringUtils()
    def delete_symbol(self, string: str, symbol: str) -> str:
        if(self.contains(string, symbol)):
            string = string.replace(symbol, "")    
        return string
    
def test_starts_with(): 
    strungUtils = StringUtils()
    def starts_with(self, string: str, symbol: str) -> bool:
        return string.startswith(symbol)
    
def test_end_with():
    strungUtils = StringUtils()
    def end_with(self, string: str, symbol: str) -> bool:
        return string.endswith(symbol)

def test_is_empty():
    strungUtils = StringUtils()
    def is_empty(self, string: str) -> bool:
        string = self.trim(string)
        return string == ""

def test_list_to_string():
    strungUtils = StringUtils()
    def list_to_string(self, lst: list, joiner=", ") -> str:
        string = ""
        length = len(lst)
        
        if length == 0: 
            return string 
        
        for i in range(0, length-1):
            string += str(lst[i]) + joiner
        
        return string + str(lst[-1])    