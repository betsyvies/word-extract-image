import os
from flask import Flask,request, jsonify
from ocr import process_image

app = Flask(__name__)

@app.route('/ocr', methods=["POST"])
def ocr():
    try: 
        file = request.json['image']
        output = process_image(file)
        return jsonify({"data": output})
        # { "data": output.data.replace('\r\n', ''), "color": output.color}
        # jsonify({"data": output})
    
    except:
        return jsonify(
            {"error": "Did you mean to send: {'image': 'image'}"}
        )

@app.errorhandler(500)
def internal_error(error):
    print(str(error))

@app.errorhandler(404)
def not_found_error(error):
    print(str(error))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)