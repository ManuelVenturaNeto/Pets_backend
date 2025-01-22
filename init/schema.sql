CREATE DATABASE IF NOT EXISTS pets_backend_db;

-- Table: addresses
CREATE TABLE IF NOT EXISTS `pets_backend_db`.`addresses` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    cep VARCHAR(8) NOT NULL,
    state VARCHAR(2) NOT NULL,
    city VARCHAR(255) NOT NULL,
    neighborhood VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    complement VARCHAR(255),
    number BIGINT NOT NULL,
    PRIMARY KEY (id)
);

-- Table: animal_shelters
CREATE TABLE IF NOT EXISTS `pets_backend_db`.`animal_shelters` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    responsible_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(11) NOT NULL,
    address_id BIGINT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (address_id) REFERENCES `pets_backend_db`.`addresses`(id) ON DELETE CASCADE
);

-- Table: species
CREATE TABLE IF NOT EXISTS `pets_backend_db`.`species` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    specie_name VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

-- Table: pets
CREATE TABLE IF NOT EXISTS `pets_backend_db`.`pets` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    specie BIGINT NOT NULL,
    age BIGINT,
    animal_shelter_id BIGINT NULL,
    adopted BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id),
    FOREIGN KEY (specie) REFERENCES `pets_backend_db`.`species`(id) ON DELETE CASCADE,
    FOREIGN KEY (animal_shelter_id) REFERENCES `pets_backend_db`.`animal_shelters`(id) ON DELETE CASCADE
);

-- Table: user_adopters
CREATE TABLE IF NOT EXISTS `pets_backend_db`.`user_adopters` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(11) NOT NULL,
    address_id BIGINT NULL,
    pet_id BIGINT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (address_id) REFERENCES `pets_backend_db`.`addresses`(id) ON DELETE CASCADE,
    FOREIGN KEY (pet_id) REFERENCES `pets_backend_db`.`pets`(id) ON DELETE CASCADE
);
