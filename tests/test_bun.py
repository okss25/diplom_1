from data import Data1, Data2
import allure


class TestBun:

    @allure.title('Получаем название булки')
    def test_get_name_bun_success(self, mock_bun):
        assert mock_bun.get_name() == Data1.bun_name

    @allure.title('Получаем стоимость булки')
    def test_get_price_bun_success(self, mock_bun_2):
        assert mock_bun_2.get_price() == Data2.bun_price