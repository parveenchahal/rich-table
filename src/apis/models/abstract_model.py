from dataclasses import dataclass, fields

@dataclass
class Model(object):

    def validate_type(self):
        for field in fields(self):
            attr = getattr(self, field.name)
            if attr is not None and not isinstance(attr, field.type):
                error_msg = "Expected type of {0.name} is {1}, given {0.type}".format(field, type(attr))
                raise ValueError(error_msg)

    def __post_init__(self):
        self.validate_type()