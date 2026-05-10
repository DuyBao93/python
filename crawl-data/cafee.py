import index

def check_value(s, w):
    return s.find(w)

def crawl_data():
    response = index.requests.get("https://giacaphe.com/gia-ca-phe-noi-dia/")
    soup = index.BeautifulSoup(response.content, "html.parser")
    allData = soup.find("tbody")
    mainData = soup.find("main")
    averagePrice = mainData.find("span", class_="_trung-binh-gia").text
    averagePriceChanges = mainData.find("span", class_="price_change").text
    datetimeVN = index.datetime.now(index.tzVN)
    if check_value(averagePriceChanges, "-") >= 0:
        resultAverage = '{:>30}\t{}\t{}'.format(index.colored("Trung Bình Giá", 'white'),
                                            index.colored(index.split_space(averagePrice), 'light_yellow'),
                                            index.colored("\u2193" + 
                                                          index.split_space(averagePriceChanges), 'red'))
    else:
        resultAverage = '{:>30}\t{}\t{}'.format(index.colored("Trung Bình Giá", 'white'),
                                            index.colored(index.split_space(averagePrice), 'light_yellow'),
                                            index.colored("\u2191" + 
                                                          index.split_space(averagePriceChanges), 'light_green'))

    print(index.colored("======================================================",'yellow'))
    print('{:>44}'.format(index.colored("Giá Cafe Nội Địa", 'light_cyan')))
    print('{:>46}'.format(index.colored(datetimeVN.strftime("%Y-%m-%d %H:%M:%S"),'white')))
    print(resultAverage)
    print(index.colored("======================================================",'yellow'))
    for data in allData.findChildren("tr"):
        name = index.split_space(data.find("td", class_="gnd_market").text)
        priceData = index.split_space(data.find("td", class_="gnd-gia").text)
        print('{:20} \t\t'.format(index.colored(name,'white')), end='')

        priceChangesData = data.find("span", class_="price_change")
        if priceChangesData == None:
            priceChangesData =  ""
        else:
            if check_value(priceChangesData.text, "-") >= 0:
                priceChangesData = index.colored("\u2193" + 
                                                 index.split_space(priceChangesData.text), 'red')
            else:
                priceChangesData = index.colored('\u2191' + 
                                                 index.split_space(priceChangesData.text), 'light_green')
        result = '{}\t\t{}'.format(index.colored(priceData, 'light_yellow'),priceChangesData)
        print(result, end='')
        print("")

if __name__ == "__main__":
    index.os.system('clear')
    crawl_data()
    while True:
        index.time.sleep(600)
        index.os.system('clear')
        crawl_data()