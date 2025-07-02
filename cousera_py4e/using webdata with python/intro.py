"""
def display_info(*args, **kwargs):
    print("Arguments:")
    for x in args:
        print(x)
    print("Keyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(1, 2, 3, name="Alice", age=25)
"""
s = "banana"
print(s[2:])
z = "banana"
if s is z:
    print("same type and value")
else:
    print("something fishy")