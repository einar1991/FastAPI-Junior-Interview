-- Categories (5 items)
INSERT INTO categories (id, name) VALUES
(1, 'Electronics'),
(2, 'Clothing'),
(3, 'Books'),
(4, 'Groceries'),
(5, 'Furniture');

-- Products (10 items)
INSERT INTO products (id, name, category_id, price, stock) VALUES
(1, 'iPhone 14', 1, 799.99, 50),
(2, 'Samsung TV', 1, 1199.99, 20),
(3, 'Levis Jeans', 2, 89.99, 100),
(4, 'Nike T-shirt', 2, 29.99, 200),
(5, 'War and Peace', 3, 14.99, 500),
(6, '1984', 3, 9.99, 300),
(7, 'Milk', 4, 1.99, 1000),
(8, 'Bread', 4, 0.99, 800),
(9, 'Chair', 5, 49.99, 150),
(10, 'Table', 5, 199.99, 50);

-- Customers (6 items)
INSERT INTO customers (id, email, name, city, registration_date) VALUES
(1, 'john.doe@email.com', 'John Doe', 'Berlin', '2025-01-15'),
(2, 'sophia.martin@email.com', 'Sophia Martin', 'Paris', '2025-02-20'),
(3, 'luca.rossi@email.com', 'Luca Rossi', 'Rome', '2025-03-10'),
(4, 'emma.jones@email.com', 'Emma Jones', 'London', '2025-01-05'),
(5, 'mikael.svensson@email.com', 'Mikael Svensson', 'Stockholm', '2025-04-01'),
(6, 'isabella.garcia@email.com', 'Isabella Garcia', 'Madrid', '2025-05-15');
