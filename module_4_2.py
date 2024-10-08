def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

    print("Exiting test_function")

test_function()  # Output:

try:
    inner_function()
except NameError:
    print("Error: inner_function is not defined in the global scope")
