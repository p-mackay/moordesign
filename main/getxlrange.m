function [startlist, stoplist] = getxlrange(c); 
    %accepts matrix, and a file
    %returns range indexes for each element category
    global U V W z rho
    global H B Cd ME moorele
    global floats wires chains acrels cms anchors miscs format
    global typelist type list addel mat
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
    global fs
    %global startlist stoplist
    pkg load io
    %load xlsdbdata.mat

    startlist=[];
    stoplist=[];
    ca = cellfun(@isempty,c);
    [m,n]=size(c);

    %Make this a switch statment switch on element type

%    for i = 1:m
%        if(strcmp(c{i,1}, "Hardware")==1)
%            break;
%        else
%        endif
%    endfor
%    start=i+1;
%    startlist(1,1)=start;
%    for i = start:m
%        if(ca(i,1)==1)
%            break;
%        else
%        endif
%    endfor
%    stop=i-1;
%    stoplist(1,1)=stop;
    %------------------------------------------------------------- 
    for i = 1:m
        if(strcmp(c{i,1}, "Flotation")==1)
            break;
        else
        endif
    endfor
    start=i+1;
    startlist(1,2)=start;
    for i = start:m
        if(ca(i,1)==1)
            break;
        else
        endif
    endfor
    stop=i-1;
    stoplist(1,2)=stop;

    %------------------------------------------------------------- 
%    for i = 1:m
%        if(strcmp(c{i,1}, "Current Meters")==1)
%            break;
%        else
%        endif
%    endfor
%    start=i+1;
%	startlist(1,3)=start;
%    for i = start:m
%        if(ca(i,1)==1)
%            break;
%        else
%        endif
%    endfor
%    stop=i-1;
%	stoplist(1,3)=stop;
%
%    %------------------------------------------------------------- 
%    for i = 1:m
%        if(strcmp(c{i,1}, "Releases")==1)
%            break;
%        else
%        endif
%    endfor
%    start=i+1;
%	startlist(1,4)=start;
%    for i = start:m
%        if(ca(i,1)==1)
%            break;
%        else
%        endif
%    endfor
%    stop=i-1;
%	stoplist(1,4)=stop;
%
%    %------------------------------------------------------------- 
%    for i = 1:m
%        if(strcmp(c{i,1}, "Miscellaneous Instruments")==1)
%            break;
%        else
%        endif
%    endfor
%    start=i+1;
%	startlist(1,5)=start;
%    for i = start:m
%        if(ca(i,1)==1)
%            break;
%        else
%        endif
%    endfor
%    stop=i-1;
%	stoplist(1,5)=stop;
%
%    %------------------------------------------------------------- 
%    for i = 1:m
%        if(strcmp(c{i,1}, "Mooring Lines")==1)
%            break;
%        else
%        endif
%    endfor
%    start=i+1;
%	startlist(1,6)=start;
%    for i = start:m
%        if(ca(i,1)==1)
%            break;
%        else
%        endif
%    endfor
%    %printf("start: %s\n",c{i,1});
%    stop=i;
%	stoplist(1,6)=stop;
%    %printf("stop: %d\n", stop);


endfunction
