## Blog Post API

This is a simple Flask API for creating and retrieving blog posts.

### Requirements

- Python 3.6+
- Flask

### Installation

First, clone the repository to your local machine:

```bash
git clone https://github.com/danielquintaos/p2-m10.git
```

### Navigate to the project directory:

```bash
cd p2-m10
```

### Set up a Python Virtual Environment (Optional but recommended)

   To create a virtual environment, run:
   ```
   python3 -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

### Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, use the following command:

```bash
python p2-2024-2-m10.py
```

The API will be available at http://localhost:5000.

### API Endpoints

POST /blog: Create a new blog post. The request body should be a JSON object with id, title, and content fields.
GET /blog: Retrieve all blog posts.

### Testing

To run the tests, use the following command:

```bash
python -m unittest test_api.py
```