# encoding: utf-8
import os
from sys import argv, stdout
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
ICON_DEFAULT = 'pandas-icon.png'
path = os.path.abspath('.')


class pandas_search(object):
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        self.driver = webdriver.Chrome(
            f'{path}/chromedriver', options=option)

    def search(self, keyword):
        query = keyword
        self.driver.get(f'https://pandas.pydata.org/pandas-docs/stable/search.html?q={query}&check_keywords=yes&area=default')
        wait = WebDriverWait(self.driver, 25)
        res = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="search-results"]/ul/li[10]/a')))

        def get_results(i):
            i = i + 1
            result = res.find_element_by_xpath(
                f'//*[@id="search-results"]/ul/li[{i}]/a')
            link = result.get_attribute('href')
            text = result.text
            result = {"Title": text, "Link": link}
            return result
        result_list = [get_results(i) for i in range(10)]
        self.driver.quit()
        return result_list


def makeItem(query, url, name):
    item = {
        'uid': url,
        'title': name,
        'subtitle': url,
        'arg': url,
        'autocomplete': query,
        'icon': {
            'path': 'icon.png'
        }
    }
    return item


def makeReturn(items):
    out = {
        'items': items
    }
    return out


def main():
    pandas = pandas_search()
    arg_c = len(argv)
    if arg_c <= 1:
        return makeReturn([])
    query = argv[1]
    if not query:
        return makeReturn([])
    results = pandas.search(query)
    items = [makeItem(query, results[i]['Link'], results[i]['Title'])
             for i in range(10)]
    out = makeReturn(items)
    return json.dumps(out, indent=4) + '\n'


if __name__ == '__main__':
    data = main()
    stdout.write(data)
