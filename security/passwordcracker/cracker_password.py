import hashlib

type_of_hash = str(input('which type of hash do you want to brute force: '))
file_path = str(input('Enter path to the file to bruteforce: '))
hash_to_decrypt = str(input('Enter hash value to bruteforce: '))

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hash_word = hash_object.hexdigest()
            if hash_word == hash_to_decrypt:
                print('Found MD5 password: ' + line.strip())
                exit(0)