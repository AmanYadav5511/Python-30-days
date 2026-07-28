t = (1, 2, 3)
try:
    t[0] = 99
except TypeError as e:
    print(f"Caught expected error: {e}\n")

temp_list = list(t)
temp_list[0]= 99
t = tuple(temp_list)
print("final updated tuple:", t)