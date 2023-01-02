import logging

import scrapy
from scrapy.http.response.html import HtmlResponse

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """
    Initializes the `pep` spider. Parses links from the
    `https://peps/python/org/` page to individual peps pages.
    On these pages, it collect information about
    the number, name and status of the pep.
    """
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response: HtmlResponse) -> None:
        """
        Parses links to individual peps pages and navigate to them
        by calling the `parse_pep` method.
        """
        try:
            for pep_row in response.css(
                    'section[id="numerical-index"] tbody tr'):
                pep_link = self.start_urls[0] + pep_row.css(
                    'td a::attr(href)').get().lstrip('/')
                yield response.follow(pep_link, callback=self.parse_pep)
        except Exception as error:
            logging.error(f'There was a problem with parsing. Error: {error}',
                          exc_info=True, stack_info=True)

    def parse_pep(self, response: HtmlResponse) -> PepParseItem:
        """
        Parses information about the number, name and status from
        individual pep pages and creates `PepParseItem` objects.
        """
        try:
            pep_text = response.css(
                'h1[class="page-title"]::text').get().split('–')
            data = {
                'number': int(pep_text[0].replace('PEP', '').strip()),
                'name': pep_text[1].strip(),
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text').get()
            }
            yield PepParseItem(data)
        except Exception as error:
            logging.error(f'There was a problem whith parsing. Error: {error}',
                          exc_info=True, stack_info=True)
