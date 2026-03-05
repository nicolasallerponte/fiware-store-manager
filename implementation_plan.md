# fiware-smart-store Implementation Plan

This plan describes how we will implement the smart store web application using Flask, SQLAlchemy, and SQLite, adhering to the requested design system and data requirements.

## User Review Required

> [!IMPORTANT]
> Please review this plan and approve it before we proceed with the actual implementation. Ensure the models, routes, and UI design match your expectations.

## Proposed Changes

### Database Models (`app/models.py`)

- **Store**: `id` (Integer), `name` (String), `location` (String), `created_at` (DateTime)
- **Product**: `id` (Integer), `name` (String), `description` (Text), `price` (Float), `created_at` (DateTime)
- **InventoryItem** (Junction Table/Model): `store_id` (Integer, ForeignKey), `product_id` (Integer, ForeignKey), `stock_quantity` (Integer)
- _Relationship_: Many-to-many relationship. A store has multiple products via `InventoryItem`, and a product can belong to multiple stores via `InventoryItem`.

### Sample Data Initialization (`run.py` or new `app/cli.py`)

- Define exactly 4 mock stores.
- Define exactly 10 distinct products.
- Distribute products across stores by creating `InventoryItem` records linking a store to a product with a defined quantity.
- Guarantee at least 5 products belong to one specific store to meet the requirement.

### UI & Styling System (`app/static/css/style.css` and `app/templates/base.html`)

- **Typography**: Include Google Fonts (Inter).
- **Styling specifications**:
  - Background: `#0f0f0f`
  - Text colors: `#ffffff` (primary), `#888888` (secondary)
  - Accent Color: `#6366f1`
  - Card background: `#1a1a1a`
  - Layout & Borders: Borders `1px solid #222`, no shadows, no gradients.
  - Buttons: Outline-style with `#6366f1` border and text.

---

### Views & Routes (`app/routes/` and `app/templates/`)

#### [NEW] app/routes/main.py

- `/`: Dashboard showing high-level stats (total stores, total products).

#### [NEW] app/routes/stores.py

- `/stores`: List of all stores.
- `/stores/<int:store_id>`: Store detail view, listing its specific products and quantities from the inventory.

#### [NEW] app/routes/products.py

- `/products`: List of all products across all stores.
- `/products/<int:product_id>`: Product detail view, showing which stores carry the product.

#### [NEW] app/templates/dashboard.html

- High level overview cards presenting the system's current state.

#### [NEW] app/templates/stores/index.html

- Grid or list interface showing all registered stores.

#### [NEW] app/templates/stores/detail.html

- Details for a specific store, including a table/list of its available products from the store inventory.

#### [NEW] app/templates/products/index.html

- Grid or table interface detailing all products in the system.

#### [NEW] app/templates/products/detail.html

- Focused details for a specific product.

## Verification Plan

### Automated Tests

- For this initial prototype phase, we will omit automated test creation unless explicitly requested.

### Manual Verification

- Start the Flask app using `flask run` or `python run.py`.
- Navigate through all 5 required views (dashboard, stores list, store detail, products list, product detail).
- Check the database visibly on the views to ensure the presence of 4 stores and 10 products, with at least 5 products belonging to one specific store.
- Confirm the UI matches the dark minimalist styling rules (colors, Inter font, 1px #222 borders, no shadows/gradients).
