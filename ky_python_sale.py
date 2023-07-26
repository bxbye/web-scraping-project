"""
Yazar: Kadir KAYA
Bu script; kitapyurdu sitesindeki python aramasi yapildiginda satista olan kitaplari kazir.
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
# category pages scraping
page = 1
while True:
    ky_category_url = f"/index.php?route=product/search&page={page}&filter_name=python&fuzzy=0&filter_in_stock=1"
    links = ky_bilim.get_all_product_links(ky_category_url)
    if not links:
        print("this category page has no product link")
        break
    product_links.extend(links)
    page += 1
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