import subprocess
import uuid


def create_code_file(code, language):
    file_name = str(uuid.uuid4()) + "." + language
    with open("code/" + file_name, "w") as f:
        f.write(code)
        return file_name


def execute_code_file(file_name, language):
    if language == "py":
        result = subprocess.run(["python", "code/" + file_name], stdout=subprocess.PIPE)
        return result.stdout.decode("utf")






