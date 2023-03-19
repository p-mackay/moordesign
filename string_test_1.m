%TODO 
%call subroutine that adds the element to the mooring (recycle code from modmoor.m)
%else
%   ask user to if add element to data base or
%   add from database

pkg load io
load testdb5.mat
[a,b,c]=odsread('Test_Paul1.ods');
save odsdata.mat c

count = 0
nomatch = 0
for i = 1:rows(c)-1
    for j = 1:rows(chains)
        if (startsWith(erase(chains(j,:),'"'), erase(c(i,1),'"'), "IgnoreCase", true) == 1) 
            count = count+1;
            printf("COUNT SO FAR: %d \nMatch", count)
            disp(c(i,1))

        endif
    endfor
endfor
