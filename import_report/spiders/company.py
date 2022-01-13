import scrapy
#scrapy crawl --nolog --output -:json shipment

class ScrapeTableSpider(scrapy.Spider):
    name = 'company'
    allowed_domains = ['https://import.report/']
    
    def start_requests(self):
        home_page = f'https://import.report/search/'
        companies = ['Volkswagen', 'General Motors', 'Nissan', 'Toyota', 'Ford']
        urls = [ home_page+company for company in companies ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        vin_numbers = []
        print(response.xpath('/html/body/div/div/div[5]/div[2]'))
        # for row in response.xpath('//div[@class="panel panel-default"][4]/div[@class="panel-body"]/table[@class="table"]/tbody/tr'):
        #     print(row)
        #     vins = row.xpath('td[1]//text()').extract_first()
            # [ vin_numbers.append(vin) if vin not in vin_numbers and self.validate_vin(vin) else vin_numbers for vin in vins ]
    #     if vin_numbers:
    #         vessel_and_port = {}
    #         for row in response.xpath('//div[@class="panel panel-default"][2]/table[@class="table"][1]/tr'):
    #             key = row.xpath('td[1]//text()').extract_first()
    #             value = row.xpath('td[2]//text()').extract_first()
    #             vessel_and_port[key] = value
                
    #         # print(vessel_and_port)
    #             # [ vin_numbers.append(vin) if vin not in vin_numbers and self.validate_vin(vin) else vin_numbers for vin in vins ]        
    #         yield {
    #             'vessel and port': vessel_and_port, 
    #             'vin numbers' : vin_numbers
    #         }


    # def validate_vin(self, data):
    #     ''' return true if vin is valid '''

    #     ILLEGAL_ALL = ['I', 'O', 'Q']
    #     ILLEGAL_TENTH = ['U','Z','0']

    #     if len(data) == 17:
    #         vin = data.upper()

    #         for char in ILLEGAL_ALL:
    #             if char in vin:
    #                 return False
    #         if vin[10] in ILLEGAL_TENTH:
    #             return False
    #     else:
    #         return False
    #     return True



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