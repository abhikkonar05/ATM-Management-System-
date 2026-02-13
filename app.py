from flask import Flask, render_template, request, redirect, url_for, session,flash

app = Flask(__name__)
app.secret_key = "supersecretkey"


acc_holders = {
    'Name': 'Abhik',
    'Account Number': 1234567890,
    'PIN': 1234,
    'Balance': 39875
}

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    pin = request.form['pin']

    if len(pin) != 4 or not pin.isdigit():
        return "Invalid PIN format"

    if int(pin) == acc_holders['PIN']:
        session['user'] = acc_holders['Name']
        return redirect(url_for('dashboard'))
    else:
        return "Invalid PIN"

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template("dashboard.html", name=acc_holders['Name'], balance=acc_holders['Balance'])
    return redirect(url_for('home'))

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = int(request.form['amount'])
        if amount % 500 == 0:
            acc_holders['Balance'] += amount
            return redirect(url_for('dashboard'))
        else:
            return "Deposit must be multiple of 500"
    return render_template("deposit.html")

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amount = int(request.form['amount'])
        if amount % 500 != 0:
            return "Withdraw must be multiple of 500"
        if amount > acc_holders['Balance']:
            return "Insufficient Balance"
        acc_holders['Balance'] -= amount
        return redirect(url_for('dashboard'))
    return render_template("withdraw.html")

@app.route('/change_pin', methods=['GET', 'POST'])
def change_pin():
    if request.method == 'POST':
        pin = request.form['pin']
        if int(pin) != acc_holders['PIN']:
            return "Incorrect current PIN"
        else:
            new_pin = request.form['new_pin']
        if len(new_pin) == 4 and new_pin.isdigit():
            acc_holders['PIN'] = int(new_pin)
            flash("PIN changed successfully!","success")
            return redirect(url_for('dashboard'))
             
        else:
            return "Invalid PIN format"
    return render_template("change_pin.html")

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
