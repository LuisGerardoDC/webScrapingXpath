import requests
import lxml.html as html

XPATH_LINK_TO_ARTICLE = '//h2[contains(@class,"Headline") or contains(@class, "Article")]/a[not(@class)]/@href'
XPATH_TITLE ='//h1[@class="DefaultTitle"]/text()'
XPATH_SUMMARY ='//h2[@class="DefaultSubtitle"]/text()'
XPATH_BODY = '//div[@class="page-internal-content"]/section/p/text()'
HOME_URL = 'https://larepublica.pe/'

def parse_home():
    try:
        response = requests.get(HOME_URL)
        if(response.status_code == 200):
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)
            print(parsed)
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)

            print(len(links_to_notices))
            print(links_to_notices)
        else:
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == "__main__":
    run()