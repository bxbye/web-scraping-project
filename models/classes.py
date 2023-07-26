import requests
from bs4 import BeautifulSoup

class Book:
    def __init__(self, title, publisher, author, price) -> None:
        self.title = title
        self.publisher = publisher
        self.writers = author
        self.price = price
    def to_dict(self):
        return {
            "title": self.title,
            "publisher": self.publisher,
            "writers": self.writers,
            "price": self.price
        }

# base class
class ProductPage:
    def __init__(self, link) -> None:
        self.link = link
    def get_product(self):
        # scrap the link, create a Book obj, return Book.
        pass
# kitapyurdu website's product page scraping
class KitapYurduProduct(ProductPage):
    def __init__(self, link) -> None:
        super().__init__(link)
    def get_product(self):
        # kitapyurdu.com'daki product page'e gore scraping uygula. Book objesi olustur ve return et.
        #print(self.link)
        # http request for product page
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        headers = {"User-Agent": user_agent}
        response = requests.get(self.link, headers=headers)
        if response.status_code != 200:
            print(f"Error: url could't responses. status_code: {response.status_code}")
            return None
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                # scrap title
                h1_tag = soup.find("h1", class_="pr_header__heading")
                h1_text = h1_tag.text.strip()
                span_tag = h1_tag.span
                # check if h1_tag has a span tag
                if span_tag:
                    span_text = span_tag.text.strip()
                    title = h1_text + " (" + span_text + ")"
                else:
                    title = h1_text
                #print(f"title: {title}")
            except:
                print(f"scrap title error: {h1_tag}")
                title = "Unknown"
            try:                
                # scrap publisher
                div_publisher = soup.find("div", class_="pr_producers__publisher")
                publisher = div_publisher.div.a.text.strip()
                #print(f"publisher: {publisher}")
            except:
                print(f"scrap publisher error: {div_publisher}")
                publisher = "Unknown"
            try:    
                # scrap author
                div_author = soup.find("div", class_="pr_producers__manufacturer")
                author = div_author.div.a.text.strip()
                #print(f"author: {author}")
            except:
                print(f"scrap author error: {div_author}")
                author = "Unknown"
            try:
                # price
                div_price = soup.find("div", class_="price__item")
                price = div_price.text.strip().replace(".","").replace(",", ".")
                price = float(price)
                #print(f"price: {price}")
            except:
                print(f"scrap price error: {div_price}")
                price = 0.00
            # create Book object and return it
            return Book(title, publisher, author, price)
# kitapsepeti website's product page scraping
class KitapSepetiProduct(ProductPage):
    def __init__(self, link) -> None:
        super().__init__(link)
    def get_product(self):
        # kitapyurdu.com'daki product page'e gore scraping uygula. Book objesi olustur ve return et.
        #print(self.link)
        # http request for product page
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        headers = {"User-Agent": user_agent}
        response = requests.get(self.link, headers=headers)
        if response.status_code != 200:
            print(f"Error: url could't responses. status_code: {response.status_code}")
            return None
        else:
            soup = BeautifulSoup(response.text, "html.parser")
            try:
                # scrap title
                h1_tag = soup.find("h1", {"id": "productName"})
                h1_text = h1_tag.text.strip()
                title = h1_text
                #print(f"title: {title}")
            except:
                print(f"scrap title error: {h1_tag}")
                title = "Unknown"
            try:                
                # scrap publisher
                div_publisher = soup.find("a", {"class": "product-brand"})
                publisher = div_publisher.text.strip()
                #print(f"publisher: {publisher}")
            except:
                print(f"scrap publisher error: {div_publisher}")
                publisher = "Unknown"
            try:    
                # scrap author
                div_author = soup.find("a", {"id": "productModelText"})
                author = div_author.text.strip()
                #print(f"author: {author}")
            except:
                print(f"scrap author error: {div_author}")
                author = "Unknown"
            try:
                # price
                div_price = soup.find("span", {"class":"product-price"})
                price = div_price.text.strip().replace(".","").replace(",", ".")
                price = float(price)
                #print(f"price: {price}")
            except:
                print(f"scrap price error: {div_price}")
                price = 0.00
            # create Book object and return it
            return Book(title, publisher, author, price)

