from typing import List, TypedDict

class User(TypedDict):
    """Definition of a User dictionary structure."""
    id: int
    name: str
    email: str
    is_active: bool

def process_users(users: List[User]) -> None:
    """Processes a list of user dictionaries and prints active users.

    Args:
        users: A list of User dictionaries.
    """
    if not users:
        print("No users to process.")
        return

    print(f"Processing {len(users)} users...")
    
    for user in users:
        # Validating structure implicitly via type hint expectations, 
        # but runtime check is good for robustness if data comes from untrusted source.
        # Here we assume data adheres to the TypedDict for the sake of the example logic.
        
        if user['is_active']:
            print(f"Active User: {user['name']} (ID: {user['id']}) - Email: {user['email']}")
        else:
            print(f"Inactive User: {user['name']} (ID: {user['id']})")

if __name__ == "__main__":
    # Example data adhering to the User TypedDict
    sample_users: List[User] = [
        {"id": 1, "name": "Alice Smith", "email": "alice@example.com", "is_active": True},
        {"id": 2, "name": "Bob Jones", "email": "bob@example.com", "is_active": False},
        {"id": 3, "name": "Charlie Brown", "email": "charlie@example.com", "is_active": True},
    ]

    try:
        process_users(sample_users)
    except KeyError as e:
        print(f"Error: Missing key in user data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
