from flask import Flask, jsonify, render_template, request
from flask_restful import Api, Resource
from items import Items

app = Flask(__name__)
api = Api(app)

# Creating endpoint for NOT restful apps
@app.route("/")  # Root
def root():
    """"""
    return jsonify({"Hello": "World"})


@app.route("/<string:name>")
def greeting(name="Ivan"):
    """"""
    return render_template("index.html", name=name)


class MyResource(Resource):
    """"""
    def get(self):
        """"""
        item = request.args.get("item")
        if item:
            my_item = Items.get(item)
            # 200 - Success, 404 - Resource not found
            return {my_item.item: my_item.price}, 200 if my_item else 404
        return {"GET Error": "Introduce the right format - {}".format(item)}, 404

    def post(self):
        """"""
        data = request.get_json()
        if data:
            item = data.get("item")
            price = data.get("price")
            if item and price:
                my_item = Items.post(item, price)
                return {my_item.item: my_item.price}, 200 if my_item else 404
        return {"POST Error": "Introduce the right format - {}".format(data)}, 404


# Setting endpoints
api.add_resource(MyResource, "/submit")

if __name__ == "__main__":
    app.run(debug=True)