from flask import Flask, render_template, request, jsonify
from items import Items

app = Flask(__name__)  # Create the object for handling URIs


@app.route("/")
def root():
    """"""
    return jsonify({"Hello": "World"})


@app.route("/<string:name>")
def greeting(name="Ivan"):
    """"""
    return render_template("index.html", name=name)


@app.route("/submit", methods=["POST", "GET"])
def resource():
    """"""
    if request.method == "POST":
        # Looking for {item: Chair, price: 15.7}
        data = request.get_json()
        if data:
            item = data.get("item")
            price = data.get("price")
            if item and price:
                my_item = Items.post(item, price)
                if my_item:
                    return jsonify({my_item.item: my_item.price})
        return jsonify({"POST Error": "Introduce the right format - {}".format(data)})
    else:
        # Looking for "/submit?item=Ball"
        item = request.args.get("item")
        if item:
            my_item = Items.get(item)
            if my_item:
                return jsonify({my_item.item: my_item.price})
        return jsonify({"GET Error": "Introduce the right format - {}".format(item)})


if __name__ == "__main__":
    app.run(debug=True)  # Add this flag to being able to update the code while server is running
