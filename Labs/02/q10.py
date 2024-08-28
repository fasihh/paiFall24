def build_message(**info):
    return "\n".join([f"{detail}: {info[detail]}" for detail in info])

print(build_message(name="fasih", age=19))