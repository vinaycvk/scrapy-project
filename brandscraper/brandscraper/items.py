# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BrandscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    category = scrapy.Field()
    brandID = scrapy.Field()
    categoryID = scrapy.Field()
    subCategoryID = scrapy.Field()
    productTypeID = scrapy.Field()
    productName = scrapy.Field()
    popularityWeight = scrapy.Field()
    productDescription = scrapy.Field()
    mfrProductNo = scrapy.Field()
    sourceURL = scrapy.Field()
    
    imageName1 = scrapy.Field()
    imageURL1 = scrapy.Field()
    imageCaption1 = scrapy.Field()
    
    imageName2 = scrapy.Field()
    imageURL2 = scrapy.Field()
    imageCaption2 = scrapy.Field()

    metaTitle = scrapy.Field()
    metaDescription = scrapy.Field()
    metaRefresh = scrapy.Field()
    metaCharset = scrapy.Field()
    metaViewport = scrapy.Field()
    metaRobots = scrapy.Field()
    
    MRP_priceCurrency = scrapy.Field()
    MRP_priceValue = scrapy.Field()
    MRP_priceDiscountPercent = scrapy.Field()
    MRP_taxName = scrapy.Field()
    MRP_taxPercent = scrapy.Field()

    WK_priceCurrency = scrapy.Field()
    WK_priceValue = scrapy.Field()
    WK_priceDiscountPercent = scrapy.Field()
    WK_taxName = scrapy.Field()
    WK_taxPercent = scrapy.Field()

    PerUnit_priceCurrency = scrapy.Field()
    pricePerUnit = scrapy.Field()
    pricingUnit = scrapy.Field()
    PerUnit_priceDiscountPercent = scrapy.Field()
    PerUnit_taxName = scrapy.Field()
    PerUnit_taxPercent = scrapy.Field()

    specifications = scrapy.Field()
