# moordesign

This is a GNU Octave adaptation of Richard Dewey's Mooring Design and Dynamics. 

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


# Disclaimer
The user of this package takes full responsibility for designing and building a safe
and reliable mooring that will allow safe and easy deployment, and safe and easy
recovery. This set of programs is only an aide in evaluating different mooring designs
and configurations forced by varying 3D currents. It does not attempt to estimate
the forces and tensions during deployment or recovery, which may be significantly
higher than the ‘in-water/static’ tensions, as components hanging out of water will
have significantly more weight and ‘falling’ moorings will experience significant
velocities and drag. The author does not provide sources for instruments or mooring
components (i.e. wire), nor endorse the manufacturers specified strength and tension
limits. If in doubt, add a safety factor of 1.5, or larger.
This package can be used to predict wire tensions, anchor weights, and sensor
heights, potentially for backing out the actual depth/height of a mooring sensor in
a current and correcting for mooring motion. My intent is to maintain this package
as a free research tool. However, the potential uses are varied, including commercial
applications. If you use this package and find it helpful, appropriate reference to this
article or the Mooring Design and Dynamics web page is appreciated.
