from fastapi import FastAPI

# Create environment: python3 -m venv .venv
# Activate source ./.venv/bin/active
# Install fastAPI: pip install "fastapi[standard]"
# Run server with unicorn: fastapi dev main.py

app = FastAPI()

items = [
    {'id': 1, 'name': 'Item One'},
    {'id': 2, 'name': 'Item Two'},
    {'id': 3, 'name': 'Item Three'},
]


@app.get('/health')
def health_check():
    return {'status': 'ok'}


@app.get('/items')
def get_items():
    return items


@app.get('/items/{item_id}')
def get_item(item_id: int):
    for item in items:
        if item['id'] == item_id:
            return item
    return {'error': 'Item not found'}


@app.post('/items')
def create_item(item: dict):
    items.append(item)
    return item
