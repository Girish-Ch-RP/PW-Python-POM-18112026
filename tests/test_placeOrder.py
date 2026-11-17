import pytest
from playwright.sync_api import expect
from pages.cartPage import CartPage
from pages.homepage import HomePage
from pages.loginPage import LoginPage
from config import Config
from utils.data_reader_util import read_csv_data, read_json_data, read_excel_data


@pytest.mark.parametrize("x,y,z", [
    ("girishkalyan", "Super", "Samsung galaxy s6")
])
def test_place_order(page, x, y, z):
    login_page = LoginPage(page)
    login_page.login(x, y)

    home_page = HomePage(page)
    home_page.add_product_to_cart(z)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    cart_page = CartPage(page)
    product_in_cart = cart_page.check_product_in_cart(z)
    # page.wait_for_timeout(3000)
    # expect(product_in_cart).to_be_visible()

@pytest.mark.sanity
def test_place_order2(page):
    login_page = LoginPage(page)
    login_page.login(Config.email, Config.password)

    home_page = HomePage(page)
    home_page.add_product_to_cart(Config.product_name)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    cart_page = CartPage(page)
    product_in_cart = cart_page.check_product_in_cart(Config.product_name)
    page.wait_for_timeout(3000)
    expect(product_in_cart).to_be_visible()


csv_data = read_csv_data("testdata/logindata.csv")


@pytest.mark.parametrize("username,password,productname", csv_data)
def test_place_order_data_driven_csv(username, password, productname, page):
    login_page = LoginPage(page)
    login_page.login(username, password)

    home_page = HomePage(page)
    home_page.add_product_to_cart(productname)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    cart_page = CartPage(page)
    product_in_cart = cart_page.check_product_in_cart(productname)
    page.wait_for_timeout(3000)
    expect(product_in_cart).to_be_visible()


json_data = read_json_data("testdata/logindata.json")


@pytest.mark.parametrize("username,password,productname", json_data)
def test_place_order_data_driven_json(username, password, productname, page):
    login_page = LoginPage(page)
    login_page.login(username, password)

    home_page = HomePage(page)
    home_page.add_product_to_cart(productname)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    cart_page = CartPage(page)
    product_in_cart = cart_page.check_product_in_cart(productname)
    page.wait_for_timeout(3000)
    expect(product_in_cart).to_be_visible()


excel_data = read_excel_data("testdata/logindata.json")


@pytest.mark.parametrize("username,password,productname", excel_data)
def test_place_order_data_driven_excel(username, password, productname, page):
    login_page = LoginPage(page)
    login_page.login(username, password)

    home_page = HomePage(page)
    home_page.add_product_to_cart(productname)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    cart_page = CartPage(page)
    product_in_cart = cart_page.check_product_in_cart(productname)
    page.wait_for_timeout(3000)
    expect(product_in_cart).to_be_visible()
