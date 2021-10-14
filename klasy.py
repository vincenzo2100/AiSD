class House:
    doors: int
    color: str
    

    def __init__(self,doors: int,color: str) -> None:
        self.doors = doors
        self.color = color

    def change_color(self,new_color: str) -> None:
        if new_color == self.color:
            print('Kolor nie moze byc ten sam')
            return 

        self.color = new_color

    def __len__(self) -> int:
        return 100

    def __str__(self) -> str:
        return f'liczba drzwi: {self.doors} '+ f'kolor elewacji:{self.color}'

house1: House = House(doors=10,color='blue')
print(house1.doors)
print(house1.color)

print(len(house1))
print(house1)

house2: House = House(doors=50,color='green')

print(house2)

