# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbaStatsItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Pos = scrapy.Field()
    Age = scrapy.Field()
    Team = scrapy.Field()
    Games = scrapy.Field()
    GamesStarted = scrapy.Field()
    MinutesPlayed = scrapy.Field()
    FGM = scrapy.Field()
    FGA = scrapy.Field()
    FGP = scrapy.Field()
    ThreePM = scrapy.Field()
    ThreePA = scrapy.Field()
    ThreePP = scrapy.Field()
    TwoPM = scrapy.Field()
    TwoPA = scrapy.Field()
    TwoPP = scrapy.Field()
    eFGP = scrapy.Field()
    FTM = scrapy.Field()
    FTA = scrapy.Field()
    FTP = scrapy.Field()
    ORB = scrapy.Field()
    DRB = scrapy.Field()
    TRB = scrapy.Field()
    AST = scrapy.Field()
    STL = scrapy.Field()
    BLK = scrapy.Field()
    TOV = scrapy.Field()
    PF = scrapy.Field()
    PTS = scrapy.Field()

    pass
