from operations.abstract_operations import Operations
from models.db_models import FoodTypeDbModel


class FoodTypeOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_obj):
        # removing this because it is auto generated.
        json_obj['id'] = None
        food_type = FoodTypeDbModel(**dict(json_obj))
        super()._insert(food_type)
        return food_type.id

    def get_all(self):
        return super()._get_all(FoodTypeDbModel)

    def delete(self, id):
        super()._delete(FoodTypeDbModel, FoodTypeDbModel.id == id)
