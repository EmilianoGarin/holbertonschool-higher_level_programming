#!/usr/bin/python3
"""Task 10"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {super().x}/{super().y} - \
{super().width}"

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        Rectangle.width.fset(self, value)
        Rectangle.height.fset(self, value)

    def update(self, *args, **kwargs):
        """update a Square"""
        if len(args) == 0:
            for i, v in kwargs.items():
                if i == "id":
                    if type(v) is not None:
                        self.id = v
                elif i == "size":
                    self.size = v
                elif i == "x":
                    Rectangle.x.fset(self, v)
                elif i == "y":
                    Rectangle.y.fset(self, v)
        else:
            for i, v in enumerate(args):
                if i == 0:
                    if type(v) is not None:
                        self.id = v
                elif i == 1:
                    self.size = v
                elif i == 2:
                    Rectangle.x.fset(self, v)
                elif i == 3:
                    Rectangle.y.fset(self, v)

    def to_dictionary(self):
        """dictionary of the Square"""
        return {'id': self.id, 'x': super().x, 'size': super().width,
                'y': super().y}
