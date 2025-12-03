from flask import Flask, render_template, request, redirect, url_for, flash
from database import db, InventoryItem

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-me'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    items = InventoryItem.query.order_by(InventoryItem.name).all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name'].strip()
        quantity = int(request.form['quantity'])
        if InventoryItem.query.filter_by(name=name).first():
            flash('Item already exists!', 'error')
        else:
            item = InventoryItem(name=name, quantity=quantity)
            db.session.add(item)
            db.session.commit()
            flash('Item added successfully!')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:item_id>', methods=['POST'])
def update_quantity(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    action = request.form.get('action')
    if action == 'increment':
        item.quantity += 1
    elif action == 'decrement' and item.quantity > 0:
        item.quantity -= 1
    elif action == 'set':
        item.quantity = max(0, int(request.form.get('new_quantity', 0)))
    db.session.commit()
    flash('Quantity updated!')
    return redirect(url_for('index'))

# ←←← NEW: Edit name ←←←
@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    if request.method == 'POST':
        new_name = request.form['name'].strip()
        if new_name != item.name and InventoryItem.query.filter_by(name=new_name).first():
            flash('That name is already taken!', 'error')
        else:
            item.name = new_name
            db.session.commit()
            flash('Item name updated!')
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

# ←←← NEW: Delete item ←←←
@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash(f'{item.name} deleted permanently.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)