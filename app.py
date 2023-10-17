from flask import Flask, render_template, request, redirect, url_for, flash
from web3 import Web3
from Crypto.Cipher import AES


app = Flask(__name__)
app.secret_key = "some_secret_key"  # used for flashing messages

# Mock Ethereum connection
class MockWeb3(Web3):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._entries = []

    def addEntry(self, description, amount):
        self._entries.append((description, amount))
        return True

    def getEntryCount(self):
        return len(self._entries)

    def getEntry(self, index):
        return self._entries[index]

web3 = MockWeb3()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form.get('description')
        amount = int(request.form.get('amount'))
        # Add entry to the mock Ethereum network
        success = web3.addEntry(description, amount)
        if success:
            flash('Entry added successfully!', 'success')
        else:
            flash('Failed to add entry!', 'danger')
        return redirect(url_for('index'))
    
    # Retrieve all entries
    entry_count = web3.getEntryCount()
    entries = [web3.getEntry(i) for i in range(entry_count)]
    
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    description = request.form.get('description')
    amount = int(request.form.get('amount'))
    # Add entry to the mock Ethereum network
    success = web3.addEntry(description, amount)
    if success:
        flash('Entry added successfully!', 'success')
    else:
        flash('Failed to add entry!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
