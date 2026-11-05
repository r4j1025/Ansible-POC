import sys
import json
 
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
 
result = num1 + num2
 
print(json.dumps({
    "status": "SUCCESS",
    "input_num1": num1,
    "input_num2": num2,
    "result": result
}))