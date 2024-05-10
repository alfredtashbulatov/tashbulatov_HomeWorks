import pytest
from stringUtils import StringUtils

stringUtils = StringUtils()

def test_capitilize():
    assert StringUtils().capitilize("skypro") == "Skypro"
    assert StringUtils().capitilize("") == ""

def test_nig_capitilize():
    assert StringUtils().capitilize("to day") == "today"
    assert StringUtils().capitilize("") == ""    

def test_trim():
    assert StringUtils().trim("  today") == "today"
    assert StringUtils().trim("") == ""

def test_nig_trim():
    assert StringUtils().trim("  to day") == "today"
    assert StringUtils().trim("") == ""


def test_to_list():
    assert StringUtils().to_list("1, 2, 3") == ["1", "2", "3"]
    # assert StringUtils().to_list("") == ["", ""]
             
def test_contains():
    assert StringUtils().contains("SkyPro", "S") == True

def test_contains_nig():
    assert StringUtils().contains("SkyPro", "u") == False

def test_delete_symbol():
    assert StringUtils().delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_nig():
    assert StringUtils().delete_symbol("SkyPro", "Pro") == "Sky"

def test_starts_with():
    assert StringUtils().starts_with("SkyPro", "S") == True

def test_starts_with_nig():
    assert StringUtils().starts_with("SkyPro", "P") == False 

def test_end_with():
    assert StringUtils().end_with("SkyPro", "o") == True
    
def test_end_with_nig():
    assert StringUtils().end_with("SkyPro", "y") == False

def test_is_empty():
    assert StringUtils().end_with("") == True

def test_is_empty_nig():
    assert StringUtils().end_with("SkyPro") == False  

def test_list_to_string():
    assert StringUtils().list_to_string([1,2,3,4]) == "1, 2, 3, 4"

def test_list_to_string_nig():
    assert StringUtils().list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
# u
