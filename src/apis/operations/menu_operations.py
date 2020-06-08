from operations.abstract_operations import Operations
from models.db_models import MenuItemsDbModel, MenuByCategoryDbModel, MenuByFoodTypeDbModel
from models.view_models import MenuViewModel

class MenuOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def insert(self, json_obj):
        # removing this because it is auto generated.
        json_obj['id'] = None
        menu_category = json_obj['menu_category']
        food_type = json_obj['food_type']
        del json_obj['menu_category']
        del json_obj['food_type']

        session = self.db_operations.create_session()
        #return json_obj
        menu_item = MenuItemsDbModel(**dict(json_obj))

        session.add(menu_item)

        if(menu_item.id is None):
            raise 'Can not write in menu_items table'

        for x in menu_category:
            session.add(MenuByCategoryDbModel(menu_category_id=x, menu_item_id=menu_item.id))

        for x in food_type:
            session.add(MenuByFoodTypeDbModel(food_type_id=x, menu_item_id=menu_item.id))

        session.commit()
        return menu_item.id

    def update(self, json_string):
        data_dict = dict(json_string)
        menu_category = list()

    def get_all(self):
        quert_result = self.db_operations.execute_query(MenuViewModel.__query__)
        result = MenuViewModel.parse_query_output(quert_result)
        return result

