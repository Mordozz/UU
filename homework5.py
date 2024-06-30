immutable_var = 1, 2, "a", "b"
print(f"Immutable tuple: {immutable_var}")

mutable_list = []
for item in immutable_var:
    mutable_list.append(item)

mutable_list.append("Modified")
print(f"Mutable list: {mutable_list}")