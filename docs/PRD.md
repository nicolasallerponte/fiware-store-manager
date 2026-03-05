# Product Requirements Document (PRD)

## Project Name

Fiware Smart Store

## Overview

Fiware Smart Store is a web application designed to manage a supermarket chain. It provides an intuitive, high-performance interface for viewing and managing stores, the products they carry, and their respective inventory levels. It also features robust multi-language support (English, Spanish, Galician, German).

## Objectives

- Provide a centralized dashboard to monitor high-level system metrics (total stores, total products, total employees).
- Offer a dedicated view for exploring registered stores and their specific inventory and staff.
- Offer a master product list detailing all products tracked across the supermarket chain.
- Offer a master employee list detailing all staff members across the chain.
- Ensure a premium user experience utilizing a light minimalist design system with interactive features like maps and standardized image handling.
- Provide a localized user experience through multi-language support.

## Design System Constraints

The application strictly follows a light minimalist aesthetic inspired by Notion/Muji.

- **Typography:** Inter (Google Fonts).
- **Background Color:** `#fafafa`
- **Card Background:** `#ffffff`
- **Text:** Primary `#111111`, Secondary `#666666`
- **Accent Color:** `#111111`
- **Borders:** Target elements have `1px solid #e5e5e5` borders.
- **Effects:** High-quality micro-animations and clean lines. No box-shadows or gradients.

## Core Features & Views

### 0. Localization

- The web app supports UI translation in 4 languages: English, Español, Galego, and Deutsch.
- Users can toggle between languages using a dropdown in the navigation bar.

### 1. Dashboard (`/`)

Landing page providing a high-level overview. Must display metric cards summarizing the total count of stores and distinct products in the database.

### 2. Stores Module (`/stores`)

- **Index View:** Displays a grid of all active stores within the chain, showing their name, image (with placeholders if unavailable), and full address.
- **Detail View:** Deep dive into a specific store. Shows the store's metadata (URN ID, address, coordinates), an interactive map (Leaflet.js + OpenStreetMap) centered on the store location, an image with standardized placeholders, and a tabular view of its inventory (product name, pricing, specific stock and shelf quantities).

### 3. Products Module (`/products`)

- **Index View:** A master list of all products defined in the system, showing URN IDs, names, pricing, size, and origin country.
- **Detail View:** Deep dive into a specific product. Displays product metadata (URN ID, image, price, size, origin country) and enumerates which stores currently stock the product, along with localized stock counts.

### 4. Employees Module (`/employees`)

- **Index View:** A grid listing all employees, showing their name, role, image, and assigned store.
- **Detail View:** Deep dive into a specific employee. Displays name, role, photo, salary, and a link to their assigned store.

## Data Requirements (FIWARE NGSIv2 Compliant)

The system aligns with the FIWARE NGSIv2 CRUD Operations tutorial structure:

- **URN Identification:** All entity IDs follow the format `urn:ngsi-ld:{EntityType}:{number:03d}`.
- **Entities:**
  - **Store:** Includes name, street address, locality, region, coordinates (lat/long), and image.
  - **Shelf:** Represents storage units within a store, linked via `ref_store`.
  - **Product:** Includes name, price, size (S/M/L/XL), image, and origin country.
  - **Employee:** Includes name, role, salary, image, and `ref_store` relationship.
  - **InventoryItem:** Links stores, products, and shelves, tracking `stock_count` and `shelf_count`.
- **Sample Data:**
  - Exactly 4 stores with real-world addresses and coordinates.
  - Exactly 10 distinct products.
  - Exactly 8 employees distributed across stores (2 per store).
  - Distribution ensuring realistic inventory mapping across stores.
- Initial database is seeded via `init_db.py`.

## Testing Requirements

The application includes a comprehensive test suite using `pytest` and `pytest-flask`.

- **Database Coverage:** All database models (Store, Product, Employee, InventoryItem) must have persistence and relationship tests using an in-memory SQLite database.
- **Route Coverage:** All core routes (Dashboard, Store listing/detail, Product listing/detail, Employee listing/detail) must be tested for correct status codes (200/404) and basic content presence.
- **Fixtures:** Tests must use clean fixtures for the Flask application and database session to ensure test isolation.
