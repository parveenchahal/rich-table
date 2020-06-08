from operations.abstract_operations import Operations
from models.db_models import MenuCategoryDbModel

class MenuCategoryOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_obj):
        # removing this because it is auto generated.
        json_obj['id'] = None
        session = self.db_operations.create_session()
        menu_category = MenuCategoryDbModel(**dict(json_obj))
        session.add(menu_category)
        session.commit()
        return menu_category.id

    def get_all(self):
        session = self.db_operations.create_session()
        quert_result = session.query(MenuCategoryDbModel).all()
        return quert_result

