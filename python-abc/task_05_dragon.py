#!/usr/bin/env python3
"""Mixins"""


class SwimMixin():
    """Mixin class"""

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    """Mixin class"""

    def fly(self):
        print("The creature flies!")


class Dragon(FlyMixin, SwimMixin):
    """Child class"""

    def roar(self):
        print("The dragon roars!")
