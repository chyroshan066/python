'''import converter  # This statement imports whole module
print(converter.kg_to_lbs(70)'''

import converter as con  # Renaming a module

# from converter import kg_to_lbs
print(con.kg_to_lbs(90))

print(dir(con))  # Lists all the member data and member functions