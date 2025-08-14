pi = 3.14

def summa(a:int, b:int) -> int:
    '''
    This function takes two numbers as input and returns their sum.
    '''
    return a + b

print("Привет из модуля")

print(__name__)
if __name__ == "__main__":
    print(2, "Самостоятельный запуск")
else :
    print(2, "Импорт модуля")
