function spreadsheet_to_mat
    %TODO
    %call subroutine that adds the element to the mooring (recycle code from modmoor.m)
    %else
    %   ask user to if add element to data base or
    %   add from database
    pkg load io

    global U V W z rho
    global H B Wt Cd ME moorele
    global Ht Bt Cdt MEt moorelet
    global BCO ZCO Jobj Pobj
    global floats wires chains acrels cms anchors miscs format typelist type list
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd hmaincls
    global h_edit_wirel
    global handle_list wire_length  insert elenum delele val
    global Z Zoo
    global fs
    global this_moorele

    global all_list
    global type
    global nlist
    global ifile
    global add_name add_buoy add_length
    global moorname moordepth dep
    #global h_push_save
    load mdcodes.mat
    load empty_mooring.mat
    global testlen




    %[ifile,ipath]=uigetfile({'*.xlsx'},'Load Spread Sheet');
    %[a,b,c]=xlsread(ifile);
    %save xlsdata.mat c
    %load empty_mooring.mat

    [ifile,ipath]=uigetfile({'*.xlsx'},'Load Spread Sheet');
    [a,b,c]=xlsread([ipath ifile]);
    save xlsdata1.mat c
    load xlsdata1.mat

    moorname = c{1,1};
    moordepth=num2str(c{2,1});
    dep = [moordepth ' 20 0'];

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

    add_name = "";
    ca = cellfun(@isempty,c);

    for i = 3:rows(c)
        if(ca(i,1)==0)
            break;
        else
        endif
    endfor
    start=i;

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
    for m = 1:rows(acrels)
        all_list(rows(all_list)+1,:)=acrels(m,:);
    endfor
    for m = 1:rows(cms)
        all_list(rows(all_list)+1,:)=cms(m,:);
    endfor
    for m = 1:rows(anchors)
        all_list(rows(all_list)+1,:)=anchors(m,:);
    endfor
    for m = 1:rows(miscs)
        all_list(rows(all_list)+1,:)=miscs(m,:);
    endfor

    count = 0;
    k=1;
    match = 0;
    flag1=0;
    for i = start:rows(c)
        if startsWith(c(i,1),"estimated")
            break;
        else
            match=0;
            k=1;
            testlen={};
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
                for m = 1:rows(acrels)
                    all_list(rows(all_list)+1,:)=acrels(m,:);
                endfor
                for m = 1:rows(cms)
                    all_list(rows(all_list)+1,:)=cms(m,:);
                endfor
                for m = 1:rows(anchors)
                    all_list(rows(all_list)+1,:)=anchors(m,:);
                endfor
                for m = 1:rows(miscs)
                    all_list(rows(all_list)+1,:)=miscs(m,:);
                endfor
                tmp = strsplit(all_list(k,1:30), "  ");
                testlen = length(tmp{1,1});
                %if (startsWith(all_list(k,testlen), c(i,1), "IgnoreCase", true) == 1)
                if (startsWith(all_list(k,1:testlen), c(i,1), "IgnoreCase", true) == 1) && (testlen == length(c{i,1}))
                    %printf("%d == %d   %s == %s\n",testlen,length(c{i,1}), c{i,1}, tmp{1,1});
                    ldng = waitbar(1);
                    match=1;
                    elenum=length(B)+1;
                    insert=elenum;
                    mb=length(B);
                    bump=[insert+1:mb+1];
                    moorele(bump,:)=moorele(elenum:mb,:);
                    B(bump)=B(elenum:mb);
                    Wt(bump)=Wt(elenum:mb);
                    H(:,bump)=H(:,elenum:mb);
                    Cd(bump)=Cd(elenum:mb);
                    ME(bump)=ME(elenum:mb);


                    moorele(elenum,:)=all_list(k,format(1,1):format(1,2));
                    BW=str2num(all_list(k,format(2,1):format(2,2)));
                    B(elenum)=BW(1);Wt(elenum)=BW(2); % for floats we need weight (Wt)
                    H(1,elenum)=str2num(all_list(k,format(3,1):format(3,2)))/100; % convert to metres pm
                    H(2,elenum)=str2num(all_list(k,format(4,1):format(4,2)))/100;
                    H(3,elenum)=str2num(all_list(k,format(5,1):format(5,2)))/100;
                    H(4,elenum)=0;
                    ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
                    %printf("Line %d, %s\n",moorele(elenum,:));
                    if H(1,elenum)==1,
                        printf("**Please provide WIRE LENGTH for: %s**\n",c{i});
                        % TODO have wire length automatically read from the spreadsheet
                        % For now enter manually
                        getwirel(0,moorele(elenum,:));waitfor(h_edit_wirel);
                        H(1,elenum)=wire_length;
                        H(4,elenum)=1; % flag for wire/chain elements, sub-divide later
                        %break;
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
                        H(4,elenum)=2; % flag for shackles and joiners
                    endif
                    Cd(elenum)=str2num(all_list(k,format(6,1):format(6,2)));
                    elenum0=elenum;
                    elenum=length(B)+1;
                    insert=0;
                    k=k+1;
                elseif (k == rows(all_list) && match == 0)
                    %printf("%d\n",)
                    %printf("list(k+1): %s\nk: %d\nc(i,1): %d\n",list(k,:),k, c{i,1})
                    %printf("%d\n",match)
                    %addelement_xls2;waitfor(h_push_save);
                    %addelement_xls2;
                    addelement;

                    set(h_edit_elename,'String',c{i});
                    add_name=get(h_edit_elename, 'String');
                    warning("Please fill in data for the following: %s", c{i,1});
                    %pause;
                    k=1;
                    match=0;
                    %waitfor(h_push_add);
                    save ('mdcodes.mat','acrels','cms','format','miscs','anchors','chains','floats','wires','all_list');
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
                    for m = 1:rows(acrels)
                        all_list(rows(all_list)+1,:)=acrels(m,:);
                    endfor
                    for m = 1:rows(cms)
                        all_list(rows(all_list)+1,:)=cms(m,:);
                    endfor
                    for m = 1:rows(anchors)
                        all_list(rows(all_list)+1,:)=anchors(m,:);
                    endfor
                    for m = 1:rows(miscs)
                        all_list(rows(all_list)+1,:)=miscs(m,:);
                    endfor
                    waitfor(h_edit_elename);
                    %waitfor(hmaincls);figure(4);clf;drawnow;close;
                else
                    k=k+1;
                endif
            endwhile
        endif
    endfor

    %If last element in the mooring is not an anchor then add a default anchor
    lastElement = moorele(end, :);
    if !strcmp(strtrim(lastElement), 'Anchor')
        elenum=length(B)+1;
        insert=elenum;
        mb=length(B);
        bump=[insert+1:mb+1];
        moorele(bump,:)=moorele(elenum:mb,:);
        B(bump)=B(elenum:mb);
        Wt(bump)=Wt(elenum:mb);
        H(:,bump)=H(:,elenum:mb);
        Cd(bump)=Cd(elenum:mb);
        ME(bump)=ME(elenum:mb);
        moorele(elenum,:)=anchors(1,format(1,1):format(1,2));
        BW=str2num(anchors(1,format(2,1):format(2,2)));
        B(elenum)=BW(1);Wt(elenum)=BW(2); % for floats we need weight (Wt)
        H(1,elenum)=str2num(anchors(1,format(3,1):format(3,2)))/100; % convert to metres pm
        H(2,elenum)=str2num(anchors(1,format(4,1):format(4,2)))/100;
        H(3,elenum)=str2num(anchors(1,format(5,1):format(5,2)))/100;
        H(4,elenum)=0;
        ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
        Cd(elenum)=str2num(anchors(1,format(6,1):format(6,2)));
        elenum0=elenum;
        elenum=length(B)+1;
        insert=0;
    end


    close(ldng);


    save('moor007.mat','U','V','W','z','rho','time','H','B', 'Wt' ,'Cd','ME','moorele', 'all_list');
    load ('moor007.mat');
    moordesign(100);

endfunction
