CREATE TABLE departments (
    id SERIAL PRIMARY KEY, -- Use SERIAL for auto-incrementing ID
    title VARCHAR(128),
    description VARCHAR(432),
    readme TEXT
);
