"""
Yazar: Kadir KAYA
Bu script; herhangi bir kitap kategorisi listelendiginde o sayfanin linki &page= parametresiyle beraber ky_category_url parametresine atanirsa o kategoriye ait tum kitaplari kazima islemi yapar.
"""
from models.classes import KitapYurduCategory, KitapYurduProduct
from models.db_operations import DbManager

# set up mongodb connection
smartmaple = DbManager("mongodb://localhost:27017", "smartmaple")
smartmaple.set_collection("kitapyurdu")

# i want to delete collection items before script starting.
print(f"current document_count: {smartmaple.get_item_count({})}")
smartmaple.drop_collection()

base_url = "https://www.kitapyurdu.com"
ky_bilim = KitapYurduCategory(base_url)

product_links = []
page = 1
while True:
    cocuk_egitimi_url = f"/index.php?route=product/category&page={page}&path=1_359_361&filter_in_stock=1"
    ky_category_url = f"/index.php?route=product/category&page={page}&path=1_359_369&filter_in_stock=1"
    links = ky_bilim.get_all_product_links(cocuk_egitimi_url)
    if not links:
        break
    product_links.extend(links)
    page += 1
    #break
print(f"category link: {ky_category_url}, product count: {len(product_links)}")

print(f"Product pages are scraping now...")
for product in product_links:
    p = KitapYurduProduct(product)
    new_book = p.get_product() # book is type of Book obj
    book = new_book.to_dict()
    # add book dict to collection.
    result = smartmaple.insert_single_item(book)
    print(f"inserted_id: {result}")
# drop collection and close connection from app.
print(f"current document_count of kitapyurdu: {smartmaple.get_item_count({})}")
smartmaple.close_connection()    