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

    def get(self, id=None):
        if(id is None):
            return super()._get(FoodTypeDbModel)
        else:
            return super()._get(FoodTypeDbModel, FoodTypeDbModel.id == id)

    def update(self, json_obj):
        id = json_obj['id']
        if(id is None):
            raise ValueError("id cannot be null or empty")
        del json_obj["id"]
        super()._update(FoodTypeDbModel, FoodTypeDbModel.id == id, json_obj)

    def delete(self, id):
        super()._delete(FoodTypeDbModel, FoodTypeDbModel.id == id)
