# MinecraftPanoramaBlur
A program to blur minecraft panorama screenshots

## Dependencies
- Pillow
- Opencv
- NumPy

**pip/3 Installation**

> `pip/3 install pillow`

> `pip/3 install opencv-python`

> `pip/3 install numpy`
## Configuration
1. Create an `output` folder.
2. Clear minecraft `screenshots` folder (optional, reccomended).
3. You should be ready!
## Running
1. Position your minecraft player into the area where you want the screenshot to be taken from.
2. Set FoV to 90
3. Resize your minecraft window to 922x922
4. Do the following in minecraft (Do not move the player!):
> Press F1

> `/tp @p ~ ~ ~ 0 0`

> Press F2

> `/tp @p ~ ~ ~ 90 0`

> Press F2

> `/tp @p ~ ~ ~ 180 0`

> Press F2

> `/tp @p ~ ~ ~ 270 0`

> Press F2

> `/tp @p ~ ~ ~ 0 -90`

> Press F2

> `/tp @p ~ ~ ~ 0 90`

> Press F2

> Press F1

3. Open your minecraft `screenshots` folder. If you cleared it, copy and paste all the files from there and put them into the same directory as `main.py`.
4. Rename all the files accordingly:
- North → `panorama_0.png.pale`
- East → `panorama_1.png.pale`
- South → `panorama_2.png.pale`
- West → `panorama_3.png.pale`
- Up → `panorama_4.png.pale`
- Down → `panorama_5.png.pale`
5. Run the script `main.py`
6. There should be a copy of the panorama files in your output folder. Please note that these are not ready for production, it is reccomended to use an external photo editing software to manually tweak and improve the panorama files.
7. You may put this into a resource pack. (Refer to https://minecraft.gamepedia.com/Tutorials/Creating_a_resource_pack for more information)
## Issues
If there are any issues/errors with this program, please file an issue on GitHub.
