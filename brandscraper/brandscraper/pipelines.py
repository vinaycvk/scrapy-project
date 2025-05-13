# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BrandscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        productName = adapter.get("productName", "Unknown Product")
        brandName = 'Hatsu'

        adapter["metaTitle"] = f'Buy {brandName} {productName} Online - Wishkarma'
        adapter["metaDescription"] = f'Buy {brandName} at best price in India from Wishkarma. Shop from Lights and Living {productName} dealers, suppliers and wholesalers online.'


        adapter.setdefault("MRP_priceCurrency", "INR")
        adapter.setdefault("MRP_priceDiscountPercent", 0)
        adapter.setdefault("MRP_taxName", "GST")
        adapter.setdefault("MRP_taxPercent", 18)

        # Default values for WK Pricing
        adapter.setdefault("WK_priceCurrency", "INR")
        adapter.setdefault("WK_priceDiscountPercent", 0)
        adapter.setdefault("WK_taxName", "GST")
        adapter.setdefault("WK_taxPercent", 18)
        
        return item