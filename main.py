import uvicorn

from fastapi import FastAPI
from sqlalchemy import func, select, cast, Numeric

from database import async_session_maker
from models import Category, Product

app = FastAPI(
    title="Online Shop",
    version="1.0.0",
    root_path="/api",
)


# Sample endpoints
# Join
@app.get("/products/name-and-category")
async def get_products():
    async with async_session_maker() as session:
        query = select(
            Product.name,
            Category.name.label("category_name"),
        ).join(Category)
        result = await session.execute(query)
        return result.mappings().all()


# Group by
@app.get("/products/stats-by-category")
async def stats_by_category():
    async with async_session_maker() as session:
        query = (
            select(
                Category.name.label("category"),
                func.count(Product.id).label("total_products"),
                func.round(cast(func.avg(Product.price), Numeric(10, 2)), 2).label(
                    "avg_price"
                ),
                func.round(cast(func.sum(Product.price), Numeric(10, 2)), 2).label(
                    "total_value"
                ),
            )
            .join(Product, Category.id == Product.category_id)
            .group_by(Category.id)
        )

        result = await session.execute(query)
        return result.mappings().all()


"""
Backend task #1
Create a GET endpoint /products that returns all products.
Use the Product model and the examples above as a reference.

Requirements:
1. Return id, name, price, stock for each product
2. Include category name for each product (use JOIN)
3. Add sorting by price (ascending order)
4. Add a limit parameter to limit the number of results
5. Use async/await as shown in the examples
"""

"""
Backend task #2
Create a POST endpoint /orders for creating a new order.

Requirements:
1. Accept JSON: {"customer_id": 1, "product_id": 5, "quantity": 2}
2. Check that the product is in stock (stock >= quantity)
3. Create the order in the database
4. Reduce the product stock (stock -= quantity)
5. Return the created order with status 201

Advanced: Use a database transaction for atomicity
(if anything fails - rollback everything).
"""

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
