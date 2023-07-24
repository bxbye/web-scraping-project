from models.classes import KitapSepetiCategory, KitapSepetiProduct

base_url = "https://www.kitapsepeti.com"
ks = KitapSepetiCategory(base_url)
product_links = []
page = 1
category_url = "/istanbul-rehberi?pg="
ks.set_pagination_limit(f"{category_url}{page}")
while True:
    ks_category_url = f"{category_url}{page}"
    links = ks.get_all_product_links(ks_category_url)
    if not links:
        break
    print(f"{len(links)} product links scraped from {ks_category_url}")
    product_links.extend(links)
    page += 1
print(f"category link: {ks_category_url}, product count: {len(product_links)}")
product_links = [base_url+link for link in product_links]
books = []
print(f"Product pages are scraping now...")
for product in product_links:
    p = KitapSepetiProduct(product)
    book = p.get_product()
    print(book.__dict__)
    books.append(book)
print(f"total books: {len(books)} in {base_url}{category_url}{page}")