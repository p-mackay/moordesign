function rangetest;
    % Program to make a GUI for modifying a mooring element in the database

    global U V W z rho
    global H B Cd ME moorele
    global floats wires chains acrels cms anchors miscs format
    global typelist type list addel mat
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
    global fs
    pkg load io
    load xlsdbdata.mat

    ca = cellfun(@isempty,c);
    [m,n]=size(c);
    count=0;

    %Make this a switch statment switch on element type
    for i = 1:m
        if(strcmp(c{i,1}, "Hardware")==1)
            break;
        else
        endif
    endfor
    start=i+1;
    printf("start: %d\n", start);
    for i = start:m
        if(ca(i,1)==1)
            break;
        else
        endif
    endfor
    stop=i-1;
    printf("stop: %d\n", stop);
    
    %for i = 1:m
    %    if(ca(i,1) == 0)
    %        break;
    %        count=count+1;
    %    endif
    %endfor

    %for i = 1:m
    %    count=count+1;
    %    if(strcmp(c{i,1}, "Hardware")==1)
    %        break;
    %    else
    %    endif
    %endfor
    %start = start+count;%start of Hardware range
    %count=0;
    %for i = start:m
    %    count=count+1;
    %    if(ca(i,1)==1)
    %        break;
    %    else
    %    endif
    %endfor
    %stop = stop+count; %end of Hardware range
    for i = 1:m
        if(strcmp(c{i,1}, "Flotation")==1)
            break;
        else
        endif
    endfor
    start=i+1;
    printf("start: %d\n", start);
    for i = start:m
        if(ca(i,1)==1)
            break;
        else
        endif
    endfor
    stop=i-1;
    printf("stop: %d\n", stop);



endfunction
