
---

# Ledger Web Application with EVM Smart Contract Integration

This project is a Flask-based web application designed to simulate interactions with an Ethereum smart contract for the addition and retrieval of ledger entries. While actual Ethereum interactions are mocked in this demonstration, the framework is structured to allow real Ethereum integration.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [About the Application](#about-the-application)
- [Troubleshooting](#troubleshooting)
- [References](#references)

## Project Structure

- `app.py`: Contains the main Flask application script with the backend logic.
- `templates/`: Houses the HTML templates for the frontend.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- web3.py library
- pycryptodome

### Installation Steps

1. Clone the GitHub repository.
2. Navigate to the project directory.
3. Install the required Python packages:

```bash
pip install Flask web3 pycryptodome
```

## Running the Application

1. Navigate to the project directory.
2. Execute the Flask application:

```bash
python app.py
```

3. Open a web browser and visit `http://localhost:5000/`.
   ![Image Alt Text](https://github.com/himanshushukla12/ledger_web_app/raw/main/Screenshot.png)


## About the Application

- **Frontend**: Designed using Bootstrap, it provides a form for users to add new ledger entries and displays all the added entries.
- **Backend**: Uses Flask to handle web requests and `web3.py` to simulate interactions with an Ethereum smart contract.
- **Ethereum Interaction**: The interactions with the Ethereum smart contract are mocked in this demonstration for simplicity. In a real-world scenario, you'd connect to an Ethereum testnet and interact with a deployed smart contract.

## Troubleshooting

If you encounter an error related to the `Crypto` module after installing the `web3.py` library:

1. Uninstall both `crypto` and `pycryptodome`:

```bash
pip uninstall crypto pycryptodome
```

2. Reinstall only `pycryptodome`:

```bash
pip install pycryptodome
```

Ensure that the `Crypto` module is accessible in Python:

```python
from Crypto.Cipher import AES
```

This should resolve potential conflicts between `crypto` and `pycryptodome`.

## References

- [Flask Documentation](https://flask.palletsprojects.com/en/2.1.x/)
- [web3.py Documentation](https://web3py.readthedocs.io/en/stable/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- [Ethereum Smart Contracts](https://ethereum.org/en/developers/docs/smart-contracts/)
- [pycryptodome Documentation](https://www.pycryptodome.org/en/latest/)

---

You can use this updated documentation as the `README.md` for your project. This provides a thorough overview, including a troubleshooting section to address the `Crypto` module error.
