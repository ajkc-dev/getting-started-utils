import json
from typing import Any, Dict, Optional

def read_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    """Reads a JSON file and returns its content as a dictionary.

    Args:
        file_path: The absolute or relative path to the JSON file.

    Returns:
        A dictionary containing the JSON data if successful, None otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data: Dict[str, Any] = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from '{file_path}'. Reason: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    json_path: str = "data.json"
    
    print(f"Attempting to read from: {json_path}")
    json_data = read_json_file(json_path)

    if json_data:
        print("Successfully read JSON data:")
        print(json.dumps(json_data, indent=4))
