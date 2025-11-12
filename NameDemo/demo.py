# demo.py

print("This line is always executed")

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("demo.py is executed directly")
    name = input("Enter your name: ")
    print(greet(name))
else:
    print("demo.py has been imported")
