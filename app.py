import my_module

print("Hello World")

#exit(100)

x = my_module.summa(10, 20)
print(x)
print(my_module.pi)

print(__name__)
if __name__ == "__main__":
    print(1, "Hello from main")
    