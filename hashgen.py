import hashlib

text = input("Digite o texto para converter: ")
options = int(input("""# HASH GENERATOR BY mrT
                        1) MD5
                        2) SHA1
                        3) SHA256
                        4) SHA512
                        Escolha uma opção acima: """))

if (options == 1):
    result = hashlib.md5(text.encode("utf-8"))
    print("Hash MD5 gerada: ", result.hexdigest())
if (options == 2):
    result = hashlib.sha1(text.encode("utf-8"))
    print("Hash SHA1 gerada: ", result.hexdigest())
if (options == 3):
    result = hashlib.sha256(text.encode("utf-8"))
    print("Hash SHA256 gerada: ", result.hexdigest())
if (options == 4):
    result = hashlib.sha512(text.encode("utf-8"))
    print("Hash SHA512 gerada: ", result.hexdigest())
else:
    print("Algo saiu errado!")
