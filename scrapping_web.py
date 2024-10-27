import scrapy
import re


class BBItem(scrapy.Item):
    rank = scrapy.Field()
    song = scrapy.Field()
    artist = scrapy.Field()


class BBSpider(scrapy.Spider):
    name = 'bb-top100'
    allowed_domains = ['www.billboard.com']
    start_urls = ['https://www.billboard.com/charts/hot-100']
    

    def parse(self, response):
        items = []
        lis = response.xpath('//div[@class = "o-chart-results-list-row-container"]')
        ranks = lis.xpath('//span[@class = "c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"]/text()').extract()
        songs = lis.xpath('//h3[@class = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"]/text()').extract()
        artists = lis.xpath('//span[@class = "c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"]/text()').extract()
    
        # The Billboard 100 has some interface changes in 2022. The first song entry has slightly different HTML attributes and thus we treat it differently.
        song_first = lis.xpath('//h3[@class = "c-title  a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"]/text()').extract()
        artist_first = lis.xpath('//span[@class = "c-label  a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"]/text()').extract()
    
        items.append(BBItem(rank=ranks[0].strip(), song=song_first[0].strip(), artist=artist_first[0].strip() ))
    
        for i in range(len(lis)-1):
            items.append(BBItem(rank=ranks[i+1].strip(), song=songs[i].strip(), artist=artists[i].strip() ))
                
        return items

    
    
    
    
    