# API PETS Backend

## Description

<p>This API is designed to allow animal shelters to register themselves and then register the animals under their care. 
  Afterward, individuals interested in adopting animals can browse the available options. 
  The system is built as a microservice and is currently in the early stages of development.

To help with understanding the project, the "Diagramas" folder includes several diagrams, such as Entity, Class, and Use Case diagrams.

The entire project is implemented in Python, following Clean Code principles to ensure maintainability and readability..</p>

## Running the Application

## Instalação

1. Clone o repositorio do github:

```terminal
  https://github.com/ManuelVenturaNeto/Pets_backend.git
```
2. Entre na parta: 

```terminal
  CD Pets_backend
```  
3. Crie o docker-compose:

```terminal
  docker-compose -f docker-compose.yml up --build
```
4. Popule a tabela de espécies

```terminal
  docker-compose exec docker-python python -m populate.species
```

## Conxão com DBeaver

1. conecte-se com MySQL com os seguintes parametros:

Servidor: localhost

Porta: 3307

Nome de usuário: root

Senha: manuel
