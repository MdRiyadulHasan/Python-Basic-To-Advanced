import json

# Your JSON data as a string
json_data = '''
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
'''

# Parse the JSON data into a Python dictionary
data = json.loads(json_data)

# Get the keys of the JSON object
keys_of_json = data.keys()

# Convert the keys to a list if needed
keys_list = list(keys_of_json)

# Print the keys
print("Keys of JSON object:", keys_list)
