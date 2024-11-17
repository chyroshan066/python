letter = "Hello, my name is {1} and I am from {0}"
name = "Roshan"
country = "Nepal"
cash = 4000.00987

print(f"Hello, my name is {name} and I am from {country} and I have Rs{cash:.3f}")
print(f"Hello, my name is {{name}} and I am from {{country}} and I have Rs{cash:.3f}")
print(letter.format(country, name))