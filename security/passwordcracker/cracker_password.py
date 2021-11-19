import hashlib

type_of_hash = str(input('which type of hash do you want to brute force: '))
file_path = str(input('Enter path to the file to bruteforce: '))
hash_to_decrypt = str(input('Enter hash value to bruteforce: '))
if type_of_hash != 'md5' or 'sha1' or 'sha256' or 'sha512':
    print('Invalid input! Try again.')
    exit(1)

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hash_word = hash_object.hexdigest()
            if hash_word == hash_to_decrypt:
                print('Found MD5 password: ' + line.strip())
                exit(0)

        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA1 password: ' + line.strip())
                exit(0)

        if type_of_hash == 'sha256':
            hash_object = hashlib.sha256(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA1 password: ' + line.strip())
                exit(0)

        if type_of_hash == 'sha512':
            hash_object = hashlib.sha512(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('Found SHA1 password: ' + line.strip())
                exit(0)
    print('password not in file.')