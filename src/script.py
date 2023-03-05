from comcrawl import IndexClient

def get_urls(crawled_site):
    archives = ["2020-05", "2020-10", "2020-16", "2020-24", "2020-29","2020-34", "2020-40", "2020-45", "2020-50"]
    r = []
    for i in archives:
        client = IndexClient([i])
        client.search(crawled_site)
        c = 0
        urls = []
        for res in client.results:
            if res['status'] == '200':
                url = res['url']
                if (url.find('covid') > -1 or url.find('coronavirus') > -1 or url.find('pandemic') > -1) and (url.find('money') > -1 
                                                                                                    or url.find('economy') > -1 
                                                                                                    or url.find('economic') > -1
                                                                                                    or url.find('inflation') > -1 
                                                                                                    or url.find('stimulus') > -1 
                                                                                                    or url.find('business') > -1
                                                                                                    or url.find('stimulus') > -1):
                    urls.append(url)
        r.append(urls)
    return r


find_in = ["cnn.com/2020/*", "theguardian.com/world/2020", "theguardian.com/us-news/2020/*", "www.foxbusiness.com/*"]
archive = ["2020-05", "2020-10", "2020-16", "2020-24", "2020-29","2020-34", "2020-40", "2020-45", "2020-50"]
with open("results.csv", "w") as res_file:
    res_file.write("ARCHIVE,URL\n")
    for i in find_in:
        r = get_urls(i)
        for arc in range(len(r)):
            for url in r[arc]:
                res_file.write(f"{archive[arc]},{url}\n")

