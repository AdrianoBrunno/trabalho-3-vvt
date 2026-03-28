CREATE DATABASE IF NOT EXISTS db_produtos;
USE db_produtos;

-- Tabela atualizada conforme exigência do Trabalho 3
CREATE TABLE codigos_sequenciais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(8) UNIQUE NOT NULL,
    sec INT NOT NULL,
    Grupo CHAR(1) NOT NULL,
    Tipo_Alimento CHAR(1) NOT NULL,
    Pais CHAR(2) NOT NULL
);

INSERT INTO codigos_sequenciais (id, codigo, sec, Grupo, Tipo_Alimento, Pais) VALUES
(1, 'BRC0001A', 1, 'C', 'A', 'BR'),
(2, 'BRD00011', 1, 'D', '1', 'BR'),
(3, 'BRA0001K', 1, 'A', 'K', 'BR'),
(4, 'BRF0001F', 1, 'F', 'F', 'BR'),
(5, 'BRG0001A', 1, 'G', 'A', 'BR'),
(6, 'BRC0002A', 2, 'C', 'A', 'BR'),
(7, 'BRD0002K', 2, 'D', 'K', 'BR'),
(8, 'BRF0002A', 2, 'F', 'A', 'BR'),
(9, 'BRC0003C', 3, 'C', 'C', 'BR');