# This is my solution to the www.hackthissite.org Realistic Mission 6.
# This mission is fairly simple so I have not bothered to make this work well. It only needs to work once....

# Library to get the encrypted text from a html file
import urllib3
from bs4 import BeautifulSoup

def most_common_char(enc_message):
    return max(set(enc_message), key=enc_message.count)

if __name__ == '__main__':
    # Set up urllib and set the url we are trying to fetch
    https = urllib3.PoolManager()
    url = "https://www.hackthissite.org/missions/realistic/6/index.html"

    # Fetch the html file and record the response
    response = https.request('GET', url)

    # Parse the data contained within the response using beautifulSoup
    soup = BeautifulSoup(response.data, 'html.parser')

    # Extract the encrypted message from the html file using the <pre> tag
    raw_enc_email = soup.pre.string

    # The encrypted email contains values separated by '.' characters. We can split them into a list, but only after
    # we remove the '\r' and '\n' characters, which luckily occur together. We should also remove the first entry, as
    # it will be blank since the string starts with a '.'
    raw_enc_email = raw_enc_email.replace('\r\n', '').split('.')[1:]

    # Then convert the character values from strings to integers
    encrypted_email = [int(i) for i in raw_enc_email]

    if len(encrypted_email) % 3 != 0:
        # XECryption splits the hex value of each character up into 3 parts at random. The value of each character
        # is found by adding the values together in groups of three. If there is not a multiple of 3 items in this list,
        # we may not have the full message.
        raise Exception("The number of elements in the list is not a multiple of 3. This indicates there was a " +
                        "problem fetching the file from www.hackthissite.org.")
    else:
        chars_in_message = int(len(encrypted_email) / 3)

    # Create a blank list to store our decrypted email in
    decrypted_email = []

    # Combine the values for each character together so there is 1 value per character
    for message_chars in range(0, chars_in_message):
        decrypted_email.append(sum(encrypted_email[message_chars*3:message_chars*3+3]))

    # Find the most commonly occurring character in the list. Since it is a long message this is assumed to be a space.
    space_val = most_common_char(decrypted_email)

    # Find the encryption key based on the difference between most common value in the message, and the ascii value of
    # a space.
    enc_key = space_val - 32

    # Subtract the encryption key from every value in the array to decrypt it
    decrypted_email = [i - enc_key for i in decrypted_email]

    # Convert the ascii values back to strings
    decrypted_email = ''.join(chr(val) for val in decrypted_email)

    # Print the output email
    print("Decrypted Email:\n")
    print(decrypted_email)
