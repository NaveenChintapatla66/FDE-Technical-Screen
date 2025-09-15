# Package Sorting
This small project simulates how a robotic arm in **Thoughtful’s automation factory** decides where a package should go.  
Each package is checked based on its size and weight, and then sent to the right stack.

## Sorting Rules
- A package is considered **bulky** if:
  - Its volume (width × height × length) is **1,000,000 cm³ or more**, or  
  - Any single dimension is **150 cm or more**.
- A package is considered **heavy** if its mass is **20 kg or more**.
- Based on these checks, the package goes into one of three stacks:
  - **STANDARD** - not bulky and not heavy  
  - **SPECIAL** - either bulky or heavy  
  - **REJECTED** - both bulky and heavy  

## How It Works
The logic is implemented in Python inside 'sort_packages.py'
