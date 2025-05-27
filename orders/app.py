from flask import Flask, jsonify
import redis
import requests
import mysql.connector
import time
import sys

app = Flask(__name__)

def connect_redis():
    max_retries = 10
    for i in range(max_retries):
        try:
            cache = redis.Redis(host='redis', port=6379, decode_responses=True)
            cache.ping()
            return cache
        except Exception as e:
            print(f"Tentativa {i+1} de conectar ao Redis falhou: {e}")
            time.sleep(2)
    raise Exception("Não foi possível conectar ao Redis")

def connect_mysql():
    max_retries = 10
    for i in range(max_retries):
        try:
            db = mysql.connector.connect(
                host="db",
                user="root",
                password="example",
                database="ecommerce"
            )
            return db
        except Exception as e:
            print(f"Tentativa {i+1} de conectar ao MySQL falhou: {e}")
            time.sleep(2)
    raise Exception("Não foi possível conectar ao MySQL")

@app.route('/order')
def create_order():
    try:
        cache = connect_redis()
        
        # Verificar cache
        cached = cache.get('product')
        if cached:
            product = eval(cached)
            print("Produto obtido do cache")
        else:
            print("Buscando produto da API...")
            r = requests.get('http://products:3001/products', timeout=10)
            product = r.json()['products'][0]
            cache.set('product', str(product), ex=300)  # Cache por 5 minutos
            print("Produto salvo no cache")

        # Conectar ao MySQL
        db = connect_mysql()
        cursor = db.cursor()
        
        # Criar tabela se não existir
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                product_id INT, 
                quantity INT, 
                total_price INT
            )
        """)
        
        # Inserir pedido
        cursor.execute(
            "INSERT INTO orders (product_id, quantity, total_price) VALUES (%s, %s, %s)", 
            (product['id'], 2, product['price'] * 2)
        )
        db.commit()
        cursor.close()
        db.close()

        return jsonify({
            "order_id": 101,
            "product_id": product['id'],
            "quantity": 2,
            "total_price": product['price'] * 2
        })
    
    except Exception as e:
        print(f"Erro: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002, debug=True)