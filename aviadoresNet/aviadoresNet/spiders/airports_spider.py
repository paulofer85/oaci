import scrapy
import logging
import html2text
import lxml.etree
import lxml.html
from scrapy.selector import Selector


class AirportSpider(scrapy.Spider):
    name = "airports"

    def start_requests(self):
        urls = [
            'http://www.aviadores.net/ICAO-AD.htm',
            'http://www.aviadores.net/ICAO-E.htm',
            'http://www.aviadores.net/ICAO-F.htm',
            'http://www.aviadores.net/ICAO-GH.htm',
            'http://www.aviadores.net/ICAO-K1.htm',
            'http://www.aviadores.net/ICAO-K2.htm',
            'http://www.aviadores.net/ICAO-L.htm',
            'http://www.aviadores.net/ICAO-MN.htm',
            'http://www.aviadores.net/ICAO-O.htm',
            'http://www.aviadores.net/ICAO-PR.htm',
            'http://www.aviadores.net/ICAO-S1.htm',            
            'http://www.aviadores.net/ICAO-S2.htm',            
            'http://www.aviadores.net/ICAO-TU.htm',            
            'http://www.aviadores.net/ICAO-VW.htm',            
            'http://www.aviadores.net/ICAO-Y.htm',            
            'http://www.aviadores.net/ICAO-Z.htm',            
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        rows = response.xpath(('//tr[contains(@valign, "bottom")]'))
        d = dict()
        for row in rows:
            columns = row.xpath(('td/font/font/text()')).extract()
            lat =  (columns[2] if len(columns) > 2 else '-') + (columns[3] if len(columns) > 3 else '-') + "°" + (columns[4] if len(columns) > 4 else '-')
            long =  (columns[5] if len(columns) > 5 else '-') + (columns[6] if len(columns) > 6 else '-') + "°" + (columns[7] if len(columns) > 7 else '-')

            d.update({columns[0]:
                        {
                            'name': columns[1],                
                            'lat': lat,                
                            'long': long
                        }           
            })
        return d




