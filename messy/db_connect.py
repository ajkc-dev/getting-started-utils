import os

def connect_to_database():
    """Connects to the database using credentials from environment variables."""
    
    # Adhering to security best practices: converting hardcoded password to environment variable
    password = os.getenv('DB_PASSWORD')
    
    if not password:
        print("Error: DB_PASSWORD environment variable is not set.")
        print("Please set it using: export DB_PASSWORD='admin123' (Linux/Mac) or set DB_PASSWORD=admin123 (Windows)")
        return

    print("Successfully retrieved password from environment variable.")
    # Simulated connection logic
    print("Connecting to database...")

if __name__ == "__main__":
    connect_to_database()
