import uvicorn

from fastapi import FastAPI, Query, HTTPException
from pydantic import Field, BaseModel
from sqlalchemy import func, select, cast, Numeric

from database import async_session_maker
from models import Category, Product, Customer, Order

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


# Solution #1
@app.get("/products/")
async def get_products(
        offset: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100),
):
    async with async_session_maker() as session:
        query = (
            select(
                Product.id,
                Product.name,
                Product.price,
                Product.stock,
                Category.name.label("category_name"),
            )
            .join(Category)
            .order_by(Product.price)
            .offset(offset)
            .limit(limit)
        )
        result = await session.execute(query)
        return result.mappings().all()


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


# Solution #2
class SOrderCreate(BaseModel):
    customer_id: int = Field(gt=0)
    product_id: int = Field(gt=0)
    quantity: int = Field(gt=0)


@app.post("/orders/", status_code=201)
async def create_order(order_data: SOrderCreate):
    async with async_session_maker() as session:
        async with session.begin():
            customer = await session.get(Customer, order_data.customer_id)
            if not customer:
                raise HTTPException(404, "Customer not found")

            product = await session.get(Product, order_data.product_id)
            if not product:
                raise HTTPException(404, "Product not found")

            if product.stock < order_data.quantity:
                raise HTTPException(400, f"Only {product.stock} items available")

            product.stock -= order_data.quantity

            order = Order(
                customer_id=order_data.customer_id,
                product_id=order_data.product_id,
                quantity=order_data.quantity,
            )
            session.add(order)

            await session.flush()
            return order


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
