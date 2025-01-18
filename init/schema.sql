CREATE DATABASE IF NOT EXISTS pets_backend_db;

USE pets_backend_db;

-- Table: addresses
CREATE TABLE IF NOT EXISTS `addresses` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    cep BIGINT NOT NULL,
    state VARCHAR(2) NOT NULL,
    city VARCHAR(255) NOT NULL,
    neighborhood VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    complement VARCHAR(255),
    number BIGINT NOT NULL,
    PRIMARY KEY (id)
);

-- Table: animal_shelters
CREATE TABLE IF NOT EXISTS `animal_shelters` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    cpf BIGINT UNIQUE NOT NULL,
    responsible_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number BIGINT NOT NULL,
    address_id BIGINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (address_id) REFERENCES addresses(id) ON DELETE CASCADE
);

-- Table: species
CREATE TABLE IF NOT EXISTS `species` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    specie_name VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (id)
);

-- Table: pets
CREATE TABLE IF NOT EXISTS `pets` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    specie BIGINT NOT NULL,
    age BIGINT,
    animal_shelter_id BIGINT NOT NULL,
    adopted BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id),
    FOREIGN KEY (specie) REFERENCES species(id) ON DELETE CASCADE,
    FOREIGN KEY (animal_shelter_id) REFERENCES animal_shelters(id) ON DELETE CASCADE
);

-- Table: user_adopters
CREATE TABLE IF NOT EXISTS `user_adopters` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    cpf BIGINT NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number BIGINT NOT NULL,
    address_id BIGINT NOT NULL,
    pet_id BIGINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (address_id) REFERENCES addresses(id) ON DELETE CASCADE,
    FOREIGN KEY (pet_id) REFERENCES pets(id) ON DELETE CASCADE
);
