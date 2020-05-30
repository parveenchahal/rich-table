from dataclasses import dataclass

@dataclass
class Model(object):
    @staticmethod
    def deserialize(list_of_dict, model_class_ref):
        return ([model_class_ref(**item) for item in list_of_dict])

