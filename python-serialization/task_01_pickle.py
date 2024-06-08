"""Custom Object class module"""
import pickle


class CustomObject:
    """Custom Object that is serializable, and deserializable"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        for key, value in self.__dict__.items():
            print("{}: {}".format(key, value))

    def serialize(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as err:
            return None
