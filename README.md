# Image Numbering Tool

This tool scans each pixel of a given image and groups similar pixels together by labelling them with the same number.
The "similarity" is determined by a user-defined tolerance of the pixel's RGB closeness, with the logic:

<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=r_1 - r_2 \leq \text{tolerance}">
</p>
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=g_1 - g_2 \leq \text{tolerance}">
</p>
<p align="center">
  <img src="https://render.githubusercontent.com/render/math?math=b_1 - b_2 \leq \text{tolerance}">
</p>

Imnum will then generate a pdf of the labelled picture.
It can either do this with all of the groups labelled on a single picture,
or it can split each group into its own page to better see each separate number.
Great for pixel art, painting, or general image analysis.

## Examples

The following are example outputs of analyzed images from the video game Minecraft.

| All-in-One               |  Expanded View           |
:-------------------------:|:-------------------------:
| <img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output-1.png" alt="bust_output.png" width="512" height="512"> | <img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-01.png" alt="bust_output-01.png" width="256" height="256"> <img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-02.png" alt="bust_output-02.png" width="256" height="256"> |


| All-in-One | Expanded View |
|------------|---------------|
| <img src="/sample%20images/bust_output-1.png" alt="bust"> |     <table>  <thead>  <tr>  <!--Z-value--></th>  <!--<th>06</th>-->  </tr>  </thead>  <tbody>  <tr>  <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-01.png" alt="bust-01.png"></td>  <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-02.png" alt="bust-02.png"></td>  </tr>  <tr>  <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-03.png" alt="bust-03.png"></td>  <td><img src="https://github.com/alecgoedinghaus/imnum/blob/main/sample%20images/bust_output_expanded/bust_output_expanded-47.png" alt="bust-47.png"></td>  </tr>  <tr>  <td>Application</td>  <td>11</td>  </tr>  <tr>  <td>Application Sub</td>  <td>00</td>  </tr>  </tbody>  </table>              |