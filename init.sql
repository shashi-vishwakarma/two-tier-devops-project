CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    salary INT NOT NULL
);

INSERT INTO employees (name, department, salary) VALUES
('Shashi Vishwakarma', 'DevOps', 60000),
('Rahul Sharma', 'Backend', 55000),
('Priya Patel', 'HR', 45000),
('Aman Singh', 'Cloud Engineer', 70000);
