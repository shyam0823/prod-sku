from flask import Flask, request, jsonify
from db import query_db

app = Flask(__name__)

@app.route('/spec-sku-qty', methods=['GET'])
def get_spec_sku_qty():
    itemcode = request.args.get("itemcode")

    cols = "ItemCode, OnHand"
    sql = f"SELECT {cols} FROM OITM"
    params = []
    if itemcode:
        sql += " WHERE ItemCode = ?"
        params.append(itemcode)

    return jsonify(query_db(sql, params))

if __name__ == '__main__':
    app.run(port=5003, debug=True)
