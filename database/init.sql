DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(30) NOT NULL,
    legajo VARCHAR(10) NOT NULL,
    feature VARCHAR(30) NOT NULL,
    servicio VARCHAR(30) NOT NULL,
    estado VARCHAR(30) NOT NULL
);

INSERT INTO members (nombre, apellido, legajo, feature, servicio, estado) VALUES
('Ivo', 'Balduzzi', '32470', 'Feature 01', 'Coordinador', 'ok'),
('Maria Belen', 'Pieroni', '32324', 'Feature 02', 'Frontend', 'ok'),
('Jeronimo', 'Molina', '30812', 'Feature 03', 'Backend', 'ok'),
('Ariel', 'Cayo', '32680', 'Feature 04', 'Base de Datos', 'ok');