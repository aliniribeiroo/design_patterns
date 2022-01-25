class Singleton1:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton1, cls).__new__(cls)

        return cls.instance


s = Singleton1()
print("Object created", s)


s1 = Singleton1()
print("Object created", s1)


# Lazy Instantiation


class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called")
        else:
            print("Instance already created", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
print("Objeto criado", s.get_instance())
s1 = Singleton()
