import os
from flask import Flask, render_template, json, request
from model.product import Product

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ac03:123456@db:5432/products'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/", methods=['GET'])
def home():
    return render_template('signup.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    nome = request.form['nome']
    categoria = request.form['categoria']
    preco = request.form['preco']

    try:
        if nome and categoria and preco:
            db.create_all()
            db.session.commit()

            product = Product(name=nome, category=categoria,
                        price=preco)

            db.session.add(product)
            db.session.commit()
            return render_template('signup.html')
    except Exception as e:
        print(e)
        return e


@app.route('/list')
def list():
    all_products = []
        products = Product.query.all()
        for product in products:
            result = {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
            }
            all_products.append(result)
    return render_template("list.html", rows=all_products)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5005))
    app.run(host='0.0.0.0', port=port)

