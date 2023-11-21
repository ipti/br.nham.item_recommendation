
from flask import Flask, request, jsonify
from teste import ItemFinder

app = Flask(__name__)

@app.route('/find_item', methods=['POST'])
def find_item():
    data = request.get_json()
    item_finder = ItemFinder('output_data.json')
    result = item_finder.find_item(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)