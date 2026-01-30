from datetime import date
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


# Create a Category model for products
class Category(Base):
    __tablename__ = "categories"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    category = relationship("Category", back_populates="products")
    orders = relationship("Order", back_populates="product")

    def __repr__(self):
        return f"<Product {self.name} ${self.price}>"


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(200))
    city = Column(String(100))
    registration_date = Column(Date, default=date.today)

    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<Customer {self.name}>"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    order_date = Column(Date, nullable=False, default=date.today)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="orders")
    product = relationship("Product", back_populates="orders")

    def __repr__(self):
        return f"<Order #{self.id} product {self.product_id}, quantity {self.quantity}>"
