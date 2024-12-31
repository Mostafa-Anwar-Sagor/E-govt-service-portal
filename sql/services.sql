CREATE TABLE services (
    id INT SERIAL PRIMARY KEY,
    title VARCHAR(128),
    description VARCHAR(432),
    readme TEXT,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);
