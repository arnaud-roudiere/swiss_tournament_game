def weird_decorator(function):
    def wrapper():
        print("bbb")
        function()
        function()
        print("ccc")
        function()

    return wrapper


@weird_decorator
def say_aaa():
    print("aaa")

say_aaa()