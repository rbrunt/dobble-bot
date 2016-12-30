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

# Define a constnat for each possible dobble symbol
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
EXCLAMATION_MARK = Symbol("Exclamation Mark")
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

ALL_SYMBOLS = [ANCHOR, APPLE, BIRD, BOMB, BOTTLE, CACTUS, CANDLE, CARROT, CAT, CHEESE, CLOCK, CLOVER, CLOWN, COBWEB, DINOSAUR, DOBBLE, DOG, DOLPHIN, DRAGON, DROP, EXCLAMATION_MARK, EYE, FIRE, FLOWER, GHOST, HAMMER, HEART, ICE_CUBE, IGLOO, KEY, KNIGHT, LADYBIRD, LIGHTBULB, LIGHTNING, LIPS, MAN, MAPLE_LEAF, MOON, NO_ENTRY, PADLOCK, PENCIL, QUESTION_MARK, SCISSORS, SKULL, SNOWFLAKE, SNOWMAN, SPIDER, SPLATS, SUN, SUNGLASSES, TARGET, TAXI, TORTOISE, TREBLE_CLEF, TREE, YIN_YANG, ZEBRA]