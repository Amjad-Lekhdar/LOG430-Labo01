-- Créer le tableau Users
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    email VARCHAR(80) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    brand VARCHAR(20) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Créer des enregistrements dans Users
INSERT INTO users (name, email) VALUES
('Ada Lovelace', 'alovelace@example.com'),
('Adele Goldberg', 'agoldberg@example.com'),
('Alan Turing', 'aturing@example.com');

-- Créer des enregistrements dans Products
INSERT INTO products (name, brand, price) VALUES
('Laptop', 'Lenovo', 899.99),
('Monitor', 'Dell', 249.99),
('Keyboard', 'Logitech', 79.99);
