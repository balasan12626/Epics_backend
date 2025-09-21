# EPICS Sensor Data API

This project is a FastAPI application that provides an API for storing and retrieving sensor data. It uses MongoDB as the database.

## Setup

1.  **Clone the repository**

2.  **Create a virtual environment**
    ```bash
    python -m venv v
    ```

3.  **Activate the virtual environment**
    -   On Windows:
        ```bash
        v\Scripts\activate
        ```
    -   On macOS and Linux:
        ```bash
        source v/bin/activate
        ```

4.  **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  Create a file named `.env` in the root of the project.

2.  Add your MongoDB connection string to the `.env` file:
    ```
    MONGO_URI=your_mongodb_connection_string
    ```

## Running the Application

To start the server, run the following command:
```bash
python main.py
```
The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Store Sensor Data

-   **URL:** `/sensor-data`
-   **Method:** `POST`
-   **Body:**
    ```json
    {
      "name": "Sensor_1",
      "location": "Room_A",
      "spo2": 98.5,
      "alt_sensor": 1012.5,
      "temp": 22.3
    }
    ```
-   **Success Response:**
    ```json
    {
        "message": "Data stored successfully",
        "inserted_id": "...",
        "unique_id": "..."
    }
    ```

### Other Endpoints

The application also includes the following placeholder endpoints:

-   `POST /api/app/data/{id}`
-   `GET /api/app/data/{id}`
-   `GET /api/website/data`
-   `GET /api/website/data/{id}`
