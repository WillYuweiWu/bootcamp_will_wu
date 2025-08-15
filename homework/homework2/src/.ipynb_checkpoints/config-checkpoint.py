# 1 Verify Interpreter

import sys, os
print("Python version:", sys.version)
print("Interpreter path:", sys.executable)

# 2 

try:
    import numpy as np
    from dotenv import load_dotenv
    print("Imports OK")
except Exception as e:
    print("Import error:", e)
    raise
    
