import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / 'data'

def simple_lookup_by_product_id(product_id: str):
    # Lightweight retriever for the scaffold: searches data/products.json for ID
    with open(DATA_DIR / 'products.json', 'r') as f:
        products = json.load(f)
    for p in products:
        if p.get('id') == product_id:
            return p
    return None
