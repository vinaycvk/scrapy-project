import scrapy
from brandscraper.items import BrandscraperItem


class ProductscraperSpider(scrapy.Spider):
    name = "productscraper"
    allowed_domains = ["www.hatsu.in"]
    start_urls = ["https://www.hatsu.in/collections/wall-lamp"]

    
    def parse(self, response):
        relative_urls = response.css('.full-unstyled-link::attr(href)').getall()

        for relative_url in relative_urls:
            full_url = response.url + relative_url
            
            yield response.follow(full_url, callback = self.parse_product)
            
        next_url = response.css('a.pagination__item.pagination__item--prev.pagination__item-arrow.link.motion-reduce::attr(href)').get()
        
        if next_url:
            full_url = response.url + next_url
            yield response.follow(full_url, callback = self.parse)


    def parse_product(self, response):
        
        productItem = BrandscraperItem()

        productItem['productName'] = response.xpath('//div[@class="product__title"]//h1/text()').get()
        productItem['productDescription'] = response.xpath('//div[@class="product__description rte quick-add-hidden"]//p/text()').get() 
        productItem['sourceURL'] = response.url
        productItem['imageName1'] = productItem['productName']
        productItem['imageURL1'] = response.xpath('//div[@class="product__media media media--transparent"]//img/@src').get()
        productItem['MRP_priceValue'] = response.css('span.money::text').get()
        productItem['WK_priceValue'] = response.css('span.money::text').get()

        if not productItem['productDescription']:
            productItem['productDescription'] = response.xpath('//div[@class="product__description rte quick-add-hidden"]//p/span/text()').get()


        yield productItem 
