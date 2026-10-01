import json
import requests

URL = "https://www.daraz.pk/catalog/?ajax=true&q={product_name}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest"
}

def raw_deals(product_name: str):
    try:
        response = requests.get(URL.format(product_name = product_name.strip().lower()), headers = HEADERS)
        response.raise_for_status()
        return list(response.json()["mods"]["listItems"])
    
    except Exception as e:
        print(f"An unexpected error occurred {e}!")
        return None

def find_deals(product_name: str) -> list[dict]:
    
    deals = raw_deals(product_name)
    
    if deals is None:
        return "No Product Found for {product_name}"
    
    items = []

    for deal in deals:
        
        items.append({
            "Name": deal.get("name", "Not provided")[:120],
            "Image": deal.get("image", "Not provided"),
            "Original Price": deal.get("originalPrice", "Not provided"),
            "Current Price": deal.get("utLogMap").get("current_price", "Not Provided"),
            "Price to Show": deal.get("priceShow", "Not Provided"),
            "Discount": deal.get("discount", "Not Provided"),
            "Rating Score": deal.get("ratingScore", "Not Provided"),
            "Review": deal.get("review", "Not Provided"),
            "Location": deal.get("location", "Not Provided"),
            "Description": deal.get("description", "Not Provided"),
            "Seller Name": deal.get("sellerName", "Not Provided"),
            "Brand Name": deal.get("brandName", "Not Provided"),
            "In Stock": deal.get("inStock", "Not Provided"),
            "Item Sold Count": deal.get("itemSoldCntShow", "Not Provided"),
            "Item Url": deal.get("itemUrl", "Not Provided"),
            "Brand Name": deal.get("brandName", "Not Provided")
        })
        
    return "Products: \n\n" + "\n\n".join(str(item) for item in items)
