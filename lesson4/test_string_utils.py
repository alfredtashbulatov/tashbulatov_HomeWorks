import pytest
from stringUtils import StringUtils

stringUtils = StringUtils()

@pytest.mark.test_capitilize
@pytest.mark.parametrize(
    "in_string, out_string",
    [
        ("b", "B"),
        ("skypro", "Skypro"),
        ("скайпро", "Скайпро"),
        ("skypro skypro", "Skypro skypro"),
        ("777a", "777a"),
    ],
)
def test_positive_capitilize(in_string, out_string):
    example_string = StringUtils()
    result = example_string.capitilize(in_string)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        (" b", "b"),
        ("  today", "today"),
        ("    скайпро", "скайпро"),
        ("   curtis tea", "curtis tea"),
        ("777", "777"),
    ],
)
def test_positive_trim(in_string, out_string):
    example_string = StringUtils()
    result = example_string.trim(in_string)
    assert result == out_string
    


@pytest.mark.parametrize(
    "in_string, out_string",
    [
       ("a,b,c,d", ["a", "b", "c", "d"])
    ],
)
def test_positive_to_list(in_string, out_string):
    example_string = StringUtils()
    result = example_string.to_list(in_string)
    assert result == out_string

@pytest.mark.parametrize(
    "in_string, out_string, logical_znach",
    [
        ("SkyPro", "S", True),
        ("Curtis Tea", "T", True),
        ("1, 2, 3", "1", True)
    ],
)
def test_positive_contains(in_string, out_string, logical_znach):
    example_string = StringUtils()
    result = example_string.contains(in_string, out_string)
    assert result == logical_znach

#     pytest.mark.parametrize(
#     "in_string, out_string, logical_znach",
#     [
#         ("kyPro", "U", False)
#     ],
# )
# def test_contains_nig(in_string, out_string, logical_znach):
#     example_string = StringUtils()
#     result = example_string.contains(in_string, out_string)
#     assert result == logical_znach

@pytest.mark.parametrize(
    "in_string, out_string, delete",
    [
        ("SkyPro", "k", "SyPro"),
        ("Curtis", "is", "Curt")
    ],
)
def test_positive_delete_symbol(in_string, out_string, delete):
    example_string = StringUtils()
    result = example_string.delete_symbol(in_string, out_string)
    assert result == delete

@pytest.mark.parametrize(
    "in_string, out_string, logical_znach",
    [
       ("SkyPro", "S", True),
        ("Curtis Tea", "C", True),
        ("1, 2, 3", "1", True) 
    ],
)
def test_positive_starts_with(in_string, out_string, logical_znach):
    example_string = StringUtils()
    result = example_string.starts_with(in_string, out_string)
    assert result == logical_znach

@pytest.mark.parametrize(
     "in_string, out_string, logical_znach",
     [
         ("SkyPro", "o", True),
        ("Curtis Tea", "a", True),
        ("1, 2, 3", "3", True) 
     ],
)
def test_positive_end_with(in_string, out_string, logical_znach):
    example_string = StringUtils()
    result = example_string.end_with(in_string, out_string)
    assert result == logical_znach

@pytest.mark.parametrize(
     "in_string, out_string",
     [
         ("       ", True),
        ("",  True),
        ("  ",  True) 
     ],
)
def test_positive_is_empty(in_string, out_string):
    example_string = StringUtils()
    result = example_string.is_empty(in_string)
    assert result == out_string

@pytest.mark.parametrize(
     "in_string, out_string",
     [
         ([1,2,3,4], "1, 2, 3, 4"),
        (["Curtis", "Tea"], "Curtis, Tea" ),
        (["Sky", "Pro"], "Sky, Pro") 
     ],
)
def test_positive_list_to_string(in_string, out_string):
    example_string = StringUtils()
    result = example_string.list_to_string(in_string)
    assert result == out_string
