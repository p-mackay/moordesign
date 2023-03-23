function spreadsheet_to_mat 
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

    %[ifile,ipath]=uigetfile({'*.xlsx'},'Load Spread Sheet');
    %[a,b,c]=xlsread(ifile);
    %save xlsdata.mat c
    %load empty_mooring.mat

    [ifile,ipath]=uigetfile({'*.xlsx'},'Load Spread Sheet');
    [a,b,c]=xlsread(ifile);
    save xlsdata.mat c

    %elseif (ext == ".ods") % might add feature for multiple file ext's
    %    [a,b,c]=odsread(ifile);
    %    save odsdata.mat c
    %endif

    %for i = 1:rows(wires)
    %    mlist(rows(mlist)+1,:)=wires(i,:);
    %endfor
    %for i = 1:rows(anchors)
    %    mlist(rows(mlist)+1,:)=anchors(i,:);
    %endfor
    %while (j <= rows(floats))
    global all_list

    list = [""];

    
    all_list = [""];
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
    match = 0;
    flag1=0;
    for i = 4:rows(c)
        match=0;
        k=1;
        while (k <= rows(all_list))
            all_list = [""];
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
            if (startsWith(all_list(k,:), c(i,1), "IgnoreCase", true) == 1) 
                match=1;
                elenum=length(B)+1;
                insert=elenum;
                mb=length(B);
                bump=[insert+1:mb+1];
                moorele(bump,:)=moorele(elenum:mb,:);
                B(bump)=B(elenum:mb);
                H(:,bump)=H(:,elenum:mb);
                Cd(bump)=Cd(elenum:mb);
                ME(bump)=ME(elenum:mb);


                moorele(elenum,:)=all_list(k,format(1,1):format(1,2));
                B(elenum)=str2num(all_list(k,format(2,1):format(2,2)));
                H(1,elenum)=str2num(all_list(k,format(3,1):format(3,2)))/100; % convert to metres pm
                H(2,elenum)=str2num(all_list(k,format(4,1):format(4,2)))/100;
                H(3,elenum)=str2num(all_list(k,format(5,1):format(5,2)))/100;
                H(4,elenum)=0;
                ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
                if H(1,elenum)==1,
                    H(1,elenum)=c{i,4};
                    H(4,elenum)=1; % flag for wire/chain elements, sub-divide later
                    mat=str2num(all_list(k,format(7,1):format(7,2)));
                    if mat==1, % steel
                        ME(elenum)=1.38e11;
                    elseif mat==2, % Nylon
                        ME(elenum)=3.45e8;
                    elseif mat==3, % Dacron
                        ME(elenum)=8.0e8;
                    elseif mat==4, % Polyprop
                        ME(elenum)=3.45e8;
                    elseif mat==5, % Polyethy
                        ME(elenum)=6.9e8;
                    elseif mat==6, % Kevlar
                        ME(elenum)=6.9e10;
                    elseif mat==7, % Aluminum
                        ME(elenum)=7.6e10;
                    elseif mat==8, % Dyneema
                        ME(elenum)=1.0e11;
                    end
                else
                    H(4,elenum)=2; % flag for shackles and koiners
                endif
                Cd(elenum)=str2num(all_list(k,format(6,1):format(6,2)));
                elenum0=elenum;
                elenum=length(B)+1;
                insert=0;
                k=k+1;
            elseif (k == rows(all_list) && match == 0)
                %printf("%d\n",)
                %printf("list(k+1): %s\nk: %d\nc(i,1): %d\n",list(k,:),k, c{i,1})
                printf("%d\n",match)
                %addelement_xls;waitfor(h_push_save);
                addelement;waitfor(h_push_save);
                set(h_edit_elename,'String',c{i,1});

                all_list = [""];
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

                warning("Please fill in data for the following: %s", c{i,1});
                save ('testdb5.mat','acrels','cms','format','miscs','anchors','chains','floats','wires','all_list');
                pause;
                k=1;
                match=0;
            else
                k=k+1;
            endif
        endwhile
    endfor


    save('moor007.mat','U','V','W','z','rho','time','H','B','Cd','ME','moorele', 'all_list');
    load ('moor007.mat');
    moordesign(100);

endfunction
