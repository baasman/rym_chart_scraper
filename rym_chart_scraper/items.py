# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class TopAlbumChartItem(Item):
    Artist = Field()
    Album = Field()
    Chart_year = Field()
    Genre = Field()
    RYM_rating = Field()
    Ratings = Field()
    Reviews = Field()
    Date = Field()
