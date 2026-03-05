# Product Requirements Document (PRD)

## Project Name

Fiware Smart Store

## Overview

Fiware Smart Store is a web application designed to manage a supermarket chain. It provides an intuitive, high-performance interface for viewing and managing stores, the products they carry, and their respective inventory levels. It also features robust multi-language support (English, Spanish, Galician, German).

## Objectives

- Provide a centralized dashboard to monitor high-level system metrics (total stores, total products).
- Offer a dedicated view for exploring registered stores and their specific inventory.
- Offer a master product list detailing all products tracked across the supermarket chain.
- Ensure a premium user experience utilizing a dark minimalist design system.
- Provide a localized user experience through multi-language support.

## Design System Constraints

The application strictly follows a dark minimalist aesthetic inspired by Linear/Vercel.

- **Typography:** Inter (Google Fonts).
- **Background Color:** `#0f0f0f`
- **Card Background:** `#1a1a1a`
- **Text:** Primary `#ffffff`, Secondary `#888888`
- **Accent Color:** `#6366f1`
- **Borders:** Target elements have `1px solid #222` borders.
- **Effects:** Absolutely no box-shadows or gradients.

## Core Features & Views

### 0. Localization

- The web app supports UI translation in 4 languages: English, Español, Galego, and Deutsch.
- Users can toggle between languages using a dropdown in the navigation bar.

### 1. Dashboard (`/`)

Landing page providing a high-level overview. Must display metric cards summarizing the total count of stores and distinct products in the database.

### 2. Stores Module (`/stores`)

- **Index View:** Displays a grid or list of all active stores within the chain, showcasing their name and location.
- **Detail View:** Deep dive into a specific store. It must show the store's metadata and a tabular view of its inventory (the products it carries, pricing, and specific stock quantities at that location).

### 3. Products Module (`/products`)

- **Index View:** A master list of all products defined in the system.
- **Detail View:** Deep dive into a specific product. Displays product metadata (name, description, price) and enumerates which stores currently stock the product, along with the corresponding localized stock quantities.

## Data Requirements (Initial Mock Data)

The system must be initialized with:

- Exactly 4 stores.
- Exactly 10 distinct products.
- A distribution of products that guarantees at least one store carries a minimum of 5 distinct products.
- Products can belong to multiple stores (Many-to-Many inventory tracking).
- Initial database is seeded via `init_db.py`.

## Testing Requirements

The application includes a comprehensive test suite using `pytest` and `pytest-flask`.

- **Database Coverage:** All database models (Store, Product, InventoryItem) must have persistence and relationship tests using an in-memory SQLite database.
- **Route Coverage:** All core routes (Dashboard, Store listing/detail, Product listing/detail) must be tested for correct status codes (200/404) and basic content presence.
- **Fixtures:** Tests must use clean fixtures for the Flask application and database session to ensure test isolation.
