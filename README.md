# moordesign

This is a GNU Octave adaptation of Richard Dewey's Mooring Design and Dynamics. 

# Usage and Features
- The main database is called 'mdcodes.mat', which contains Buoyancy, Weight, 
Length, Width, Diameter, Drag Coef, Material. For the following categories: 
Hardware(Shackles, Sling Link, Miller, Drop Link, Chain), Floatation devices,
Current meters, Releases, Misc Instruments and Mooring Lines.
- "Load Mooring From Excel":
Compares the names of elements from the Excel file
to the names that are in the database. If an element in the mooring is not in 
the database then you will be prompted to provide the information for that element,
it will then be added to the database. (by default it will update mdcodes.mat)
The input Excel file should be in the following format:

| Format of mooring design from Excel |
|-------------------------------------|
| Mooring Title |
| Name of element 1 |
| . |
| . |
| . |
| Name of element n |

<details>
    <summary>Click to show full example</summary>

| Mooring Title |
|------|
| 4 Vinies on 3/4" Polysteel |
| 1/2" Shackle |
| 1/2" Shackle |
| SBE37 |
| 1/2" Shackle |
| 1/2" Sling Link2 |
| 7/16" Shackle |
| 1/4" Tenex |
| 7/16" Shackle |
| 1/2" Shackle |
| AF36↑ w WH600+SBE37 ODO |
| 1/2" Shackle |
| 1/2" Shackle |
| SeapHox in Frame |
| 1/2" Shackle |
| 1/2" Shackle |
| Miller C212 |
| 1/2" Shackle |
| 1/2" Sling Link |
| 7/16" Shackle |
| 5/16" Amsteel II+ |
| 7/16" Shackle |
| 1/2" Shackle |
| SB30 |
| 1/2" Shackle |
| SM2M+ in Frame |
| 1/2" Shackle |
| 1/2" Shackle |
| SM2M+ in Frame |
| 1/2" Shackle |
| 1/2" Shackle |
| Aquadopp↓+SBE37 |
| 1/2" Shackle |
| 1/2" Shackle |
| Miller C212 |
| 1/2" Shackle |
| 1/2" Sling Link |
| 7/16" Shackle |
| 5/16" Amsteel II+ |
| 7/16" Shackle |
| 1/2" Shackle |
| AF44↑ w WH150+SBE37 ODO |
| 1/2" Shackle |
| 1/2" Shackle |
| MillerC3 |
| 1/2" Shackle |
| 5/8" Shackle |
| AR861 B2S |
| Drop Link |
| 1" Polysteel |
| 7/8" Shackle |
| 1" Chain |

</details>

- "Import Database from Excel": 
Reads an Excel file and creates a MAT file database. The Excel file should have
the following format to be read properly: Here is an example input database:

<details>
    <summary>Click to show full Excel database</summary>

The top row is not needed it is only for illustration purposes. (Shown for illustration)
| Shown for illustration | Buoyancy | Weight | Length | Width | Diameter | Drag Coef | Material |
|------------------------|----------|--------|--------|-------|----------|-----------|----------|

| Format of input Excel Database |        |   |   |   |   |     |   |
|--------------------------------|--------|---|---|---|---|-----|---|
| Hardware     |        |   |   |   |   |     |   |
| 7/16" Shackle | -0.194 | 0 | 4 | 3 | 0 | 1.3 | 1 |
| 7/16" Shackle | -0.194 | 0 | 4 | 3 | 0 | 1.3 | 1 |
| 7/16" Shackle | -0.194 | 0 | 4 | 3 | 0 | 1.3 | 1 |
| Flotation     |        |   |   |   |   |     |   |
| WB-17 | 18 | 10 | 60 | 0 | 43.2 | 1 | 1 |
| WB-17 | 18 | 10 | 60 | 0 | 43.2 | 1 | 1 |
| WB-17 | 18 | 10 | 60 | 0 | 43.2 | 1 | 1 |
| Current Meters     |        |   |   |   |   |     |   |
| ADP in Frame | . | . | . | . | . | . | . |
| ADP in Frame | . | . | . | . | . | . | . |
| ADP in Frame | . | . | . | . | . | . | . |
| Releases     |        |   |   |   |   |     |   |
| AR861 | . | . | . | . | . | . | . |
| AR861 | . | . | . | . | . | . | . |
| AR861 | . | . | . | . | . | . | . |
| Miscellaneous     |        |   |   |   |   |     |   |
| SM2M+ in Frame | . | . | . | . | . | . | . |
| SM2M+ in Frame | . | . | . | . | . | . | . |
| SM2M+ in Frame | . | . | . | . | . | . | . |
| Mooring Lines     |        |   |   |   |   |     |   |
| 5/16" Amsteel | . | . | . | . | . | . | . |
| 5/16" Amsteel | . | . | . | . | . | . | . |
| 5/16" Amsteel | . | . | . | . | . | . | . |

</details>



# Installation
## Prerequisites 
### 1. GNU Octave
### 2. files from github 
If you haven't already [download](https://octave.org/download) the latest version of 
GNU Octave.
#### Download the files:
#### Option 1: 
- Click on *Code* -> *Download ZIP* 

#### Option 2: 
`git clone https://github.com/p-mackay/moordesign`

## Running the program
Once you have Octave and the files installed. Open Octave then navigate to `moordesign/main` then enter the
command `moordesign` to run the program
```
cd moordesign/main 
moordesign
```

# Credit

[Mooring Design & Dynamics(Website)](http://web.uvic.ca/~rdewey/mooring/moordyn.php)

[Mooring Design & Dynamics(MathWorks Exchange)](http://web.uvic.ca/~rdewey/mooring/moordyn.php)


# License
Copyright (c) 2023, Richard Dewey
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution

Neither the name of University of Victoria nor the names of its
contributors may be used to endorse or promote products derived from this
software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

