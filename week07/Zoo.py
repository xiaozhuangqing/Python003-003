from abc import ABCMeta, abstractclassmethod
import sys

class Zoo(object):
    
    animals = {}

    def __init__(self, name):
        self.name = name

    @classmethod
    def add_animal(cls, animal):
        if animal not in cls.animals:
            cls.animals[animal] = animal
        
        if not hasattr(cls, animal.__class__.__name__):
            setattr(cls, animal.__class__.__name__, animal)

        
class Animal(metaclass=ABCMeta):
    
    @abstractclassmethod
    def __init__(self, kind, shape, character):
        self.kind = kind    #类型
        self.shape = shape  #体型
        self.character = character  #性格

    @property
    def is_fierce(self):    #是否凶猛动物
        return (self.shape == '中型' or self.shape == '大型') and self.kind == '食肉' and self.character == '凶猛'

    @property
    def is_pet(self):
        return (!self.is_fierce)
    

class Cat(Animal):
    sound = '喵'

    def __init__(self, name, kind, shape, character):
        self.name = name
        super().__init__(kind, shape, character)


class Dog(Animal):
    sound = '汪汪'

    def __init__(self, name, kind, shape, character):
        self.name = name
        super().__init__(kind, shape, character)


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
