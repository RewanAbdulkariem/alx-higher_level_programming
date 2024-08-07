#!/usr/bin/python3
"""
module base.py
"""
import json
import csv
import turtle
import os


class Base:
    """
        Base class for managing id attribute in future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'

        json_str = json.dumps(list_dictionaries)
        return (json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as outfile:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dict_list)
            outfile.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            return None

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r') as f:
            data = f.read()

        dict_list = cls.from_json_string(data)
        instances = [cls.create(**d) for d in dict_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in CSV
        """
        if list_objs is None:
            list_objs = []
        fields = []
        filename = f"{cls.__name__}.csv"
        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
                writer.writerow(fields)
                for obj in list_objs:
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                fields = ['id', 'width', 'x', 'y']
                writer.writerow(fields)
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes in CSV
        """
        filename = f"{cls.__name__}.csv"
        if not os.path.isfile(filename):
            return []

        instances = []
        with open(filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                row = {key: int(value) for key, value in row.items()}
                obj = cls.create(**row)
                instances.append(obj)
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all the Rectangles and Squares using the Turtle graphics module.
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        pen = turtle.Turtle()
        pen.speed(1)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for sq in list_squares:
            pen.penup()
            pen.goto(sq.x, sq.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(sq.size)
                pen.left(90)

        turtle.done()
