from PIL import Image
import sys

bug = Image.open("Logos/Bug.png")
dark = Image.open("Logos/Dark.png")
dragon = Image.open("Logos/Dragon.png")
electric = Image.open("Logos/Electric.png")
fairy = Image.open("Logos/Fairy.png")
fighting = Image.open("Logos/Fighting.png")
fire = Image.open("Logos/Fire.png")
flying = Image.open("Logos/Flying.png")
ghost = Image.open("Logos/Ghost.png")
grass = Image.open("Logos/Grass.png")
ground = Image.open("Logos/Ground.png")
ice = Image.open("Logos/Ice.png")
normal = Image.open("Logos/Normal.png")
poison = Image.open("Logos/Poison.png")
psychic = Image.open("Logos/Psychic.png")
rock = Image.open("Logos/Rock.png")
steel = Image.open("Logos/Steel.png")
water = Image.open("Logos/Water.png")
none = Image.open("Logos/None.png")

colors = {"normal":'white',"fire":"red","water":"blue","electric":"yellow","grass":"green","ice":"cyan","fighting":"orange","poison":"purple","ground":"brown","flying":"lightblue","psychic":"pink","bug":"lightgreen","rock":"gray","ghost":"lightgray","dragon":"darkblue","dark":"black","steel":"lightgray","fairy":"pink"}

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)