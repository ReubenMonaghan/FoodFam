import jsonschema

schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "ingredient": {"type": "string"},
            "measurement": {"type": "string"},
            "quantity": {"type": "number"}
        },
        "required": ["ingredient", "quantity"],
        },
    "minItems": 1
    }

def validate_contributors(value):
    jsonschema.validate(data, array_schema)
