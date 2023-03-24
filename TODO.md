#### 2023/03/23
- When prompting user Add:
    - Header with instructions.
    - Prompt: 
        - Option to either add to database.(addelement)
        - Or add existing element from data base.(modmoor)
    - Get Add function to work.
- Make spreadsheettoxls more robust by reading empty cells as start end blocks.
- Add feature: Import Database from xls
    - Make it read dinamically by reading headers and blank cells (to know the range).
- Add feature: Export Database to xls



Summary:
#1
### Added features:
Print out a summary of all information of a mooring.
View 2D plot of mooring.
Create a mooring by parsing an xlsx spread sheet.
### Made more efficient:
rewriting parts of code in Octave

#2
Octave/ MATLAB
Excel



####2023/03/13

- be able to add an element to a mooring by hard coding it using code that already
exists in the program.








REVERSING ORDER OF THIS FILE
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
- create a completely separate class and methods to pass values beween functions
- and in this case we are trying to get values from "getvelocity.m" -> "dismoor.m" 

#### 2023/02/22

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
    - Total Tension on Anchor ...
    - ...
    - ...
##### FEATURE
- add a functionality to import spread sheets(.xlsx) files. To automatically create a mooring
based on the information on the spread sheet.

#### 2023/02/23
- Got the desired info to print on one page.
- Format the info so it is readable. Headers, position, font size. Make it pretty.
- work on efficiency. The program runs slow currently.

#### 2023/02/27
- Got desired info to print on one page without breaking the program.
- When user hits print button force it to calculate all info.
- Force silent output to increase runtime speed

#### 2023/03/07
##### FEATURE 
- Create a "New Mooring" by importing data from an xlsx file
    - convert xlsx to mat:
        `[a,b,c]=xlsread('yourfile.xlsx')
        save yourmatfile c`
- look at the following formats and compare them:
    - database
    - moor.m
    - try to create a moor.m from the c matrix from above

##### FEATURE 
- Make the static mooring more realistic






