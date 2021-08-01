# Challenge 3

### Description:
We sniffed another capture between two communicating parties. I think this one has more layers than the previous captures, they must know that we’re listening. See if you can capture the what was exchanged.

### Objective:
* Learn about SPI
* Analyze asynchronous serial by hand

### Difficulty:
* `medium`

### Flag:
* `flag{wh0_n33dz_F4ncY_sw?}` 

### Challenge:

The player is provided a Logic 1 capture with four channels. The player should be able to identify this is SPI based on the chip select, clock, and two serial channels. By applying the SPI analyzer and looking through the results, the player should be able to tell the MOSI is transmitting an index and the MISO is responding with one of four characters `_`, `/`, `\`, or `¯`. By following a similar procedure to the previous challenge, Challenge 2, the player will find that the the capture only communicates another asynchronous serial type string, instead of the flag. Looking deeper at this string, the player can analyze this async serial by hand (identify start and stop bits, LSBit is sent first, etc) to uncover the flag.

### Solver:

chal3._solver.py is a Python3 script or assisting in solving this challenge after exporting the results data. Make sure to use `Export search results` in the Decoded Protocols section, and save the export as `chal3.csv`. This script loops through the results and parses our the MSByte and LSByte being sent from the MOSI, as well as the associated character responded by the MISO. The MSB and LSB are combined for an index, and the character is stored at that index in a buffer. The buffer is then printed out at the end.