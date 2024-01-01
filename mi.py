# My name is Ahmed Maher Khalil
# I made this game while I was 7 years old
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()
class Game(Button):
    def __init__(self,position=(0,0,0)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=.5,
            texture="grass",
            color=color.color(0, 0, random.uniform(32, 1.0)),
            highlight_color = color.brown,
         
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                build = Game(position=self.position + mouse.normal)
            if key == "right mouse down":
                destroy(self)

for z in range(8):
    for x in range(8):
        raxo = Game(position=(x,0,z))
player = FirstPersonController()
app.run()
            