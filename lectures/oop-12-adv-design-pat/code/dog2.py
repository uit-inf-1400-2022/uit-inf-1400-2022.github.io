from PIL import Image
from numpy import asarray

# This is great!

class Dog2:

    goldenImage = asarray(Image.open("golden.png"))
    labradorImage = asarray(Image.open("labrador.png"))

    def __init__(self, breed, gender, height):
        self.breed = breed
        self.gender = gender
        self.height = height
        self.image = self.loadImage()

    def loadImage(self):
        if self.breed == "golden":
            return Dog2.goldenImage
        elif self.breed == "labrador":
            return Dog2.labradorImage
        raise ValueError("Unidentified breed")

    def __str__(self):
        return "Dog of breed: " + self.breed + " with gender " + self.gender

    