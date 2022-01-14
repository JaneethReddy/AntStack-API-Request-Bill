from typing import Dict
from flask import Flask, Request, request, jsonify
from datetime import datetime, time
import json

app = Flask(__name__)

# with open('templates/input.json') as inp:
#         data = json.load(inp)
def taxRate(item,price = None):
    if item == "Medicine" or item == "Food":
        return 5
    elif item == "Clothes":
        if price < 1000:
            return 5
        else:
            return 12
    elif item == "Music":
        return 3
    elif item == "Imported":
        return 18
    elif item == "Book":
        return 0

# print(json.dumps(data, indent=2))



@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.json
    total_tax = 0
    amount_payable = 0 
    for opt in data:
        tax_rate = taxRate(opt["itemCategory"], opt["price"])
        tax = ((tax_rate/100)*opt["price"]) 
        finalPrice = opt["price"] + tax
        opt["taxRate"] = tax_rate
        opt["tax"] = tax
        opt["finalPrice"] = finalPrice
        total_tax = total_tax + tax
        amount_payable = amount_payable + finalPrice
    if amount_payable > 2000:
        amount_payable = amount_payable - ((5/100)*amount_payable)
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    data.append({"time": dt_string})
    data.append({"total_tax": total_tax})
    data.append({"amount_payable": amount_payable})
    receipt = dict()
    receipt["Date & Time"] = data[len(data)-3]['time']
    det = []
    for i in range(len(data)):
        if i >= len(data) - 3:
            break
        det.append("  " + data[i]['item'] + "  Price : " + str(data[i]['price']) + "  Tax_Rate : " + str(data[i]['taxRate']) + " Tax_Amount : " + str(data[i]['tax']) )
    det.sort()
    for i in range(len(det)):
        key = "Item " + str(i + 1)
        receipt[key] = det[i]
    receipt['Total Amount'] = data[len(data)-1]['amount_payable']
    receipt = jsonify(receipt)
    return receipt


if __name__ == '__main__':
    app.run(debug=True)