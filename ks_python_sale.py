"""
Yazar: Kadir KAYA
Bu script; kitapsepeti sitesindeki python aramasi yapildiginda satista olan kitaplari kazir.
"""
from models.classes import KitapSepetiCategory, KitapSepetiProduct

base_url = "https://www.kitapsepeti.com"
ks = KitapSepetiCategory(base_url)
product_links = []

page = 1
category_url = "/arama?q=python&stock=1"
ks.set_pagination_limit(f"{category_url}")
print(f"pagination_limit setted: {ks.category_pagination_count}")
while True:
    links = ks.get_all_product_links(f"{category_url}&pg={page}")
    if not links:
        print("this page has no product!")
        break
    print(f"{len(links)} product links scraped from {category_url}&pg={page}")
    product_links.extend(links)
    page += 1

print(f"category link: {category_url}&pg={page}, product count: {len(product_links)}")
product_links = [base_url+link for link in product_links]
books = []
print(f"Product pages are scraping now...")
for product in product_links:
    p = KitapSepetiProduct(product)
    book = p.get_product()
    print(book.__dict__)
    books.append(book)
print(f"total books: {len(books)} in {base_url}{category_url}")