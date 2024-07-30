import os
from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

# MQTT Configuration
MQTT_BROKER = 'mqtt.meshtastic.org'
MQTT_PORT = 1883
MQTT_TOPIC = 'msh/US'
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')

# Web Host, Port, and Debug Configuration
WEB_HOST = os.getenv('FLASK_WEB_HOST', '0.0.0.0')
WEB_PORT = int(os.getenv('FLASK_WEB_PORT', 8080))
DEBUG_MODE = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't', 'y', 'yes']

# Global variable to store messages
messages = []

# MQTT Client Setup
mqtt_client = mqtt.Client()

# Set username and password
mqtt_client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"Received message: {message}")
    messages.append(message)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']
    mqtt_client.publish(MQTT_TOPIC, message)
    return jsonify({"status": "Message sent"})

if __name__ == '__main__':
    app.run(host=WEB_HOST, port=WEB_PORT, debug=DEBUG_MODE)
