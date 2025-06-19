class Example:
    def __init__(self):
        self.attr1 = 5
        self.__private = "attributo_privato" 

    def add_property(self):
        self.attr2 = 10

    def get_private(self):
        return self.__private
    
    def set_private(self, value):
        self.__private = value

    def __str__(self):
        return f"Example with attr1 = {self.attr1}"

ex = Example()
print(ex)
print(ex.attr1)
ex.add_property()
print(ex.attr2)
print(ex.__private)
ex.attr3 = "ciao"
pass
