from playwright.sync_api import Page


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        # Product links under product cards
        self.products_list_locator = "div#tbodyid div.card h4.card-title a"

        # Add to cart button
        self.add_to_cart_button = page.locator(
            'a:has-text("Add to cart")'
        )

        # Cart link
        self.cart_link = page.locator("#cartur")

    def add_product_to_cart(self, product_name):

        products = self.page.locator(self.products_list_locator)

        count = products.count()

        for i in range(count):

            name = products.nth(i).text_content().strip()

            if name == product_name:
                products.nth(i).click()
                break
        self.page.on("dialog", lambda dialog: dialog.accept())

        self.add_to_cart_button.click()

    def goto_cart(self):

        self.cart_link.click()
