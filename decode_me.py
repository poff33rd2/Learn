# help me create a python function decode(message_file):
# • reads a set of numbers and their values from a .txt file names. the values of the numbers are words like "I", "am" "Roger" "Dave" "mark" "John" 
# • it is in a pyrmaid like structure, using a staircase formula helps organize it. 
# • decode only the last index in each case

def decode_pyramid(numbers): #define/declare the function 'decode_pyramid'
    decoded_string = '' #intialize value 'decoded_string' to accept string
    index = 0 #set the starting index to zero to start with the first value in a array

    for i in range(1, len(numbers) + 1): # a loop that goes through each number in the array
        decoded_string += chr(numbers[index]) # decoded_string is being assigned the chars from the numbers
        index += i #goes to the next step in the array of numbers
