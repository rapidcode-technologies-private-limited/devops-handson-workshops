from flask import Flask, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
  host="db",
  user="root",
  password="password",
  database="orders"
)

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders(
id INT AUTO_INCREMENT PRIMARY KEY,
item VARCHAR(50)
)
""")

@app.route("/order",methods=["POST"])
def order():
    item = request.json["item"]
    cursor.execute("INSERT INTO orders(item) VALUES(%s)",(item,))
    db.commit()
    return {"status":"order placed"}

app.run(host="0.0.0.0",port=5000)
