# Mathematics of Encryption
## Differential Equations and Linear Algebra - Associate Professor Dr. Markus Reitenbach
### Clayton Johnson, Christopher Vandermeer, Caden Anderson

## Usage
This program was created to encrypt and decrypt given messages based off an encryption scheme discussed in the assignment. The encryption keys and decryption keys are hard-coded within the program; however if another pair is used to replace these the code will not break. The given message can be of n length. The program is intended for use from a command line as follows:
```
$ python encryption_master.py --encode 'this is a test message'
encoding THIS IS A TEST MESSAGE
Your message has been encoded: DXXMHYKPOZIGZMFCXSPWWBZD
```
and decryption works similarly:
```
$ python encryption_master.py --decode 'DXXMHYKPOZIGZMFCXSPWWBZD'
decoding DXXMHYKPOZIGZMFCXSPWWBZD
Your message has been decoded: THIS IS A TEST MESSAGE  
```

It is important to note that the message will replace all special characters with a space by default. Additionally, the code is meant to only handle upper case letters. For this reason, all messages are automatically converted to upper case, thus all case-sensativity is lost.  
#### Dependencies
This program should run without errors on Windows/Mac/Linux with Python (v2 or v3). If any issues arise, please contact the owner. 

## Frequency Analysis
#### How useful is this encryption scheme?  
At an academic level, it is thought-provoking and acts as an introduction to cryptographic techniques. A basic analysis of this encryption scheme may immediately look at the frequency analysis of the encoded messages compared to the originals. An analyzation of a small example is provided below.  

| Letter | Count | Frequency |
|--------|-------|-----------|
| B	| 49×	| 5.4% |
| F	| 48×	| 5.29% |
| Z	| 48×	| 5.29% |
| P	| 47×	| 5.18% |
| T	| 42×	| 4.63% |
| I	| 40×	| 4.41% |
| N	| 40×	| 4.41% |
| E	| 37×	| 4.07% |
| O	| 37×	| 4.07% |
| Y	| 37×	| 4.07% |
| V	| 36×	| 3.96% |
| S	| 36×	| 3.96% |
| D	| 35×	| 3.85% |
| J	| 34×	| 3.74% |
| X	| 33×	| 3.63% |
| G	| 33×	| 3.63% |
| R	| 33×	| 3.63% |
| A	| 32×	| 3.52% |
| W	| 31×	| 3.41% |
| Q	| 29×	| 3.19% |
| C	| 29× | 3.19% |
| H	| 29×	| 3.19% |
| M	| 27×	| 2.97% |
| K	| 25×	| 2.75% |
| L	| 21×	| 2.31% |
| U	| 20× |	2.2%  |

From the frequency analysis (provided by [dcode.fr](https://www.dcode.fr/frequency-analysis) ) of an encrypted message, we clearly see that there is no mapped letter that is over-represented. This significantly improves the practicality of the encryption scheme; especially compared to other schemes such as a basic Caesar Cipher, which contains artifacts from the original message in the form of letter frequency.  
__Note__: For anyone pursuing serious encryption algorithms, do __not__ use the encryption scheme presented here. It is wildly insecure and not built for the real-world. This was modelled after a simplified version of the Blu-Ray Encryption Scheme, which has long been cracked.
