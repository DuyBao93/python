import index
from xml.dom import minidom 
from urllib.request import urlopen

def crawl_data():
    url = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx?b=10"
    soup = minidom.parse(urlopen(url))
    allData = soup.getElementsByTagName('Exrate')
    datetimeVN = index.datetime.now(index.tzVN)
    print(index.colored("=========================================================================", 'yellow'))
    print('{:>55}'.format(index.colored("Ngoại Tệ Việt Nam", 'light_cyan')))
    print('{:>56}'.format(index.colored(datetimeVN.strftime("%Y-%m-%d %H:%M:%S"), 'white')))
    print(index.colored("=========================================================================", 'yellow'))
    print('{:15}\t{:30}\t{:20}\t{:20}\t{:20}'.format(index.colored("Mã", 'white'), 
                                                     index.colored("Tên Ngoại Tệ", 'white'),
                                                     index.colored("Mua Offline", 'white'),
                                                     index.colored("Mua Online ", 'white'),
                                                     index.colored("Giá Bán", 'white')))
    print(index.colored("-------------------------------------------------------------------------", 'yellow'))
    for item in allData:
        currentcyCode = index.colored(index.split_space(item.attributes["CurrencyCode"].value), 'white')
        currentcyName = index.colored(index.split_space(item.attributes["CurrencyName"].value), 'white')
        buy = index.colored(index.split_space(item.attributes["Buy"].value), 'light_yellow')
        transfer = index.colored(index.split_space(item.attributes["Transfer"].value), 'light_yellow')
        sell = index.colored(index.split_space(item.attributes["Sell"].value), 'light_yellow')
        result = '{:15}\t{:30}\t{:20}\t{:20}\t{:20}'.format(currentcyCode, currentcyName, buy, transfer, sell)
        print(result)

if __name__ == "__main__":
    index.os.system('clear')
    crawl_data()
    while True:
        index.time.sleep(300)
        index.os.system('clear')
        crawl_data()