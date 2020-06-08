from operations.abstract_operations import Operations
from models.db_models import FoodTypeDbModel

class FoodTypeOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_obj):
        # removing this because it is auto generated.
        json_obj['id'] = None
        session = self.db_operations.create_session()
        food_type = FoodTypeDbModel(**dict(json_obj))
        session.add(food_type)
        session.commit()
        return food_type.id

    def get_all(self):
        session = self.db_operations.create_session()
        quert_result = session.query(FoodTypeDbModel).all()
        return quert_result

