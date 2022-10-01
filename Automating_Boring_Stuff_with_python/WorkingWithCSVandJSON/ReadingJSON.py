# Notice Output of this program!
import json

# Sample JSON
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsValue = json.loads(stringOfJsonData)      # Load data
print(jsonDataAsValue)      # Print data
