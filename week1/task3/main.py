# Task 3 - data type conversion examples

# 1. int -> float
zahl_int = 5
zahl_float = float(zahl_int)
print("int to float:", zahl_int, "->", zahl_float, type(zahl_float))

# 2. float -> int (this just cuts off the decimal part, doesn't round!)
kommazahl = 7.9
ganzzahl = int(kommazahl)
print("float to int:", kommazahl, "->", ganzzahl, type(ganzzahl))

# 3. int -> string
zahl2 = 42
text = str(zahl2)
print("int to string:", zahl2, "->", text, type(text))

# 4. string -> int (only works if the string is actually a number)
zahlenstring = "123"
zahl3 = int(zahlenstring)
print("string to int:", zahlenstring, "->", zahl3, type(zahl3))

# 5. int -> boolean (0 = False, everything else = True)
zahl4 = 1
wahrheitswert = bool(zahl4)
print("int to bool:", zahl4, "->", wahrheitswert, type(wahrheitswert))
