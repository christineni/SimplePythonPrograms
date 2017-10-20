import hashlib, random, string, numpy as np

def original_string():
    ori = hashlib.md5(b'Today is cloudy') # The original string
    hex_ori = ori.hexdigest() # The hex of the original string
    
    hex_shorten = "" 
    for i in range(6):
        hex_shorten += hex_ori[i] 
    return hex_shorten # Returns the first 6 characters of the original string

def generate_random():
    hash = ""
    for i in range(32):
        hash += random.choice(string.lowercase + string.uppercase + string.digits) # Generates a random string of 32 characters
    md5_hash = hashlib.md5(hash).hexdigest() # Generates the hash that corresponds to the string
    
    hex_shorten = "" 
    for i in range(6):
        hex_shorten += md5_hash[i]
    return hex_shorten # Returns the first 6 characters of the random string hash

def pre_image():
    count = 0
    o = original_string()
    ran = generate_random()
    while o != ran: # While the original string does not equal the randomly generated string
        count += 1 # Increase the count by 1 to count the number of trials
        ran = generate_random() # Generate a new string until the hash is the same as the original
        if o == ran:
            break
    return count # Return the number of trials it took until pre-image collision occurred

def collision():
    count = 0
    ran1 = generate_random() # Generate a hash of a random string (only the first 6 characters)
    ran2 = generate_random() # Generate another hash of another random string (only the first 6 characters)
    ran3 = ""
    arr = [ran1]
    new_arr = [ran2]

    while True: # While condition is true
        for i in arr: # For the hash in arr, if the second hash does not match the first, 
            for j in new_arr: # then generate a new hash and add it to the second array
                if (i != j): # then compare 
                    count += 1 # Increase count by 1 for every trial it runs through
                    ran3 = generate_random() # Generate a new  hash of a random string (only the first 6 characters) until it matches the first
                    new_arr.append(ran3) 
    return count # Return the number of trials it took until collision resistant occurred


pre_image()
collision()
