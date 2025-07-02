from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def handle_data():
    content = request.get_json()
    name = content.get('name')
    age = content.get('age')

    print(f"Received: Name={name}, Age={age}")

    return jsonify({"message": f"Hello {name} of age {age}, I got your message, here is the data.",
                    "comments": [
                        {
                            "id": "001",
                            "x": "2",
                            "name": "chuck"
                        },
                        {
                            "id": "007",
                            "x": "1",
                            "name": "bond"
                        },
                        {
                            "id": "045",
                            "name": "hitman",
                            "x": "264"
                        }
                    ]
                    })


if __name__ == '__main__':
    app.run(port=5000)
