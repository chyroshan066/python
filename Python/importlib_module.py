import importlib

module = importlib.import_module("time")  # Imports module dynamically
module.sleep(2)

print("Hello World!")