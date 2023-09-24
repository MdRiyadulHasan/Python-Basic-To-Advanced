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

# Calculate the length of the JSON object
length_of_json = len(data)

# Print the length
print("Length of JSON object:", length_of_json)
