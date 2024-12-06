def spare_part_schema(spare_part) -> dict:
    return{
        "id": str(spare_part["_id"]),
        "part_number": spare_part["part_number"],
        "name": spare_part["name"],
        "description": spare_part["description"],
        "marca": spare_part["label"],
        "qty": spare_part["qty"]        
    }

def spare_parts_schema(spare_parts) -> list:
    return [spare_part_schema(spare_part) for spare_part in spare_parts]
