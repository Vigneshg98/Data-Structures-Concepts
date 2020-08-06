import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

internal_urls = set()
external_urls = set()
total_urls_visited = 0


def downloadFile(url, fileName):
    with open(fileName, "wb") as file:
        response = requests.get(url)
        file.write(response.content)


def is_valid(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_website_links(url):
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            continue
        if href in internal_urls:
            continue
        if domain_name not in href:
            if href not in external_urls:
                external_urls.add(href)
            continue
        urls.add(href)
        internal_urls.add(href)
    return urls


def crawl(url, max_urls=50):
    global total_urls_visited
    total_urls_visited += 1
    links = get_all_website_links(url)
    for link in links:
        if total_urls_visited > max_urls:
            break
        crawl(link, max_urls=max_urls)


if __name__ == "__main__":
    
    # "http://palakkadcooking.blogspot.com/p/traditional-palakkad-recipes.html"
    url = input()
    # to set a limit for number of urls to get downloaded, if not set, default limit is 50
    max_urls = 30

    crawl(url, max_urls=max_urls)

    print("Total Internal links:", len(internal_urls))
    print("Total External links:", len(external_urls))
    print("Total URLs:", len(external_urls) + len(internal_urls))

    domain_name = urlparse(url).netloc

    with open(f"{domain_name}_internal_links.txt", "w") as f:
        for internal_link in internal_urls:
            print(internal_link.strip(), file=f)

    with open(f"{domain_name}_external_links.txt", "w") as f:
        for external_link in external_urls:
            print(external_link.strip(), file=f)

    for url in internal_urls :
      dish = url.split("/")[-1]
      if dish != "" and dish != " " and dish.find(".html") != -1 :
        downloadFile(url, dish)
      # break 
    print("Files downloaded successfully.")