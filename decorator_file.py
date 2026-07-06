from time import sleep

def delay_fun(fun):
    def wrapper(*args, **kwargs):
        sleep(2)
        fun()
    return wrapper

@delay_fun
def hello_world():
    print("hello world")

def bye_world():
    print("bye")

hello_world()