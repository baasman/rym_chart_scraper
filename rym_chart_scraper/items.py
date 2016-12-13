# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class TopAlbumChartItem(Item):
    Artist = Field()
    Album = Field()
    Chart_year = Field()
    Genre = Field()
    RYMRating = Field()
    Ratings = Field()
    Reviews = Field()
    Date = Field()


class WorstAlbumChartItem(Item):
    Artist = Field()
    Album = Field()
    Chart_year = Field()
    Genre = Field()
    RYMRating = Field()
    Ratings = Field()
    Reviews = Field()
    Date = Field()
