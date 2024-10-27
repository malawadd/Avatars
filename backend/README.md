
# Chat API Backend

This project is a simple chat API  that utilizes the `swarmzero` and `langtrace-python-sdk` libraries.

## Requirements

- Python 3.7+
- `swarmzero`
- `langtrace-python-sdk`

## Installation


### 1. Create a virtual environment

It's recommended to create a virtual environment to manage dependencies:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```
- **On Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

### 2. Install dependencies

The dependencies are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

Ensure your `requirements.txt` contains:
```
swarmzero
langtrace-python-sdk
```

### 4. Add Environment Variables

Create a `.env` file in the root directory to store environment variables if needed:

```
MODEL=gpt-4o
OPENAI_API_KEY=

```

### 5. Configure the Agent

Ensure that you have a valid configuration file named `swarmzero_config.toml` in the same directory as the script. Adjust the configuration based on your requirements.

### 6. Start the API Server

Run the API server:


```bash
python chat.py
```

The server will start on `http://localhost:5450`.

## Usage

### Endpoints

- **GET** `/chat`: Chat endpoint that returns a response to a given prompt.

#### Example cURL Request:

```bash
curl "http://localhost:5450/chat?prompt=whats+the+origin+of+pi"
```


### Client Integration

You can use the API from any client-side code, such as JavaScript, using a library like Axios.
