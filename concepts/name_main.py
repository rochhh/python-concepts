import name_main2

def fn():
    print("the main fn in the name_main.py file")

print("this will always run wherever imported !")

print(__name__)

if __name__ == '__main__':
    fn()

    print("this will only work in this main file and no where-else ")