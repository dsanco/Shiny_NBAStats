from scrapy import Spider
from nba_stats.items import NbaStatsItem

class NBAStatsSpider(Spider):
    name = 'nba_stats_spider'
    allowed_domains = ['www.basketball-reference.com']
    start_urls = ['https://basketball-reference.com/leagues/NBA_2020_per_game.html']

    def parse(self, response):
        # tr @class = "full_table" is the class for the actual player stats
        rows = response.xpath('//div[@class="overthrow table_container"]/table/tbody/tr[@class="full_table"]')

        # Loop thru all player rows 
        for row in rows:
            # Assign each cell to a variable
            Name = row.xpath('./td[1]/a/text()').extract_first()
            Pos = row.xpath('./td[2]/text()').extract_first()
            Age = row.xpath('./td[3]/text()').extract_first()
            Team = row.xpath('./td[4]/a/text()').extract_first()
            Games = row.xpath('./td[5]/text()').extract_first()
            GamesStarted = row.xpath('./td[6]/text()').extract_first()
            MinutesPlayed = row.xpath('./td[7]/text()').extract_first()
            FGM = row.xpath('./td[8]/text()').extract_first()
            FGA = row.xpath('./td[9]/text()').extract_first()
            FGP = row.xpath('./td[10]/text()').extract_first()
            ThreePM = row.xpath('./td[11]/text()').extract_first()
            ThreePA = row.xpath('./td[12]/text()').extract_first()
            ThreePP = row.xpath('./td[13]/text()').extract_first()
            TwoPM = row.xpath('./td[14]/text()').extract_first()
            TwoPA = row.xpath('./td[15]/text()').extract_first()
            TwoPP = row.xpath('./td[16]/text()').extract_first()
            eFGP = row.xpath('./td[17]/text()').extract_first()
            FTM = row.xpath('./td[18]/text()').extract_first()
            FTA = row.xpath('./td[19]/text()').extract_first()
            FTP = row.xpath('./td[20]/text()').extract_first()
            ORB = row.xpath('./td[21]/text()').extract_first()
            DRB = row.xpath('./td[22]/text()').extract_first()
            TRB = row.xpath('./td[23]/text()').extract_first()
            AST = row.xpath('./td[24]/text()').extract_first()
            STL = row.xpath('./td[25]/text()').extract_first()
            BLK = row.xpath('./td[26]/text()').extract_first()
            TOV = row.xpath('./td[27]/text()').extract_first()
            PF = row.xpath('./td[28]/text()').extract_first()
            PTS = row.xpath('./td[29]/text()').extract_first()

            # Initialize NBAStatsItem for each instance of player stats
            Player = NbaStatsItem()
            Player['Name'] = Name
            Player['Pos'] = Pos
            Player['Age'] = Age
            Player['Team'] = Team
            Player['Games'] = Games
            Player['GamesStarted'] = GamesStarted
            Player['MinutesPlayed'] = MinutesPlayed
            Player['FGM'] = FGM
            Player['FGA'] = FGA
            Player['FGP'] = FGP
            Player['ThreePM'] = ThreePM
            Player['ThreePA'] = ThreePA
            Player['ThreePP'] = ThreePP
            Player['TwoPM'] = TwoPM
            Player['TwoPA'] = TwoPA
            Player['TwoPP'] = TwoPP
            Player['eFGP'] = eFGP
            Player['FTM'] = FTM
            Player['FTA'] = FTA
            Player['FTP'] = FTP
            Player['ORB'] = ORB
            Player['DRB'] = DRB
            Player['TRB'] = TRB
            Player['AST'] = AST
            Player['STL'] = STL
            Player['BLK'] = BLK
            Player['TOV'] = TOV
            Player['PF'] = PF 
            Player['PTS'] = PTS
            yield Player



