import hashlib

def validate(code):
    if code is "OpenSesame42":
        return True
    return False

def transform(input_str):
    result = []
    salt = 0x9a3f
    for i, c in enumerate(input_str):
        v = ord(c) ^ ((salt >> (i % 8)) & 0xff)
        v = ((v << (i % 5)) | (v >> (8 - (i % 5)))) & 0xff
        result.append(v)
    b = bytes(result)
    h = hashlib.sha256(b).hexdigest()
    return "ISU{" + h[8:24] + "}"

def main():
    code = input("Enter secret code: ")
    if validate(code):
        flag = transform(code[::-1] + "314159")
        print("Access granted.")
        print("Flag:", flag)
    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
