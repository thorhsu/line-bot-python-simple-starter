
from pyquery import PyQuery
# 貨幣


class Currency:
    # 定義貨幣屬性: 名稱name、銀行買入價bid、銀行賣出價offer
    def __init__(self, n, b, o):
        self.name = n
        self.bid = b
        self.offer = o

# 貨幣爬蟲


class CurrencyCrawler:
    # 貨幣爬蟲屬性: 目標網址url(https://rate.bot.com.tw/xrt?Lang=zh-TW)、爬取的資料data
    # 貨幣爬蟲函數: 爬取資料fetch_data、取得指定貨幣資訊get_data
    def __init__(self):
        self.url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
        # self.data = {'日圓': Currency, '美金': Currency}
        self.data = {}
    #抓取即時資料 
    def fetch_data(self):
        #爬取目標網址
        html = PyQuery(self.url)
        #篩選資料出來
        names = html('div.hidden-phone.print_show').text().split()
        #篩選出銀行買入價格
        #<td data-table="本行現金買入" class="rate-content-cash text-right print_hide">30.42</td>
        bids = html('td.rate-content-cash.text-right[data-table="本行現金買入"]').text().split()

        #篩選出銀行賣出價格
        #<td data-table="本行現金賣出" class="rate-content-cash text-right print_hide">31.11</td>
        offers = html('td.rate-content-cash.text-right[data-table="本行現金賣出"]').text().split()
        
        print(names)
        print(bids)
        print(offers)
        # 定義價格的索引為0
        price_index = 0
        for i, name in enumerate(names):
            if i % 2 == 0:
                self.data[name] = Currency(name, bids[price_index], offers[price_index])
            else:
                print(name[1: len(name) - 1])
                self.data[name[1: len(name) - 1]] = Currency(name[1: len(name) - 1], bids[price_index], offers[price_index])
                price_index += 1

    #取得資料
    def get_data(self, name):
        try:
            return '{} 銀行買入價:{} 銀行賣出價: {}'.format(
                name, self.data[name].bid, self.data[name].offer
            )
            # return '%s 銀行買入價:%s 銀行賣出價: %s' %(
            #     name, self.data[name].bid, self.data[name].offer
            # )
        except:
            return '查詢不到%s' %(name)


# ==============測試================    
cw = CurrencyCrawler()
#爬取即時資料
cw.fetch_data()
#取得貨幣報告
print(cw.get_data('usd'.upper()))
