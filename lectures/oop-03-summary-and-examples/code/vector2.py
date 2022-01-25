#!/usr/bin/env python3

"""Simple Vector example.

This is used to illusttrate Python classes and some vector operations.
For a more complete (and faster) implementation, see pygame.math.Vector2.

Instead of converting back and forth between Vector and GVectors,
use a draw_vector function that draws vectors.
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
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtracts the other vector from this vector. Returns a new vector."""
        return Vector(self.x - other.x, self.y - other.y)

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


def draw_vector(vector, origin=None):
    """Draw a vector. This requires a starting point/origin to draw the vector _from_.
    An object (such as Vector) with an 'x' and 'y' attribute can be used to specify the origin.
    If no origin is specified, an origin of (0,0) is assumed.
    """
    if origin is None:
        origin = Vector(0, 0)
    end = origin + vector
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

        # Second approach: use a separate function that draws a vector.
        # The parameter order here is a bit strange since origin is an optional
        # parameter, and default parameters need to be after required parameters.

        # Draw v from the origin
        draw_vector(v)

        # Draw v from the mouse cursor
        draw_vector(v, vmouse)

        # Draw the vector vmouse + v from the origin.
        draw_vector(vmouse + v)

        pygame.display.update()


if __name__ == '__main__':
    run_demo()
