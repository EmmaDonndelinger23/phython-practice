def define(word):
    word == word.lower()
    if word == "ice cream":
        return "a soft frozen food made with sweetened and flavored milk fat"
    elif word == "oreo":
        return "a brand of chocolate sandwich cookie with a creamy white filling"
    elif word == "cookie":
        return "a small sweet cake, typically round and flat and having a crisp or chewy texture"
    elif word == "cake":
        return "an item of soft, sweet food made from a mixture of flour, shortening, eggs, sugar, and other ingredients, baked and often decorated"
    elif word == "pie":
        return "a baked dish of fruit, or meat and vegetables, typically with a top and base of pastry"
    elif word == "pizza":
        return "a dish of Italian origin consisting of a flat, round base of dough baked with a topping of tomato sauce and cheese, typically with added meat or vegetables"
    elif word == "doughnut":
        return "a small fried cake of sweetened dough, typically in the shape of a ball or ring"
    elif word == "cupcake":
        return "a small cake baked in a cup-shaped container and typically iced"
    elif word == "spaghetti":
        return "pasta made in long, slender, solid strings"
    elif word == "apple":
        return "the round fruit of a tree of the rose family, which typically has thin red or green skin and crisp flesh"
    else:
        return "this word is not in this dictionary"

print(define("cake"))
print(define("banana"))