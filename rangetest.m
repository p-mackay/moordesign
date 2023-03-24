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
    start=1;
    stop=1;
    
    %for i = 1:m
    %    if(ca(i,1) == 0)
    %        break;
    %        count=count+1;
    %    endif
    %endfor

    for i = 1:m
        count=count+1;
        if(strcmp(c{i,1}, "Hardware")==1)
            break;
        else
        endif
    endfor
    start = start+count;
    disp(start)
    count=0;
    for i = start:m
        count=count+1;
        if(ca(i,1)==1)
            break;
        else
        endif
    endfor
    stop = stop+count;
    disp(stop)



endfunction
