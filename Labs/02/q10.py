def build_message(**info):
    message = ""
    for key, value in info.items():
        message += f"{key}: {value}\n"
    return message

print(build_message(name="fasih", age=19))
