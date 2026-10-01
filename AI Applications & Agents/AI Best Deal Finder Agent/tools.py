import json
from search import find_deals

find_deals_desc = {
    "name": "find_deals",
    "description": "Fetch list of 40 products from daraz (A Pakistani E-commerce Website)",
    "parameters": {
        "product_name": {
            "type": "string",
            "description": "The name of a product user want to get deals of"
        }
    },
    "required": ["product_name"],
    "additionalProperties": False
}

tools = [{
    "type": "function",
    "function": find_deals_desc
}]

def handle_tool_calls(message):
    
    response = []
    for tool_call in message.tool_calls:
        
        if tool_call.function.name == "find_deals":
            
            arguments = json.loads(tool_call.function.arguments)
            product_name = arguments.get("product_name")
            items = find_deals(product_name)
            
            response.append({
                "role": "tool",
                "content": items,
                "tool_call_id": tool_call.id
            })
            
    return response
