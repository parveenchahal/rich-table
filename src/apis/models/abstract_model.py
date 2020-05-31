from dataclasses import dataclass, fields
from flask import jsonify

@dataclass
class Model(object):

    @staticmethod
    def deserialize(list_of_dict, model_class_ref):
        return ([model_class_ref(**item) for item in list_of_dict])

    @staticmethod
    def serialize(data_list):
        return ([row.__dict__ for row in data_list]) 

    def validate_type(self):
        for field in fields(self):
            attr = getattr(self, field.name)
            if attr is not None and not isinstance(attr, field.type):
                error_msg = "Expected type of {0.name} is {1}, given {0.type}".format(field, type(attr))
                raise ValueError(error_msg)

    def __post_init__(self):
        self.validate_type()