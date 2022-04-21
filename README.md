# XECryption_Decryptor
This is a simple script I hacked together to solve the Realistic Challenge 6 of [HackThisSite](https://www.hackthissite.org/).
## About XECryption
As far as I understand it, XECryption "encrypts" a string by adding the sum of the ascii values in the password to each of the values in the message, and each character in the message is then split up into three values (apparently) at random.
## Defeating XECryption
This cipher is fairly easy to decrypt, the first step is simply to combine the values in sets of 3 to get one entry per character of the message. You can then look at the most commonly occurring value and use that to make assumptions about the "encryption key" as the same value is added to all characters. IN my example, I have assumed that a space (ASCII value 32) is the most common character since it appeared to be a long message. We can then find the difference between the value of the most common character and subtract 32 from it if we are assuming that it is a space. This gives us the "encryption key". Subtracting this key from every value will give us the (hopefully) decrypted message.

An alternative approach would be to incrementally increase the "encryption key" and run the resulting string against a dictionary of common words like "and" or "but" until those strings appear in the decrypted message, and that should hopefully be the encryption key we are looking for and give us the message.
## Using this script
I strongly encourage you to write your own version of this script, as not doing so defeats the whole point of challenge 6 otherwise. If you must run it, you need Python3 (Shame on you if you're still using Python2). To install the required libraries (beautifulsoup and urllib), you can either run `pip3 install -r requirements.txt` or `pip3 install beautifulsoup4 urllib3`. You should then be able to simply run the script using `python3 ./main.py`.

This script will automatically pull the encrypted text from [https://www.hackthissite.org/missions/realistic/6/index.html](https://www.hackthissite.org/missions/realistic/6/index.html), which contains the text under a `<pre>` tag. It shouldn't need any user input and will automatically use the space character as a guess for the most common character. It should then print the decrypted text for you to send to **ToxiCo_Watch**.
