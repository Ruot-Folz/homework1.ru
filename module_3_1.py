calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_lower = [item.lower() for item in list_to_search]
    return string_lower in list_lower
info1 = string_info("Hello, World!")
info2 = string_info("Python")
contains1 = is_contains("Urban", ["city", "URBAN", "village"])
contains2 = is_contains("town", ["city", "URBAN", "village"])
print(f"Количество вызовов функций: {calls}")
print(f"Информация о строках: {info1}, {info2}")
print(f"Результаты поиска: {contains1}, {contains2}")
