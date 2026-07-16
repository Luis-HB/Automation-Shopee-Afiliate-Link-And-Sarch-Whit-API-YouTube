class ShopeeProductService:

    def __init__(self):
        self.client = ShopeeClient()

    def get_item(self, item_id):

        return self.client.get(

            "/api/v2/product/get_item_base_info",

            {
                "item_id_list": [item_id]
            }

        )