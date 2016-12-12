from scrapy import Spider, Request
from rym_chart_scraper.utility import find_between, listToString
from rym_chart_scraper.items import TopAlbumChartItem
from datetime import datetime


class TopAlbumChartSpider(Spider):
    name = "top_music_charts"
    allowed_domains = ['rateyourmusic.com']

    start_urls = [
        "https://rateyourmusic.com/charts/top/album/all-time"
    ]

    n_pages = 1

    def parse(self, response):

        for album, stats in zip(response.css('div.chart_main'),
                                response.css('div.chart_stats')):

            # chart details
            chart_detail_l1 = album.css(
                'div.chart_details span.chart_detail_line1')
            chart_detail_l2 = album.css(
                'div.chart_details div.chart_detail_line2')
            chart_detail_l3 = album.css(
                'div.chart_details div.chart_detail_line3')

            # chart stats
            cstats = [find_between(i, "<b>", "</b>") for i in
                      stats.css('a').extract_first().split("|")]

            item = TopAlbumChartItem()
            item['Artist'] = chart_detail_l1.css(
                'a.artist::text').extract_first()
            item['Album'] = chart_detail_l2.css(
                'a.album::text').extract_first()
            item['Chart_year'] = chart_detail_l2.css(
                'span.chart_year::text').extract_first()
            item['Genre'] = listToString(chart_detail_l3.
                                         css('span.chart_genres').css(
                                             'a.genre::text').extract())
            item['RYMRating'] = cstats[0]
            item['Ratings'] = cstats[1]
            item['Reviews'] = cstats[2]
            item['Date'] = datetime.now().strftime('%Y-%m-%d')
            yield item

        next_page = response.css('a.navlinknext')[0].css(
            'a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            self.n_pages += 1
            if self.n_pages < 31:
                yield Request(next_page, callback=self.parse)
