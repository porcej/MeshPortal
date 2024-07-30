
# Meshtastic MQTT Flask Interface

This project provides a web interface for viewing and sending MQTT messages to a Meshtastic device using Python Flask. The application connects to an MQTT broker, subscribes to a specified topic, and allows users to send messages via the web interface.

## Prerequisites

- Python 3.x
- MQTT Broker
- Meshtastic device

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/porcej/MeshPortal.git
   cd MeshPortal
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip -r requirements.txt
   ```

## Configuration

Set the following environment variables for configuration:

- `MQTT_BROKER`: The address of your MQTT broker.
- `MQTT_PORT`: The port of your MQTT broker (default: 1883).
- `MQTT_USERNAME`: The username for MQTT authentication.
- `MQTT_PASSWORD`: The password for MQTT authentication.
- `FLASK_WEB_HOST`: The host address for the Flask application (default: `0.0.0.0`).
- `FLASK_WEB_PORT`: The port for the Flask application (default: `8080`).
- `FLASK_DEBUG`: Enable/disable Flask debug mode (default: `False`).

Example of setting environment variables:

On Unix-like systems:
```bash
export MQTT_BROKER='your_mqtt_broker_address'
export MQTT_PORT='1883'
export MQTT_USERNAME='your_mqtt_username'
export MQTT_PASSWORD='your_mqtt_password'
export FLASK_WEB_HOST='0.0.0.0'
export FLASK_WEB_PORT='8080'
export FLASK_DEBUG='True'
```

On Windows:
```cmd
set MQTT_BROKER=your_mqtt_broker_address
set MQTT_PORT=1883
set MQTT_USERNAME=your_mqtt_username
set MQTT_PASSWORD=your_mqtt_password
set FLASK_WEB_HOST=0.0.0.0
set FLASK_WEB_PORT=8080
set FLASK_DEBUG=True
```

## Running the Application

1. Ensure your Meshtastic device is connected and the MQTT broker is running.

2. Run the Flask application:

   ```bash
   python app.py
   ```

3. Open your browser and navigate to `http://<FLASK_WEB_HOST>:<FLASK_WEB_PORT>` (e.g., `http://0.0.0.0:8080`).

## Project Structure

```
MeshPortal/
├── app.py
├── LICENSE
├── README.md
├── requirements.txt
├── static/
│   └── js
│       └── script.js
├── templates/
│   └── index.html
```

- `app.py`: Main Flask application file.
- `templates/index.html`: HTML template for the web interface.
- `static/js/script.js`: JavaScript file for fetching and sending messages.

## Usage

### Viewing Messages

The web interface will automatically fetch and display messages received from the Meshtastic device via MQTT.

### Sending Messages

To send a message, enter your message in the input field and click the "Send" button. The message will be published to the MQTT topic and sent to the Meshtastic device.

## License

This project is licensed under the MIT License.