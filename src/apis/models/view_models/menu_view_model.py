from models.abstract_model import Model
from models.db_models import MenuItemsDbModel, FoodTypeDbModel, MenuByCategoryDbModel, MenuByFoodTypeDbModel, MenuCategoryDbModel
from dataclasses import dataclass
from typing import List


@dataclass
class MenuViewModel(Model):
    __query__ = f'(SELECT m.id, m.name, m.price, m.image_url, mc.id as menu_category, NULL as food_type from {MenuItemsDbModel.__tablename__} m '\
        f'left join {MenuByCategoryDbModel.__tablename__} mbc on m.id = mbc.menu_item_id '\
        f'left join {MenuCategoryDbModel.__tablename__} mc on mbc.menu_category_id = mc.id) '\
        f'UNION ALL '\
        f'(SELECT m.id, m.name, m.price, m.image_url, NULL as menu_category, ft.id as food_type from {MenuItemsDbModel.__tablename__} m '\
        f'left join {MenuByFoodTypeDbModel.__tablename__} mbft on m.id = mbft.menu_item_id '\
        f'left join {FoodTypeDbModel.__tablename__} ft on mbft.food_type_id = ft.id) '
    
    __query_with_id_filter__ = f'(SELECT m.id, m.name, m.price, m.image_url, mc.id as menu_category, NULL as food_type from {MenuItemsDbModel.__tablename__} m '\
        f'left join {MenuByCategoryDbModel.__tablename__} mbc on m.id = mbc.menu_item_id '\
        f'left join {MenuCategoryDbModel.__tablename__} mc on mbc.menu_category_id = mc.id '\
        f'where m.id = ?) '\
        f'UNION ALL '\
        f'(SELECT m.id, m.name, m.price, m.image_url, NULL as menu_category, ft.id as food_type from {MenuItemsDbModel.__tablename__} m '\
        f'left join {MenuByFoodTypeDbModel.__tablename__} mbft on m.id = mbft.menu_item_id '\
        f'left join {FoodTypeDbModel.__tablename__} ft on mbft.food_type_id = ft.id '\
        f'where m.id = ?) '\

    id: int
    name: str
    price: float
    image_url: str
    menu_category: list = None
    food_type: list = None

    @staticmethod
    def parse_query_output(query_output_list):
        result_dict = {}
        for row in query_output_list:
            if row['id'] not in result_dict:
                result_dict[row['id']] = MenuViewModel(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    image_url=row['image_url'],
                    menu_category=list(),
                    food_type=list())
            else:
                result_dict[row['id']]
            if row['food_type'] is not None:
                result_dict[row['id']].food_type.append(row['food_type'])
            elif row['menu_category'] is not None:
                result_dict[row['id']].menu_category.append(
                    row['menu_category'])
        return ([row for row in result_dict.values()])
