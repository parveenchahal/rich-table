from operations.abstract_operations import Operations
from operations.menu_category_operations import MenuCategoryOperations
from operations.food_type_operations import FoodTypeOperations
from models.db_models import MenuItemsDbModel, MenuByCategoryDbModel, MenuByFoodTypeDbModel
from models.view_models import MenuViewModel


class MenuOperations(Operations):

    def __init__(self, db_operations):
        super().__init__(db_operations)

    def get(self, id=None):
        query = MenuViewModel.__query__
        if(id is not None):
            query = MenuViewModel.__query_with_id_filter__.replace('?', str(id), 2)
        query_result = self.db_operations.execute_query(query)
        result = MenuViewModel.parse_query_output(query_result)
        return result

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
            super()._insert(menu_item, session=session)
            session.flush()
            if(menu_item.id is None):
                raise 'Can not write in {0} table'.format(
                    MenuItemsDbModel.__tablename__)

            menu_category = [MenuByCategoryDbModel(
                menu_category_id=x, menu_item_id=menu_item.id) for x in menu_category]
            food_type = [MenuByFoodTypeDbModel(
                food_type_id=x, menu_item_id=menu_item.id) for x in food_type]

            for x in menu_category:
                super()._insert(x, session=session)

            for x in food_type:
                super()._insert(x, session=session)

            session.flush()

            for x in menu_category:
                if(x.menu_category_id is None or x.menu_item_id is None):
                    raise "Error writing in {0}".format(
                        MenuByCategoryDbModel.__tablename__)

            for x in food_type:
                if(x.food_type_id is None or x.menu_item_id is None):
                    raise "Error writing in {0}".format(
                        MenuByFoodTypeDbModel.__tablename__)

            session.commit()
            return menu_item.id
        except:
            session.rollback()
            raise

    def update(self, json_obj):
        id = json_obj['id']
        if(id is None):
            raise ValueError("id cannot be null or empty")
        del json_obj["id"]
        new_menu_category = set(json_obj.get("menu_category", []))
        new_food_type = set(json_obj.get("food_type", []))
        json_obj.pop('menu_category', None)
        json_obj.pop('food_type', None)

        session = self.db_operations.create_session()
        menu_db_data = self.get(id)[0]
        old_menu_category = set(menu_db_data.menu_category)
        old_food_type = set(menu_db_data.food_type)

        menu_category_to_be_added = new_menu_category.difference(old_menu_category)
        menu_category_to_be_added = [MenuByCategoryDbModel(
            menu_category_id=x, menu_item_id=id) for x in menu_category_to_be_added]
        menu_category_to_be_deleted = old_menu_category.difference(new_menu_category)

        food_type_to_be_added = new_food_type.difference(old_food_type)
        food_type_to_be_added = [MenuByFoodTypeDbModel(
            food_type_id=x, menu_item_id=id) for x in food_type_to_be_added]
        food_type_to_be_deleted = old_food_type.difference(new_food_type)

        try:
            for x in menu_category_to_be_added:
                super()._insert(x, session=session)

            for x in food_type_to_be_added:
                super()._insert(x, session=session)

            session.flush()

            for x in menu_category_to_be_added:
                if(x.menu_category_id is None or x.menu_item_id is None):
                    raise "Error writing in {0}".format(
                        MenuByCategoryDbModel.__tablename__)

            for x in food_type_to_be_added:
                if(x.food_type_id is None or x.menu_item_id is None):
                    raise "Error writing in {0}".format(
                        MenuByFoodTypeDbModel.__tablename__)

            for x in menu_category_to_be_deleted:
                super()._delete(MenuByCategoryDbModel, (MenuByCategoryDbModel.menu_item_id == id, MenuByCategoryDbModel.menu_category_id == x,), session)

            for x in food_type_to_be_deleted:
                super()._delete(MenuByFoodTypeDbModel, (MenuByFoodTypeDbModel.menu_item_id == id, MenuByFoodTypeDbModel.food_type_id == x,), session)

            super()._update(MenuItemsDbModel, MenuItemsDbModel.id == id, json_obj, session=session)
            session.commit()
        except:
            session.rollback()
            raise

    def delete(self, id):
        session = self.db_operations.create_session()
        try:
            result = super()._get(MenuByCategoryDbModel, MenuByCategoryDbModel.menu_item_id == id)
            if(result is not None and len(result) > 0):
                super()._delete(MenuByCategoryDbModel,
                    MenuByCategoryDbModel.menu_item_id == id, session=session)

            result = super()._get(MenuByFoodTypeDbModel, MenuByFoodTypeDbModel.menu_item_id == id)
            if(result is not None and len(result) > 0):
                super()._delete(MenuByFoodTypeDbModel,
                    MenuByFoodTypeDbModel.menu_item_id == id, session=session)

            super()._delete(MenuItemsDbModel, MenuItemsDbModel.id == id, session=session)

            session.commit()
        except:
            session.rollback()
            raise
