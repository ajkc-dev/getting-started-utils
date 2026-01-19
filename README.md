# Getting Started Utilities

This repository contains a collection of Python utility scripts and a React component example, designed to demonstrate various coding concepts including algorithms, file handling, and type safety.

## Project Structure

```
├── components/
│   └── Button.tsx          # React Button component with Tailwind CSS
├── messy/
│   ├── binary_search.py    # Binary search implementation
│   ├── db_connect.py       # Database connection example (secure)
│   ├── fibonacci.py        # Fibonacci sequence generator
│   ├── json_reader.py      # JSON file reader with error handling
│   ├── math_ops.py         # Basic math operations
│   ├── order_system.py     # Order processing system
│   ├── process_users.py    # User dictionary processing using TypedDict
│   ├── data.json           # Sample JSON data
│   └── test_order_system.py # Unit tests for order system
└── README.md
```

## Installation

1.  **Prerequisites**: Ensure you have Python 3.7+ installed.
2.  **Dependencies**: The scripts primarily use the Python standard library. The React component requires a standard React + Tailwind setup.

## Usage

### Running Python Scripts

Navigate to the `messy` directory to run the usage examples included in the scripts:

**Math Operations**
```bash
cd messy
python math_ops.py
```

**Fibonacci Sequence**
```bash
cd messy
python fibonacci.py
```

**Binary Search**
```bash
cd messy
python binary_search.py
```

**Secure Database Connect**
*Note: Set the `DB_PASSWORD` environment variable first.*
```bash
# Windows (PowerShell)
$env:DB_PASSWORD="admin123"; python db_connect.py

# Windows (CMD)
set DB_PASSWORD=admin123 && python db_connect.py
```

### Using the Button Component

The `components/Button.tsx` is a reusable React component. Import it into your React project:

```tsx
import { Button } from './components/Button';

function App() {
  return (
    <Button variant="primary" onClick={() => console.log('Clicked!')}>
      Click Me
    </Button>
  );
}
```
