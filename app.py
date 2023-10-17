
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "some_secret_key"  # used for flashing messages

# Set up connection with Ethereum testnet
# For the sake of this example, we're just mocking the web3 connection
# In a real scenario, you'd connect to an Ethereum node (e.g., via Infura)

class MockWeb3:
    def __init__(self):
        self._entries = []

    @property
    def eth(self):
        return self

    def contract(self, **kwargs):
        return self

    def functions(self):
        return self

    def addEntry(self, description, amount):
        # Now actually store the entry in the mock class
        self._entries.append((description, amount))

    def getEntryCount(self):
        # Return the count of stored entries
        return len(self._entries)

    def getEntry(self, index):
        # Return the entry at the specified index
        return self._entries[index]
web3 = MockWeb3()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = int(request.form.get('amount'))
        # Add entry to the smart contract
        web3.eth.contract().functions().addEntry(description, amount)
        flash('Entry added successfully!', 'success')
        return redirect(url_for('index'))
    
    # Retrieve all entries
    entry_count = web3.eth.contract().functions().getEntryCount()
    entries = [web3.eth.contract().functions().getEntry(i) for i in range(entry_count)]
    
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    description = request.form.get('description')
    amount = int(request.form.get('amount'))
    # Add entry to the smart contract
    web3.eth.contract().functions().addEntry(description, amount)
    flash('Entry added successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
