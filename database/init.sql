CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    date DATE,
    name VARCHAR(100),
    time TIME,
    location VARCHAR(100)
);

CREATE VIEW attendance_view AS
SELECT name, date, time, location FROM attendance;
