# XECryption_Decryptor
This is a simple script I hacked together to solve the realistic challenge 6 of [hackthissite](https://www.hackthissite.org/).
## About XECryption
As far as I understand it, XECryption "encrypts" a string by adding the sum of the ascii values in the password to each of the values in the message, and each character in the message is then split up into three values (apparently) at random.
## Defeating XECryption
This cipher is fairly easy to decrypt, the first step is simply to combine the values in sets of 3 to get one entry per character of the message. You can then look at the most commonly occurring value and use that to make assumptions about the "encryption key" as the same value is added to all characters. IN my example, I have assumed that a space (ASCII value 32) is the most common character since it appeared to be a long message. We can then find the difference between the value of the most common character and subtract 32 from it if we are assuming that it is a space. This gives us the "encryption key". Subtracting this key from every value will give us the (hopefully) decrypted message.

An alternative approach would be to incrementally increase the "encryption key" and run the resulting string against a dictionary of common words like "and" or "but" until those strings appear in the decrypted message, and that should hopefully be the encryption key we are looking for and give us the message.
