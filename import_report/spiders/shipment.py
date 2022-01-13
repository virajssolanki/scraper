import scrapy
#scrapy crawl --nolog --output -:json shipment

class ScrapeTableSpider(scrapy.Spider):
    name = 'shipment'
    allowed_domains = ['https://import.report/record/2020092246672']

    def start_requests(self):
        urls = [
            'https://import.report/record/2019091354400',
            'https://import.report/record/2020092527733',
            'https://import.report/record/2018101928062',
            'https://import.report/record/20200929103670',
            'https://import.report/record/2020092915481',
            'https://import.report/record/2020092816969',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        vin_numbers = []
        for row in response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][3]/tr'):
            vins = row.xpath('td[3]//text()').extract_first().split()
            [ vin_numbers.append(vin) if vin not in vin_numbers and self.validate_vin(vin) else vin_numbers for vin in vins ]
        
        if vin_numbers:
            vessel_and_port = {}
            for row in response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][1]/tr'):
                key = row.xpath('td[1]//text()').extract_first()
                value = row.xpath('td[2]//text()').extract_first()
                vessel_and_port[key] = value
                
            # print(vessel_and_port)
                # [ vin_numbers.append(vin) if vin not in vin_numbers and self.validate_vin(vin) else vin_numbers for vin in vins ]        
            yield {
                'vessel and port': vessel_and_port, 
                'vin numbers' : vin_numbers
            }


    def validate_vin(self, data):
        ''' return true if vin is valid '''

        ILLEGAL_ALL = ['I', 'O', 'Q']
        ILLEGAL_TENTH = ['U','Z','0']

        if len(data) == 17:
            vin = data.upper()

            for char in ILLEGAL_ALL:
                if char in vin:
                    return False
            if vin[10] in ILLEGAL_TENTH:
                return False
        else:
            return False
        return True



            # yield row.xpath('td[3]//text()').extract_first()
            #{
                # 'first' : row.xpath('td[1]//text()').extract_first(),
                # 'last': row.xpath('td[2]//text()').extract_first(),
            #     row.xpath('td[3]//text()').extract_first(),
            # }

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