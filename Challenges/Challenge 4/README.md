# Challenge 4

### Description:
We found a strange, random 7-segment display laying around, but it was flashing too fast for us to read it. It looks like a controller was transmitted to a shift register (74HC595), and the shift register was connected to segment pins of the 7-segment display. We were only able to capture the signals latch, clock, and data signals between the controller and the shift register before we heard someone coming. Can you help us decode what was being set on the 7-segment display?

### Objective:
* Learn about shift registers
* Prompt player to look at datasheet
* Encourage the player to get creative for uncovering the 7-segment mapping

### Difficulty:
* `medium`

### Flag:
* `FLAG[LEttErS_r_hArd_with_7_SEGmEntS]` 

### Challenge:

The player is provided a Logic 1 capture with three channels, and told the channels are latch, clock, and data. The player is also provided the shift register part number (74HC595), and upon looking at the datasheet, they will learn the latch and clock lines are rising-edge triggered. The serial data can then be parsed manually, or by cleverly applying the SPI analyzer, since each event is 8 bits. To get the mapping for shift register out to 7-segment display, the player can either look for all possibly 7-segment letter decodes from the first transfer, and then match that against subsequent transfers to narrow down the mapping based on what characters would be possible, OR knowing that the flag format is `FLAG`, they can look for that in the sequence. Additionally, there are hits that this is a common-anode configuration since `0xFF` is sent a few times, and it would be unlikely that the 7-segment dot segment would be used. After correctly matching the 7-segment mapping, the player will find the string, "thE FLAG iS FLAG[LEttErS_r_hArd_with_7_SEGmEntS]".

### Solver:

N/A