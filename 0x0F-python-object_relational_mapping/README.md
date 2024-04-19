# Python Object. Relational Mapping (ORM) with MySQL

This repository contains a series of Python scripts that demonstrate the use of Object. Relational Mapping (ORM) techniques with MySQL databases. The scripts utilize the **MySQLdb** library for direct MySQL interaction and **SQLAlchemy** for ORM operations.

## Setup
To run these scripts, ensure you have Python 3.8 and the required dependencies installed:
1. Install Python 3.8 and pip:
```bash
sudo apt. get update
sudo apt. get install python3.8 python3.8. venv python3.8. dev
```
2. Create and activate a virtual environment:
```bash
python3.8 . m venv venv
source venv/bin/activate
```
3. Install MySQLdb and SQLAlchemy:
```bash
pip install mysqlclient SQLAlchemy
```
## Usage

Each script in this repository demonstrates a specific task:

0. ***select_states.py***: Lists all states from a database.
1. ***filter_states.py***: Lists states starting with 'N'.
2. ***my_filter_states.py***: Lists states based on user input.
3. ***my_safe_filter_states.py***: Lists states securely against SQL injection.
4. ***cities_by_state.py***: Lists all cities from the database.
5. ***filter_cities.py***: Lists cities of a specific state.
6. ***model_state.py***: Defines a State class using SQLAlchemy.
7. ***model_state_fetch_all.py***: Lists all State objects.
8. ***model_state_fetch_first.py***: Lists the first State object.
9. ***model_state_filter_a.py***: Lists State objects containing the letter 'a'.
10. ***model_state_my_get.py***: Prints the id of a specified State.
11. ***model_state_insert.py***: Inserts a new State into the database.
12. ***model_state_update_id_2.py***: Updates the name of a State by ID.
13. ***model_state_delete_a.py***: Deletes State objects with 'a' in the name.

Each script takes MySQL credentials and database name as arguments.

### Example
```bash 
./0-select_states.py root password hbtn_0e_0_usa
./1-filter_states.py root password hbtn_0e_0_usa
# etc...
```
