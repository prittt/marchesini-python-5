from typing import Union, List, Tuple, Set, Self

class Vector:
    # def __init__(self, *initializer : Union[int, float, List[Union[int, float]], Tuple[Union[int, float]], Set[Union[int, float]]]):
    #     if len(initializer) == 1 and isinstance(initializer[0], (list, tuple, set)):
    #         self.__data: List[Union[int, float]] = list(initializer[0])
    #     elif all(isinstance(x, (int, float)) for x in initializer):
    #         self.__data: List[Union[int, float]] = list(initializer)
    #     else:
    #         raise TypeError("Expected numbers or a single list/tuple/set of numbers")
    
    def __init__(self, *initializer : Union[int, float, List[Union[int, float]], Tuple[Union[int, float]], Set[Union[int, float]]]):
        if len(initializer) == 1 and isinstance(initializer[0], (list, tuple, set)):
            self.__data: List[Union[int, float]] = list(initializer[0])
        elif all(isinstance(x, (int, float)) for x in initializer):
            self.__data: List[Union[int, float]] = list(initializer)
        else:
            raise TypeError("Expected numbers or a single list/tuple/set of numbers")


    def __str__(self) -> str:
        return "{" + f"{self.__data.__str__().replace("[", "").replace("]","")}" + "}"

    def __repr__(self) -> str:
        return f"Vector({self.__data})"

    def __len__(self) -> int:
        return len(self.__data) 

    ####### ADD ####### 
    def __add__(self, other: Union[Self, int, float]) -> "Vector":  
        if isinstance(other, Vector):
            if len(self.__data) != len(other.__data):
                raise ValueError("Vectors must have the same length for addition")
            sum = []
            # for i in range(len(self.__data)):
            #     sum.append(self.__data[i] + other.__data[i])
            # return Vector(sum)
            # OPPURE     
            # sum = []
            # for a, b in zip(self.__data, other.__data):
            #     sum.append(a + b)
            # return Vector(sum)
            # return Vector([a + b for a, b in zip(self.__data, other.__data)])
        elif isinstance(other, (int, float)):
            return Vector([a + other for a in self.__data])
        else:
            raise NotImplemented

    def __iadd__(self, other: Self) -> Self:
        result = self + other
        self.__data = result.__data
        return self

    def __radd__(self, other: Union[int, float]) -> Self:
        return self + other
    
    def __getitem__(self, key: int | slice) -> Union[int, float] | Self:
        
        # if len(key) == 1:
        #     return self.__data[*key]
        # elif len(key) > 1:
        #     return Vector(self.__data[*key])
        
        # if isinstance(key, int):
        #     return self.__data[key] 
        # elif isinstance(key, slice):
        #     return Vector(self.__data[key])
        # return NotImplemented

        result = self.__data[key]
        if isinstance(key, slice):
            return Vector(result) 
        else:
            result        
        return Vector(result) if isinstance(key, slice) else result

print(v0 := Vector(1))
print(v1 := Vector(1, 2, 3, 4, 5, 6, 7))
print(v2 := Vector([1, 2, 3, 4, 5, 6, 7]))
print(v3 := Vector({1, 2, 3, 4, 5, 6, 7}))
print(v4 := Vector((1, 2, 3, 4, 5, 6, 7)))

print(v3 := v1 + v2)
print(v4 := v1 + 1)
print(v5 := 1 + v2)

for e in v5:
    print(e)

v6 = v5[2]
v6 = v5[2:3]
pass