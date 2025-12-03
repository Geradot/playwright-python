import re
from playwright.sync_api import expect
from pages import HomePage
from utils import data_loader

def test_tc8(home_page: HomePage) -> None:
    """TC-8. Verify All Products and product detail page"""    
    products_page = home_page.open_products_page()
    expect(products_page.page).to_have_url(
        re.compile(f"{products_page.PATH}$")
    )
    expect(products_page.products_block.product_list).to_have_count(
        products_page.products_block.expected_count_of_products
    )
    
    product_page = products_page.products_block.view_product_details(
        data_loader.get_product(0)["id"]
    )
    expect(product_page.page).to_have_url(
        re.compile(f"{product_page.PATH}$")
    )
    expect(product_page.product_name).to_be_visible()
    expect(product_page.product_category).to_be_visible()
    expect(product_page.product_price).to_be_visible()
    expect(product_page.product_availability).to_be_visible()
    expect(product_page.product_condition).to_be_visible()
    expect(product_page.product_brand).to_be_visible()
    
def test_tc9(home_page: HomePage) -> None:
    """TC-9. Search Product"""
    searching_query = data_loader.get_product(1)["name"][:5]  # "Tshirt"
    
    expected_results = re.compile(r"T[-\s]?Shirt", re.IGNORECASE)
    
    products_page = home_page.open_products_page()
    expect(products_page.page).to_have_url(
        re.compile(f"{products_page.PATH}$")
    )
    expect(products_page.products_block.product_list).to_have_count(
        products_page.products_block.expected_count_of_products
    )

    products_page.search_product(searching_query)
    for i in range(products_page.products_block.product_list.count()):
        expect(products_page.products_block.product_list.nth(i)).to_contain_text(
            expected_results
        )
    
def test_tc12(home_page: HomePage) -> None:
    """TC-12. Add Products in Cart"""
    products = data_loader.get_products()[:2]
    
    products_page = home_page.open_products_page()
    products_page.products_block.scroll_to_products()
    products_page.products_block.add_product_to_cart(products[0]["id"])
    products_page.modal_added_to_cart.click_continue_shopping()
    products_page.products_block.add_product_to_cart(products[1]["id"])
    
    cart_page = products_page.modal_added_to_cart.click_view_cart()
    assert cart_page.are_products_in_cart(
        products[0]["name"],
        products[1]["name"]
    )
    
def test_tc13(home_page: HomePage) -> None:
    """TC-13. Verify Product quantity in Cart"""
    import random
    random_index = random.randint(0, 1)
    product = data_loader.get_product(random_index)
    quantity = 4
    
    home_page.products_block.scroll_to_products()
    product_page = home_page.products_block.view_product_details(random_index)
    product_page.set_quantity(quantity)
    product_page.add_to_cart()
    cart_page = home_page.modal_added_to_cart.click_view_cart()
    expect(cart_page.get_product_quantity(product["name"])).to_have_text(str(quantity))
    