# base class
class CategoryPage:
    def __init__(self, base_link) -> None:
        self.base_link = base_link
        print(f"CategoryPage: {base_link}")
    def get_all_product_links(self,category_url):
        # make http request, scrap html codes.
        # return product_links in given category_url page.
        pass
    def set_pagination_limit(self):
        pass
# kitapyurdu.com website's category page's operations.
class KitapYurduCategory(CategoryPage):
    def __init__(self, base_link) -> None:
        super().__init__(base_link)
    def get_all_product_links(self, category_url):
        product_links = []
        full_url = self.base_link + category_url
        print(f"full_category_url: {full_url}")
        # make http request, scrap html codes.
        try:
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            headers = {"User-Agent": user_agent}
            response = requests.get(full_url, headers=headers)
            if response.status_code != 200:
                print(f"Error: url could't responses. status_code: {response.status_code}")
            else:
                soup = BeautifulSoup(response.text, "html.parser")
                product_list_tag = soup.find("div", {"id":"product-table"})# if exist its ok(searched item)
                if (product_list_tag):
                    # print("Bu sayfada product list tag mevcuttur.")
                    product_links = [link.get("href") for link in product_list_tag.findAll("a", class_="pr-img-link")]
                else:
                    # print("Bu sayfada product-table tag mevcuttur degildir.")
                    product_not_found_tag = soup.find("div", class_= "product-not-found")
                    #print(product_not_found_tag)
                    if product_not_found_tag:
                        product_links = []
                    else:
                        product_links = [link.get("href") for link in soup.findAll("a", class_="pr-img-link")]
                #print(product_links, len(product_links))
        except Exception as e:
            print(f"Error accured: {e}")
        # return product_links in given category_url page.
        return product_links
# kitapsepeti.com website's category page's operations.        
class KitapSepetiCategory(CategoryPage):
    def __init__(self, base_link) -> None:
        super().__init__(base_link)
        self.category_pagination_count = 0 # for category paginations
    def get_all_product_links(self, category_url):
        # when category page dont have current page, product_list should return empty
        product_links = []
        full_url = self.base_link + category_url
        #print(f"full_category_url: {full_url}")
        # make http request, scrap html codes.
        try:
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            headers = {"User-Agent": user_agent}
            response = requests.get(full_url, headers=headers)
            if response.status_code != 200:
                print(f"Error: url could't responses. status_code: {response.status_code}")
            else:
                soup = BeautifulSoup(response.text, "html.parser")
                # find current_url's page number
                current_page = int(category_url[category_url.index("pg=")+3:])
                print(f"current_page: {current_page}, end_page: {self.category_pagination_count}")
                if (current_page > self.category_pagination_count):
                    product_links = []
                else:
                    product_links = [link.get("href") for link in soup.select('a.image-wrapper.fl.detailLink')]
                #print(product_links, len(product_links))
        except Exception as e:
            print(f"Error accured: {e}")
        return product_links
    # set pagination limit for last category index.
    def set_pagination_limit(self, category_url):
        full_url = self.base_link + category_url
        print(f"set_paginationpage_url: {full_url}")
        try:
            user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            headers = {"User-Agent": user_agent}
            response = requests.get(full_url, headers=headers)
            if response.status_code != 200:
                print(f"Error: url could't responses. status_code: {response.status_code}")
            else:
                soup = BeautifulSoup(response.text, "html.parser")
                # find pagination part
                pagination_tag = soup.find("div", class_="productPager")
                # if page has no pagination a tag not exist in div
                a_tags_in_pagination = pagination_tag.findAll("a", class_="")
                if len(a_tags_in_pagination) > 0:    
                    last_pagination = a_tags_in_pagination[-1].get("href")
                    self.category_pagination_count = int(last_pagination[last_pagination.index("pg=")+3:])
                else:
                    self.category_pagination_count = 1
        except Exception as e:
            print(f"Error accured in let_pagination_limit(): {e}")