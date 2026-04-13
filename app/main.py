import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return

    source_file = parts[1]
    destination_path = parts[2]

    if source_file == destination_path:
        return

    if destination_path.endswith("/"):
        destination_path = os.path.join(destination_path, source_file)

    directory = os.path.dirname(destination_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source_file, "r") as file_in:
        content = file_in.read()

    with open(destination_path, "w") as file_out:
        file_out.write(content)

    os.remove(source_file)
