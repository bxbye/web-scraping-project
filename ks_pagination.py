"""
Yazar: Kadir KAYA
Bu script; herhangi bir kitap kategorisi listelendiginde o sayfanin linki pg= parametresiyle beraber category_url parametresine atanirsa o kategoriye ait tum kitaplari kazima islemi yapar.
"""
from models.classes import KitapSepetiCategory, KitapSepetiProduct
from models.db_operations import DbManager

# set up mongodb connection
smartmaple = DbManager("mongodb://localhost:27017", "smartmaple")
smartmaple.set_collection("kitapsepeti")

# i want to delete collection items before script starting.
print(f"current document_count: {smartmaple.get_item_count({})}")
smartmaple.drop_collection()

base_url = "https://www.kitapsepeti.com"
ks = KitapSepetiCategory(base_url)
product_links = []

# category pages scraping
page = 1
category_url = f"/istanbul-rehberi?pg="
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

print(f"Product pages are scraping now...")
for product in product_links:
    p = KitapSepetiProduct(product)
    new_book = p.get_product() # book is type of Book obj
    book = new_book.to_dict()
    # add book dict to collection.
    result = smartmaple.insert_single_item(book)
    print(f"inserted_id: {result}")

# drop collection and close connection from app.
print(f"current document_count of kitapsepeti: {smartmaple.get_item_count({})}")
smartmaple.close_connection()