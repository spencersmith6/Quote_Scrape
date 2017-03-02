
### https://www.goodreads.com/quotes

from bs4 import BeautifulSoup
import urllib2
import re
import pickle



def fetch(url, delay=(2,5)):
    #time.sleep(random.randint(delay[0], delay[1]))
    try:
        req = urllib2.Request(url, headers={'User-Agent': 'Not A Hacker'})
        response = urllib2.urlopen(req)
    except:
        return BeautifulSoup('', "html.parser"), ''
    text = response.read()
    soup = BeautifulSoup(text, 'html.parser')
    return soup, text

base = "https://www.goodreads.com/"
soup, html = fetch("https://www.goodreads.com/quotes")

quote_list = []
for i in range(98):
    all_quotes = [i for i in soup.find_all(class_='quoteText')]

    for el in all_quotes:
        list = [i for i in el]
        if len(list)==2:
            quote_obj = [x.strip() for x in re.findall("[a-z A-Z ';:,.?! C-j]+", list[0]) if x.strip() != ""]
            if len(quote_obj)==1:
                person_obj = re.findall("[a-z A-Z ';:,.?! C-j]+", list[1].get_text().strip(" "))
                if len(person_obj) == 1:
                    quote_list.append((quote_obj[0], person_obj[0].strip()))

    soup, html = fetch(base +str(soup.find_all(class_='next_page')[0]["href"]))


with open('quotes.txt', 'wb') as fp:
    pickle.dump(quote_list, fp)

with open('quotes_txt.txt', "w") as f:
    for i in quote_list:
        f.write("%s\n" %str(i))


print len(quote_list)
