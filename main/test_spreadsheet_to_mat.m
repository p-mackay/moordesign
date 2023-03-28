function test_spreadsheet_to_mat 
    %TODO 
    %call subroutine that adds the element to the mooring (recycle code from modmoor.m)
    %else
    %   ask user to if add element to data base or
    %   add from database
    pkg load io

    global U V W z rho
    global H B Cd ME moorele
    global Ht Bt Cdt MEt moorelet
    global BCO ZCO Jobj Pobj
    global floats wires chains acrels cms anchors miscs format typelist type list
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
    global handle_list wire_length h_edit_wirel insert elenum delele val
    global Z Zoo
    global fs

    global type
    global nlist
    global elenum moorele insert format
    global handle_list wire_length h_edit_wirel delele 
    global ifile
    global h_push_save
    load testdb5.mat
    load empty_mooring.mat
    load xlsdata.mat
    global all_list

    all_list = [""];
    list = [""];


    for m = 1:rows(floats)
        all_list(rows(all_list)+1,:)=floats(m,:);
    endfor
    for m = 1:rows(wires)
        all_list(rows(all_list)+1,:)=wires(m,:);
    endfor
    for m = 1:rows(chains)
        all_list(rows(all_list)+1,:)=chains(m,:);
    endfor
    for m = 1:rows(anchors)
        all_list(rows(all_list)+1,:)=anchors(m,:);
    endfor

    k=1;
    match=0;
    flag1=0;

    for i = 4:rows(c)
        match=0;
        k=1;
        %printf("%s\n",c{i,1});
        while (k <= rows(all_list))
            printf("MATCH: %d\n",match);
            all_list=[""];
            for m = 1:rows(floats)
                all_list(rows(all_list)+1,:)=floats(m,:);
            endfor
            for m = 1:rows(wires)
                all_list(rows(all_list)+1,:)=wires(m,:);
            endfor
            for m = 1:rows(chains)
                all_list(rows(all_list)+1,:)=chains(m,:);
            endfor
            for m = 1:rows(anchors)
                all_list(rows(all_list)+1,:)=anchors(m,:);
            endfor
            %printf("%d: Hello: %s\n",k,all_list);
            %disp(all_list)
            %printf("floats(k+1): %s\nc(i,1): %d",floats(k,:), c{i,1})
            if (startsWith(all_list(k,:), c(i,1), "IgnoreCase", true) == 1) 


                match=1;
                %printf("1. k = %d\n",k);
                %printf("%s --- %s\n",all_list(k,:),c{i,1});
                %printf("%s\n",c{i,1});
                k=k+1;

            elseif (k == rows(all_list) && match == 0)
                printf("IS NOT IN DATABASE ADD TO DATABASE%d\n",k);
                printf("2. k = %d\n",k);
                printf("%s\n",c{i,1});
                printf("%d\n",match)

                addelement;%waitfor(h_push_save);
                set(h_edit_elename,'String',c{i,1});

                all_list=[""];
                for m = 1:rows(floats)
                    all_list(rows(all_list)+1,:)=floats(m,:);
                endfor
                for m = 1:rows(wires)
                    all_list(rows(all_list)+1,:)=wires(m,:);
                endfor
                for m = 1:rows(chains)
                    all_list(rows(all_list)+1,:)=chains(m,:);
                endfor
                for m = 1:rows(anchors)
                    all_list(rows(all_list)+1,:)=anchors(m,:);
                endfor

                disp(all_list)
                warning("Please fill in data for the following: %s", c{i,1});
                save ('testdb5.mat','acrels','cms','format','miscs','anchors','chains','floats','wires','all_list');
                load('testdb5.mat');
                pause;


                k=1;
                match=0;
            else
                printf("3. k = %d\n",k);
                %printf(all_list(k,:));
                printf("%s\n",c{i,1});
                k=k+1;
            endif
        endwhile
    endfor
endfunction
