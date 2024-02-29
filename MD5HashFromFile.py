import hashlib
import os


def generate_md5(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()



file_path = input("Enter the path of the file > ")
file_path = file_path.strip(' "\'')


if not os.path.exists(file_path):
    print("File not found")
    exit()


md5_hash = generate_md5(file_path)
print(f"MD5 hash of the file")
print(md5_hash)

