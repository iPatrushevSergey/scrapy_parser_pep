import scrapy

from pep_parse.configs import configure_logging
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        configure_logging()
        for pep_row in response.css('section[id="numerical-index"] tbody tr')[:6]:
            pep_link = self.start_urls[0] + pep_row.css('td a::attr(href)').get().lstrip('/')
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_text = response.css('h1[class="page-title"]::text').get().split('–')
        data = {
            'number': int(pep_text[0].replace('PEP', '').strip()),
            'name': pep_text[1].strip(),
            'status': response.css('dt:contains("Status") + dd abbr::text').get()
        }
        yield PepParseItem(data)
