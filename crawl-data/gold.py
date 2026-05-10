import index

def crawl_data():
    response = index.requests.get("https://giavangsjc.net/")
    soup = index.BeautifulSoup(response.content, "html.parser")
    allData = soup.find("tbody")
    datetimeVN = index.datetime.now(index.tzVN)

    print(index.colored("=============================================================", 'yellow'))
    print('{:>45}'.format(index.colored("Giá Vàng Việt Nam", 'light_cyan')))
    print('{:>46}'.format(index.colored(datetimeVN.strftime("%Y-%m-%d %H:%M:%S"), 'white')))
    print(index.colored("=============================================================", 'yellow'))
    for data in allData.findChildren("tr"):
        name = index.split_space(data.find("th").text)
        print('{:25} \t\t'.format(index.colored(name, 'white')), end='')
        for priceData in data.findChildren("td"):
            priceChangesData = priceData.find("span")
            up = priceData.find("span", class_="text-success u")
            priceData = priceData.text
            if priceChangesData == None:
                priceData = index.split_space(priceData)
                priceChangesData =  ""
            else:
                priceData = index.split_space(priceData.replace(priceChangesData.text, "", 1))
                if up != None:
                    priceChangesData = index.colored('\u2191' + index.split_space(priceChangesData.text), 'light_green')
                else:
                    priceChangesData = index.colored("\u2193" + index.split_space(priceChangesData.text), 'light_red')
            result = '{}\t{}\t'.format(index.colored(priceData, 'light_yellow'),priceChangesData)
            print(result, end='')
        print("")

if __name__ == "__main__":
    index.os.system('clear')
    crawl_data()
    while True:
        index.time.sleep(60)
        index.os.system('clear')
        crawl_data()