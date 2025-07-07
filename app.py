from flask import Flask, render_template, request
import etcd3
import grpc

app = Flask(__name__)

# Connect to the etcd cluster
try:
    client = etcd3.client()
except grpc.RpcError as e:
    print("Connection Error: Unable to connect to the etcd cluster.")
    exit()

def list_all_keys():
    try:
        all_data = client.get_all()
        return all_data
    except grpc.RpcError as e:
        return None

def get_value(key):
    try:
        value = client.get(key)
        if value is not None:
            return f"Value for key {key}: {value[0].decode('utf-8')}"
        else:
            return f"No value found for key {key}"
    except Exception as e:
        return f"Error: {e}"

def put_key_value(key, value):
    try:
        client.put(key, value)
        return f"Key: {key}, Value: {value} successfully stored"
    except grpc.RpcError as e:
        return f"Error: Unable to store key-value pair. Reason: {e.details()}"

def delete_key(key):
    try:
        deleted = client.delete(key)
        if deleted:
            return f"Key: {key} deleted successfully"
        else:
            return f"Key: {key} not found"
    except grpc.RpcError as e:
        return f"Error: Unable to delete key. Reason: {e.details()}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_keys')
def list_keys():
    keys = list_all_keys()
    return render_template('list_keys.html', keys=keys)

@app.route('/get_value', methods=['POST'])
def get_value_route():
    key = request.form['key']
    value = get_value(key)
    return render_template('get_value.html', key=key, value=value)

@app.route('/put_key_value', methods=['POST'])
def put_key_value_route():
    key = request.form['key']
    value = request.form['value']
    message = put_key_value(key, value)
    return render_template('put_key_value.html', message=message)

@app.route('/delete_key', methods=['POST'])
def delete_key_route():
    key = request.form['key']
    message = delete_key(key)
    return render_template('delete_key.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
