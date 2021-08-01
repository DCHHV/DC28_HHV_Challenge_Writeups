# Challenge 2

### Description:
We sniffed this capture between a microcontroller and various eeproms. Unfortunately, the capture was cutoff before we could see the results of the read. Could you figure out what would have come out from the read?

### Objective:
* Learn about i2c
* Learn about EEPROMs
* Become familiar with exporting data from Logic 1
* Write a basic script for parsing

### Difficulty:
* `easy`

### Flag:
* `flag{ii_c_y0U_Kn0w_uR_5er1aL}` 

### Challenge:

The player is provided a Logic 1 capture with two channels. By looking closer at the signals, it can be determined this is likely to be i2c. After applying the i2c analyzer and looking through the results, the player will learn there are four total EEPROMs being written too, but based on the read at the end, the EEPROM at address 0x8 has the flag. The player can then export the results and write a basic script for filtering out the writes to the 0x8 EEPROM, along with parsing the index and character for each write to recreate the flag sorted in the EEPROM's memory.

### Solver:

chal2._solver.py is a Python3 script or solving this challenge after exporting the results data. Make sure to use `Export search results` in the Decoded Protocols section, and save the export as `chal2.csv`. This script loops through the results looking for writes to the EEPROM on 0x8 i2c address, and when a write is found, it parses the index and character for the write. A global buffer is filled in with the write characters, and the character is placed in the buffer at the intended index specified in the write to recreate the flag. Finally, the flag is printed out at the end.