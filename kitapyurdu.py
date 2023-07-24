from models.classes import KitapYurduCategory, KitapYurduProduct

base_url = "https://www.kitapyurdu.com"
ky_bilim = KitapYurduCategory(base_url)

product_links = []
page = 1
while True:
    ky_category_url = f"/index.php?route=product/category&page={page}&path=1_737_740&filter_in_stock=1"
    links = ky_bilim.get_all_product_links(ky_category_url)
    if not links:
        break
    product_links.extend(links)
    page += 1
    #break
print(f"category link: {ky_category_url}, product count: {len(product_links)}")

books = []
print(f"Product pages are scraping now...")
for product in product_links:
    p = KitapYurduProduct(product)
    book = p.get_product()
    print(book.__dict__)
    books.append(book)
print(f"total books: {len(books)} in {base_url}/index.php?route=product/category&page={page}&path=1_1033_1715&filter_in_stock=1")