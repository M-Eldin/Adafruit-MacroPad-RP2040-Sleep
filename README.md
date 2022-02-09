# Adafruit-MacroPad-RP2040
Sleep Functionality for Adafruit MacroPad RP2040

## Details

**This is a modification of AdaFruit project bundle found [here](https://learn.adafruit.com/macropad-hotkeys/project-code)**

_specifically_
changes to 
- code.py file 
- addition of `adafruit_displayio_sh1107_wrapper.py` to lib 
- addition of `autoscreen.py` to lib

## Setting Time to Sleep

in `code.py` 

```python
# MAIN LOOP ----------------------------

autoscreen = AutoOffScreen(60 * 5)
```
_after 5 minutes of inactivey, MacroPad enters sleep_

## Troubleshooting 

_After copying over files, Macropad updates but screen turns off and does not "wake"_ 

- Press Reset button after adding files to CIRCUITPY directoy 

![adafruit_products_MacroPad_boot_reset](https://user-images.githubusercontent.com/85906111/153274775-de28b512-bf4d-4843-bfbb-d65cfec14ca8.png)
