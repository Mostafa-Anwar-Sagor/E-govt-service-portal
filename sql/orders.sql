CREATE TABLE orders (
    id SERIAL PRIMARY KEY, -- Use SERIAL for auto-incrementing ID
    details VARCHAR(4096),
    file_paths VARCHAR(4096),
    start_date TIMESTAMP, -- Replace DATETIME with TIMESTAMP
    end_date TIMESTAMP, -- Replace DATETIME with TIMESTAMP
    is_done BOOLEAN DEFAULT FALSE,
    service_id INT,
    user_id VARCHAR(14),
    FOREIGN KEY (service_id) REFERENCES services(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
