# Challenge 1

### Description:
We sniffed this capture between two communicating parties. We need help figuring out what was said? We believe a critical key was exchanged.

### Objective:
* Install and run [Saleae Logic 1](https://support.saleae.com/logic-software/legacy-software/older-software-releases#logic-1-x-download-links)
* Become familiar with basic interfacing with Logic (including using analyzer)
* Learn about basic asynchronous serial

### Difficulty:
* `very-easy`

### Flag:
* `flag{part_of_a_balanced_breakfast}` 

### Challenge:

The player is provided a Logic 1 capture with two channels. The player must look closer at this capture to identify it's using asynchronous serial and calculate the baudrate (9600). With this information, the player can apply the async serial analzer to each of the channels and read through the communication. Eventually, the communication will point to changing the baudrate (to 115200), so the player must calculate and apply that change to decode the communication segment that contains the flag.

### Solver:

N/A