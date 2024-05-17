import random

def squeeze_orange():
    phrases = [
        "Squeezing oranges... Extracting giggles!",
        "Orange juice with a splash of sunshine!",
        "Warning: This juice is full of puns!",
        "Squeezed by the hands of laughter!",
        "Juice so fresh, it's practically a comedian!",
        "From orange to hilariously tangy!",
        "Pure orange juice with a twist of chuckles!",
        "Freshly squeezed with a side of smiles!"
    ]
    return random.choice(phrases)

def add_ingredients():
    ingredients = [
        "1 cup of hilarity",
        "2 tablespoons of chuckles",
        "A pinch of wit",
        "A dollop of joy",
        "A zest of humor",
        "A dash of giggles",
        "1 quart of sunshine",
        "A sprinkle of fun"
    ]
    return random.sample(ingredients, 3)

def blend_juice():
    steps = [
        "Blending with the speed of a laugh!",
        "Stirring in some humor!",
        "Mixing with a spoonful of fun!",
        "Shaking it with a dance of joy!",
        "Whisking it with a smile!",
        "Combining with a burst of laughter!"
    ]
    return random.choice(steps)

def pour_glass():
    glasses = [
        "Pouring into a glass of mirth!",
        "Serving in a cup of cheer!",
        "Filling a goblet of glee!",
        "Decanting into a jug of jests!",
        "Splashing into a tumbler of tickles!",
        "Flowing into a flask of fun!"
    ]
    return random.choice(glasses)

def serve_juice():
    return "Enjoy your orange juice with a twist of fun and a squeeze of laughter!"

def orange_juice_generator():
    print(squeeze_orange())
    print("Adding ingredients:")
    for ingredient in add_ingredients():
        print(f" - {ingredient}")
    print(blend_juice())
    print(pour_glass())
    print(serve_juice())

if __name__ == "__main__":
    orange_juice_generator()
