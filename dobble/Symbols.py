class Symbol(object):

    def __init__(self, name, *args):
        self.name = name
        if args:
            self.alternative_names = [x for x in args]
        else:
            self.alternative_names = []

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self.name)

    def get_img_path(self):
        filename = self.name.replace(" ", "_").lower()
        path = 'img/patterns/' + filename + '.jpg'
        return path


ANCHOR = Symbol("Anchor")
APPLE = Symbol("Apple")
BIRD = Symbol("Bird")
BOMB = Symbol("Bomb")
BOTTLE = Symbol("Bottle")
CACTUS = Symbol("Cactus")
CANDLE = Symbol("Candle")
CARROT = Symbol("Carrot")
CAT = Symbol("Cat")
CHEESE = Symbol("Cheese")
CLOCK = Symbol("Clock")
CLOVER = Symbol("Clover")
CLOWN = Symbol("Clown")
COBWEB = Symbol("Cobweb", "Spider's Web")
DINOSAUR = Symbol("Dinosaur")
DOBBLE = Symbol("Dobble")
DOG = Symbol("Dog")
DOLPHIN = Symbol("Dolphin")
DRAGON = Symbol("Dragon")
DROP = Symbol("Drop")
EXCLAMATION_MARK = Symbol("Exclaimation Mark")
EYE = Symbol("Eye")
FIRE = Symbol("Fire")
FLOWER = Symbol("Flower")
GHOST = Symbol("Ghost")
HAMMER = Symbol("Hammer")
HEART = Symbol("Heart")
ICE_CUBE = Symbol("Ice Cube")
IGLOO = Symbol("Igloo")
KEY = Symbol("Key")
KNIGHT = Symbol("Knight")
LADYBIRD = Symbol("Ladybird")
LIGHTBULB = Symbol("Lightbulb")
LIGHTNING = Symbol("Lightning")
LIPS = Symbol("Lips")
MAN = Symbol("Man", "Little Man")
MAPLE_LEAF = Symbol("Maple Leaf")
MOON = Symbol("Moon")
NO_ENTRY = Symbol("No Entry", "Stop Sign")
PADLOCK = Symbol("Padlock", "Lock")
PENCIL = Symbol("Pencil", "Crayon")
QUESTION_MARK = Symbol("Question Mark")
SCISSORS = Symbol("Scissors")
SKULL = Symbol("Skull", "Skull and Crossbones")
SNOWFLAKE = Symbol("Snowflake")
SNOWMAN = Symbol("Snowman")
SPIDER = Symbol("Spider")
SPLATS = Symbol("Splats", "Splodge", "Spots")
SUN = Symbol("Sun")
SUNGLASSES = Symbol("Sunglasses")
TARGET = Symbol("Target", "Crosshair")
TAXI = Symbol("Taxi", "Car")
TORTOISE = Symbol("Tortoise")
TREBLE_CLEF = Symbol("Treble Clef", "Music")
TREE = Symbol("Tree")
YIN_YANG = Symbol("Yin Yang")
ZEBRA = Symbol("Zebra")