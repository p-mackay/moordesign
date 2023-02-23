#### 2023/02/17

- figuring out how to get the "print" pop up menu on Windows 10.
    - Could be an admin issue. Testing on my personal machine to figure out if it is an admin issue.
    - CUPS/Printer sharing - archwiki
    - https://wiki.octave.org/Uicontrols

- need to add velocity profiles to the print-out, and potentially other information.

#### 2023/02/21

- potential bug when using octave gui: have to delete the following file: C:\Users\<USERNAME>\AppData\Roaming\octave\octave-gui.ini
- adding "getvelocity" to the main print function
- need the following in text file created:
    - at the top Height U V W Density
    - headers describing what each column is

##### SOLUTION
- create a completely seperate class and methods to pass values beween functions
- and in this case we are trying to get values from "getvelocity.m" -> "dismoor.m" 

#### 2023/02/22

## CURRENTLY WORKING ON: 
- IMPLEMENT OBJECT ORIENTED PROGRAMMING 
    - Mooring class
        - velocity
        - height
        - desnity
        - etc
- working on the output text file: see "DESIRED\_OUTPUT.txt"
    - header
    - Height U V W Density
    - output when plotting the 3d model
    - This is a sub-surface solution.
    Total Tension on Anchor ...
    ...
    ...
##### FEATURE
- add a functionality to import spread sheets(.xlsx) files. To automatically create a mooring
based on the information on the spread sheet.

