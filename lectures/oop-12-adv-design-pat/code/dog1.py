from PIL import Image
from numpy import asarray

# WARNING: This is not a good way to implement this...

class Dog1:

    def __init__(self, breed, gender, height):
        self.breed = breed
        self.gender = gender
        self.height = height
        self.image = self.loadImage()

    def loadImage(self):
        imgfile = Image.open(self.breed + ".png")
        image = asarray(imgfile)
        imgfile.close()
        return image

    def __str__(self):
        return "Dog of breed: " + self.breed + " with gender " + self.gender

    