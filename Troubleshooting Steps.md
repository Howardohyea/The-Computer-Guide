# Table of Contents
- [So, it's not booting](#so-its-not-booting)


# So, it's not booting
If you're reading this, I assume there is absolutely no reactions out of the PC when you're pressing the power button. There might be fans spinning but nothing coming out of the display. If that's the case, continue reading!

1. Check the cables. Odds are you forgot one of those, or even forgot to turn the PSU on. Here's a list of the cables you need.
    - 24 pin cable to the motherboard, on the right of the RAM slots.
	- 4/8/12 pin for the CPU, depending on the motherboard. The cables are all bundled together in multiples of four and marked CPU. This is on the top right of the motherboard.
	- Several cables marked PCIe, these are for the GPU, and depending on the card installed it could be 6, 8, 14, 16, or more pins. Always group one 6+2 cable into one bundle, and **never** daisy chain one 6+2 cable into two connectors on the GPU.
2. Where did you plug the display cable? If you have a discrete GPU, put the display cable in there, unless you're planning to use the integrated GPU.
3. Is the case front panel wired up? one of the cables might be in the wrong place, double check with the motherboard manual to see if that's the case.
4. A common place for builds to not boot is incorrectly is the RAM stick isn't in correctly. They require some ridiculous force to stick in and even then one side might not be inserted correctly.
5. It's hightly recommended to stick the GPU in the topmost PCIe slot. You might loose performance otherwise. 