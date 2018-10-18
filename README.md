# Flask

A simple example to demonstrate the structure of a Flask-built data-driven web app

This README will serve as a tutorial to getting started with building a Flask web app. Example comes from Udacity course on [full-stack foundations](https://classroom.udacity.com/courses/ud088)

## Getting started

This walk through assumes basic familiarity with Python classes/methods, SQL statements, HTML/CSS and a bit of javascript. These topics will not be covered here.

Make sure you have the following installed (use of fresh conda environment encouraged):

- `conda install flask`
- `conda install sqlalchemy`
- `conda install `
- `conda install `
- `conda install `


## Concepts

Brief overview of concepts/topics core to web development

### CRUD

Basic data actions can be summarized with the CRUD acronym

- **C**reate
  - Storage of new data
  - Often performed by a ***POST*** request
  - Analogous to SQL INSERT (INTO)
- **R**ead
  - Retreival of existing data
  - Often performed by a ***GET*** request
  - Analogous to SQL SELECT
- **U**pdate
  - Modification of existing data
  - Often performed by a ***PUT*** request
  - Analogous to SQL UPDATE
- **D**elete
  - Removal of existing data
  - Often performed by a ***DELETE*** request
  - Analogous to SQL DELETE

### ORM (Object-Relation-Manager/Mapper)

At the most simple level, an ORM is a tool to help a programmers interact with databases using syntax more consistent with the programming language. A full-fledged ORM however will help model data from a relational database as *objects* complete with built-in and custom methods, attributes, and relationships.

The most popular Python ORM (and the focus of this project) is [SQLAlchemy](https://www.sqlalchemy.org)
> Popular javascript ORMs include Loopback, Bookshelf.js, mongoose (MongoDB only), sequelize, and knex.js (not a full ORM but great db-interface tool)

Use of an ORM typically involves the following 4 steps:

- Configuration
  - set up dependencies and bind to SQLAlchemy Engine
  - should be mostly consistent project-to-project
  - beginning will create *declarative base*
  - end of block will create or connect to database (and add tables or columns)
- Class
  - representation of a table as Python class
  - should extend the Base class
  - `class TableName(Base)`
- Table
  - representation of table inside database
  - syntax: `__tablename__ = 'some_table'`
- Mapper
  - maps python objects to columns in database
  - must pass an attribute to each column creation to specify dtype
  - syntax: `columnName = Column(attributes, ...)`
  - example attributes = {`String(250)`, `Integer`, `relationship(Class)`, `nullable=False`, `primary_key=True`, `ForeignKy('some_table.id')`, etc}
  - 

Implementation for the above [demonstrated here](./db_setup.py)
