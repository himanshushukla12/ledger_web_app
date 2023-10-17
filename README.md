
# Ledger Web Application with EVM Smart Contract Integration

This project demonstrates a simple Flask-based web application that interacts with a mock Ethereum Virtual Machine (EVM) smart contract to add and retrieve ledger entries. The actual Ethereum interactions are mocked for simplicity.

## Project Structure

- `app.py`: The main Flask application script containing the backend logic.
- `templates/`: This directory contains the HTML templates for the frontend.

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask

### Installation Steps

1. Clone the repository.
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

## Notes

This is a mock application for demonstration purposes, and the Ethereum smart contract interactions are simulated. In a real-world scenario, you'd replace the mocked interactions with actual `web3.py` interactions and deploy the smart contract to an Ethereum testnet.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
