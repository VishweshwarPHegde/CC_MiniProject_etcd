# CC_MiniProject_etcd
Building a Distributed Key-Value Store with etcd.
This is a mini project built using **Flask** that provides a simple web interface to interact with an **etcd** key-value store. It supports listing all keys, retrieving values by key, inserting key-value pairs, and deleting keys from the etcd cluster.

## 🚀 Features

- 🔑 List all keys stored in etcd
- 📥 Retrieve a value by key
- 📤 Insert (put) a new key-value pair
- ❌ Delete a key from the store
- 🖥️ Web interface built using Flask and HTML templates

## 🛠️ Technologies Used

- Python 3
- Flask
- etcd3 (Python etcd client)
- gRPC
- HTML (Jinja2 templating)

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/etcd-flask-interface.git
   cd etcd-flask-interface
   
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Start etcd server**:
   ```bash
   etcd

4. **Run the flask app**:
   ```bash
   python app.py

5. **Access the app in your browser at**:
   ```bash
   http://127.0.0.1:5000/




