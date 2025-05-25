from data import TestDataBase
import pytest
import allure


class TestDB:
    @allure.title('Список доступных булок из базы')
    @allure.description('Имя и стоимость  булки')
    @pytest.mark.parametrize('index_bun, bun_name, bun_price', TestDataBase.test_data_base_buns)
    def test_available_buns_db_success(self, db, index_bun, bun_name, bun_price):
        db = DataBase()
        data_buns = db.available_buns()
        bun = data_buns [index_bun]
        assert bun.get_name() == bun_name, f"Expected bun name '{bun_name}', got '{bun.get_name()}'"
        assert bun.get_price() == bun_price, f"Expected bun price '{bun_price}', got '{bun.get_price()}'"

    @allure.title('Список доступных ингредиентов из базы')
    @allure.description('Имя, тип и стоимость  ингредиента')
    @pytest.mark.parametrize('index_i, type_ingredient, name_ingredient, price_ingredient',
                             TestDataBase.test_data_base_ingredients)
    def test_available_ingredients_db_success(self, db, index_i, type_ingredient, name_ingredient, price_ingredient):
        db = DataBase()
        data_ingredients = db.available_ingredients()
        ingredient = data_ingredients[index_i]
        assert ingredient.get_name() == name_ingredient, f"Expected ingredient name '{name_ingredient}', got '{ingredient.get_name()}'"
        assert ingredient.get_type() == type_ingredient, f"Expected type '{type_ingredient}', got '{ingredient.get_type()}'"
        assert ingredient.get_price() == price_ingredient, f"Expected price '{price_ingredient}', got '{ingredient.get_price()}'"