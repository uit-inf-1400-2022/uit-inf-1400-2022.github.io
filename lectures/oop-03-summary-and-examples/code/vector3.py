#!/usr/bin/env python3

"""Simple Vector example.

This is used to illusttrate Python classes and some vector operations.
For a more complete (and faster) implementation, see pygame.math.Vector2.

Try to mitigate the issue of vector operations always returning a Vector
object by asking "self" what class it is and using that class to create
and return an object.

Remaining issue: This solves adding a vector to a GVector (gv + v),
but what about adding a GVector to a vector (v + gv)?
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


class GVector(Vector):
    """A Vector with a draw method"""
    def __init__(self, x=0, y=0, vec=None):
        if vec:
            super().__init__(vec.x, vec.y)
        else:
            super().__init__(x, y)

    def draw(self, origin=None):
        """Draw a vector. This requires a starting point/origin to draw the vector _from_.
        An object (such as Vector) with an 'x' and 'y' attribute can be used to specify the origin.
        If no origin is specified, an origin of (0,0) is assumed.
        """
        if origin is None:
            origin = Vector(0, 0)
        end = origin + self
        pygame.draw.line(screen, pygame.color.Color("red"), tuple(origin), tuple(end))


def run_demo():
    clock = pygame.time.Clock()

    v = Vector(50, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        clock.tick(30)

        pygame.draw.rect(screen, (0, 0, 0), ((0, 0), (screen.get_width(), screen.get_height())))

        # Draw a vector from the origin to the mouse position
        # This one _is_ a GVector anyway (it was just created)
        vmouse = GVector(*pygame.mouse.get_pos())
        vmouse.draw()

        # Draw v from the origin
        # Wrap the vector into a GVector and then draw it.
        v = GVector(vec=v)
        v.draw()

        # Draw v from the mouse cursor
        v.draw(vmouse)

        # Draw the vector vmouse + v from the origin.
        v2 = vmouse + v
        v2.draw()

        pygame.display.update()


if __name__ == '__main__':
    run_demo()
