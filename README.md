
# Ledger Web Application with EVM Smart Contract Integration

This project demonstrates a Flask-based web application that simulates interaction with an Ethereum Virtual Machine (EVM) smart contract to add and retrieve ledger entries. For simplicity and offline demonstration purposes, actual Ethereum interactions are mocked.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [Project Explanation](#project-explanation)
  - [Smart Contract](#smart-contract)
  - [Flask Backend](#flask-backend)
  - [Frontend](#frontend)
- [References and Further Reading](#references-and-further-reading)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

- `app.py`: Contains the main Flask application script with the backend logic.
- `templates/`: Houses the HTML templates for the frontend.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask

### Installation Steps

1. Clone the GitHub repository.
2. Navigate to the project directory.
3. Install the required Python packages:

```bash
pip install Flask
```

## Running the Application

1. Navigate to the project directory.
2. Run the Flask application:

```bash
python app.py
```

3. Open a web browser and visit `http://localhost:5000/` to interact with the application.

## Project Explanation

### Smart Contract

The theoretical smart contract (not implemented in this demo) is a basic ledger contract that allows users to add and retrieve ledger entries. It has functionalities to:
- Add a new ledger entry.
- Retrieve the total number of entries.
- Fetch an entry by its index.

### Flask Backend

The Flask backend simulates the interaction with the mock Ethereum smart contract. The `MockWeb3` class mimics the behavior of the `web3.py` library without actually connecting to an Ethereum network. It includes methods to:
- Add a ledger entry.
- Fetch the count of all ledger entries.
- Retrieve a ledger entry by its index.

### Frontend

The frontend is designed using HTML and Bootstrap. It provides a user interface to:
- Add new ledger entries via a form.
- Display all the added ledger entries.

## References and Further Reading

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [Ethereum Smart Contracts](https://ethereum.org/en/developers/docs/smart-contracts/)
- [web3.py Documentation](https://web3py.readthedocs.io/en/stable/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
