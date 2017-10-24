myndir = ["Batman", "Forest Gump", "Ninja"]


print(type(myndir))


import json

# Use json.dumps to convert best_food_chains to a string
myndir_string = json.dumps(myndir)

# We've successfully converted our list to a string.
print(type(myndir_string))

# Convert best_food_chains_string back into a list
print(type(json.loads(myndir_string)))

# Make a dictionary
bestu_myndir = {
    "batman": 24722,
    "rush": 14098,
    "ninja": 10821,
    "forest gump": 7600
}

# We can also dump a dictionary to a string and load it.
myndir_string = json.dumps(bestu_myndir)
print(type(myndir_string))
