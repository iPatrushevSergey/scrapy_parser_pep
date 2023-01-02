import scrapy


class PepParseItem(scrapy.Item):
    """
    Based on the data coming from the parser, it creates
    Items objects, while validating fields. Then the objects
    fall into pipelines.
    """
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
