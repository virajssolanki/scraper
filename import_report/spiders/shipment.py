import scrapy
#scrapy crawl --nolog --output -:json shipment

class ScrapeTableSpider(scrapy.Spider):
    name = 'shipment'
    allowed_domains = ['https://import.report/record/2020092246672']
    start_urls = ['https://import.report/record/2018101928062']
 
    def start_requests(self):
        urls = [
            'https://import.report/record/2018101928062',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][3]/tr'):
            yield {
                'first' : row.xpath('td[1]//text()').extract_first(),
                'last': row.xpath('td[2]//text()').extract_first(),
                'handle' : row.xpath('td[3]//text()').extract_first(),
            }

        # data = response.xpath('//table//text()').extract()
        # cargo = response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][3]//text()').extract()
        # print(cargo)

        # vessel_port = response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][1]')
        # bol = response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][5]')
        
        
        
        
        
        
        
        # /table[@class="table"][3]/tr[1]/td[3]/text()
        # print(details)
        # for row in response.xpath('//*[@class="column"]//tbody/tr'):
        # print(details.xpath('/table[@class="table"][3]/tbody/tr[1]/td[3]').getall())
        # vessel_port = details.xpath('.//table[@class="table"][1]/tr[1]/td[1]')
        # cargo = details.xpath('.//table[@class="table"][1]/tr[2]/td[1]')
        # bill = details.xpath('.//table[@class="table"][1]/tr[3]/td[1]')