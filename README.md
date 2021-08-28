# Image Numbering Tool

This tool scans each pixel of a given image and groups similar pixels together by labelling them with the same number.
The "similarity" is determined by a user-defined tolerance of the pixel's RGB closeness, with the logic:

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=r_1 - r_2 \leq \text{tolerance},">
</p>
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=g_1 - g_2 \leq \text{tolerance,}">
</p>
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=b_1 - b_2 \leq \text{tolerance}.">
</p>

Imnum will then generate a pdf of the labelled picture.
It can either do this with all of the groups labelled on a single picture,
or it can split each group into its own page to better see each separate number.
Great for pixel art, painting, or general image analysis.

## Examples

The following are example outputs of analyzed images from the video game Minecraft (with a tolerance of 20).

| All-in-One | Expanded View |
|------------|---------------|
| <img src="/sample%20images/bust_output-1.png" alt="bust_output-1.png" width="256" height="256"> | <table> <tbody> <tr> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-01.png" alt="bust-01.png" width="256" height="256"></td> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-02.png" alt="bust-02.png" width="256" height="256"></td> </tr>  <tr> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-03.png" alt="bust-03.png" width="256" height="256"></td> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-47.png" alt="bust-47.png" width="256" height="256"></td> </tr> </tbody> </table> |
| <img src="/sample%20images/sunset_output-1.png" alt="sunset_output-1.png" width="256" height="128"> | <table> <tbody> <tr> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/sunset_output_expanded/sunset_output_expanded-01.png" alt="sunset-01.png" width="256" height="128"></td> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/sunset_output_expanded/sunset_output_expanded-02.png" alt="sunset-02.png" width="256" height="128"></td> </tr>  <tr> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/sunset_output_expanded/sunset_output_expanded-03.png" alt="sunset-03.png" width="256" height="128"></td> <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/sunset_output_expanded/sunset_output_expanded-20.png" alt="sunset-20.png" width="256" height="128"></td> </tr> </tbody> </table> |

## Usage

After cloning the git repository, run the following commands:

(For first time `pipenv` use)

```bash
pip install pipenv
```

Followed by:

```bash
cd imnum
pipenv install
```

Once your environment is set up, you can start the venv and run the script:

```bash
pipenv shell
python imnum.py /path/to/image.png
```

Imnum accepts most common image formats.
See the [skimage documentation](https://scikit-image.org/docs/stable/) for more details.

Flags can also be set to further customize the output.
- `-f` or `--font_size` to change the font size of the overlayed numbers. Defaulted at 6.
- `-e` or `--expand` to have the expanded view output.
- `-s` or `--scale` to downscale the image prior to analyzing the pixels.
- `-t` or `--tolerance` to adjust how similar the pixel colors can be for them to be grouped in the same category. Defaulted at 25.

For example, to get the above outputs, I used:

```bash
python imnum.py bust.png -s 10 -t 20
python imnum.py sunset.png -s 10 -t 20
```

for the standard view, and:

```
python imnum.py bust.png -s 10 -t 20 -e
python imnum.py sunset.png -s 10 -t 20 -e
```

for the expanded view.
