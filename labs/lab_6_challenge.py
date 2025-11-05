raw_data = input("Welcome to our store manager! Please enter your choice among:\n(1) (V)iew our restock queue\n(2) Add a (R)egular delivery\n(3) Add an (U)rgent delivery\n(4) (E)xit\n")

inventory_list = []
display = None
inventory_list_cleaned = []

def process_data(raw_data):
    inventory_list = raw_data.split(";")

    for i in inventory_list:
        name_count = i.split(":")
        
        
        display = f"{name_count[0]} ({name_count[1]} in stock)"

        inventory_list_cleaned.append(display)

process_data(raw_data)

inventory_list_cleaned.append("Headsets (18 in stock)")
inventory_list_cleaned.insert(0, "Hard drives (Urgent Restock)")

inventory_list_cleaned = "\n".join(inventory_list_cleaned)

print(f"-- FINAL INVENTORY STATUS --\n{inventory_list_cleaned}")