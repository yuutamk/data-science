-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS rendimiento_academico;
USE rendimiento_academico;

-- Crear la tabla estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    student_id INT PRIMARY KEY,
    study_hours DECIMAL(4, 1),
    attendance DECIMAL(5, 2),
    socioeconomic_status ENUM('low', 'medium', 'high'),
    previous_grades DECIMAL(5, 2),
    access_to_resources ENUM('yes', 'no'),
    final_grade DECIMAL(5, 2)
);

-- Insertar datos de ejemplo
INSERT INTO estudiantes (student_id, study_hours, attendance, socioeconomic_status, previous_grades, access_to_resources, final_grade) VALUES
(1, 5.5, 85.00, 'low', 70.00, 'yes', 72.00),
(2, 8.0, 95.00, 'medium', 85.00, 'yes', 88.00),
(3, 3.0, 60.00, 'low', 65.00, 'no', 58.00),
(4, 10.5, 90.00, 'high', 90.00, 'yes', 92.00),
(5, 7.0, 75.00, 'medium', 78.00, 'yes', 80.00),
(6, 4.5, 50.00, 'low', 62.00, 'no', 55.00),
(7, 9.0, 100.00, 'high', 95.00, 'yes', 94.00),
(8, 6.5, 80.00, 'medium', 75.00, 'yes', 78.00),
(9, 2.0, 40.00, 'low', 55.00, 'no', 50.00),
(10, 12.0, 98.00, 'high', 93.00, 'yes', 96.00);