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
        try:
            menu_item = MenuItemsDbModel(**dict(json_obj))
            
            session.add(menu_item)
            session.flush()

            if(menu_item.id is None):
                raise 'Can not write in {0} table'.format(MenuItemsDbModel.__tablename__)

            menu_category = [MenuByCategoryDbModel(menu_category_id=x, menu_item_id=menu_item.id) for x in menu_category]
            food_type = [MenuByFoodTypeDbModel(food_type_id=x, menu_item_id=menu_item.id) for x in food_type]
            
            for x in menu_category:
                session.add(x)

            for x in food_type:
                session.add(x)

            session.flush()

            for x in menu_category:
                if(x.id is None):
                    raise "Error writing in {0}".format(MenuByCategoryDbModel.__tablename__)

            for x in food_type:
                if(x.id is None):
                    raise "Error writing in {0}".format(MenuByFoodTypeDbModel.__tablename__)

            session.commit()
            return menu_item.id
        except:
            session.rollback()
            raise

    def update(self, json_obj):
        pass

    def delete(self, id):
        try:
            super().delete_all(MenuByCategoryDbModel, MenuByCategoryDbModel.menu_item_id == id)
            super().delete_all(MenuByFoodTypeDbModel, MenuByFoodTypeDbModel.menu_item_id == id)
        except:
            pass
        super().delete_all(MenuItemsDbModel, MenuItemsDbModel.id == id)

    def get_all(self):
        quert_result = self.db_operations.execute_query(MenuViewModel.__query__)
        result = MenuViewModel.parse_query_output(quert_result)
        return result

