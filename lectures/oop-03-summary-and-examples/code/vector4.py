#!/usr/bin/env python3

"""Simple Vector example.

This is used to illusttrate Python classes and some vector operations.
For a more complete (and faster) implementation, see pygame.math.Vector2.

Taking an existing Vector and extending it to a graphical vector
causes some interesting clutter in the code.

An alternative is to use graphical vectors that _have_ vectors instead of being vectors.
This is an example of the has-a (composition/contain) vs. is-a (inherit) relationship.
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add 2 vectors using the + operand. Returns a new vector."""
        # return type(self)(self.x + other.x, self.y + other.y)
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtracts the other vector from this vector. Returns a new vector."""
        return self.__class__(self.x - other.x, self.y - other.y)

    def __iter__(self):
        """Minor trick if the vector needs to be converted to a list or tuple.
        tuple(v) tries to treat the vector as a sequence. This method provides the
        necessary interface to let tuple() and list() retrieve x,y as in a sequence.
        """
        yield self.x
        yield self.y


class GVector:
    """A graphical object that draws a vector."""
    def __init__(self, origin, vec):
        self.origin = origin
        self.vec = vec

    def draw(self):
        """Draw a vector starting from the specified origin. """
        pygame.draw.line(screen, pygame.color.Color("red"), tuple(self.origin), tuple(self.origin + self.vec))


def run_demo():
    clock = pygame.time.Clock()

    v = Vector(50, 60)
    origin = Vector(0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        clock.tick(30)

        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), screen.get_height())))

        # Vector from origin to mouse
        vmouse = Vector(*pygame.mouse.get_pos())

        # Draw a vector from the origin to the mouse position
        GVector(origin, vmouse).draw()

        # Draw v from the origin
        # Wrap the vector into a GVector and then draw it.
        GVector(origin, v).draw()

        # Draw v from the mouse cursor
        GVector(vmouse, v).draw()

        # Draw the vector vmouse + v from the origin.
        GVector(origin, vmouse + v).draw()

        pygame.display.update()


if __name__ == '__main__':
    run_demo()
