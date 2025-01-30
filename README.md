# Product Service python version

The Product Service is a simple web service built using **Python** and the **Flask** web framework. It is responsible for serving the product catalog, which includes a list of products that can be fetched via a RESTful API.

## **Requirements**

- Python (latest stable version, recommended **Python 3.10+**)
- `pip` (Python package manager)

## **Setup Instructions**

1. **Update your package list** (Linux users):
   ```bash
   sudo apt update
   ```
2. **Install Python and essential build tools** (if not installed):
   ```bash
   sudo apt install python3 python3-pip python3-venv -y
   ```
3. **Create and activate a virtual environment** (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows (Command Prompt)
   ```
4. **Navigate to the `product-service` directory:**
   ```bash
   cd product-service-py
   ```
5. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
6. **Run the service:**
   ```bash
   python main.py
   ```
   The service will be running on **http://localhost:3030**.

## **Testing**
1. Install the **REST Client** extension in VS Code to use `.http` files.
2. Use the provided `test-product-service.http` file to test the service.

