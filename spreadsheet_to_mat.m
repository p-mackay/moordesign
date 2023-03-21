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

    %for j = 1:rows(wires)
    match=0;
    isele=1;
    k=1;
    disp(k)
    for i = 4:rows(c)
        printf("for... ")
        isele=rows(floats);
        while (k <= rows(floats))
            %printf("floats(k+1): %s\nc(i,1): %d",floats(k,:), c{i,1})
            if (startsWith(floats(k,:), c(i,1), "IgnoreCase", true) == 1) 
                match=match+1;

                elenum=length(B)+1;
                insert=elenum;
                mb=length(B);
                bump=[insert+1:mb+1];
                moorele(bump,:)=moorele(elenum:mb,:);
                B(bump)=B(elenum:mb);
                H(:,bump)=H(:,elenum:mb);
                Cd(bump)=Cd(elenum:mb);
                ME(bump)=ME(elenum:mb);


                moorele(elenum,:)=floats(k,format(1,1):format(1,2));
                B(elenum)=str2num(floats(k,format(2,1):format(2,2)));
                H(1,elenum)=str2num(floats(k,format(3,1):format(3,2)))/100; % convert to metres pm
                H(2,elenum)=str2num(floats(k,format(4,1):format(4,2)))/100;
                H(3,elenum)=str2num(floats(k,format(5,1):format(5,2)))/100;
                H(4,elenum)=0;
                ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
                if type == 2 || type == 3, % then a wire/chain element, get length
                    if H(1,elenum)==1,
                        getwirel;waitfor(h_edit_wirel); % wait for this window(4) to close
                        H(1,elenum)=wire_length;
                        H(4,elenum)=1; % flag for wire/chain elements, sub-divide later
                        mat=str2num(floats(k,format(7,1):format(7,2)));
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
                    end
                end
                Cd(elenum)=str2num(floats(k,format(6,1):format(6,2)));
                elenum0=elenum;
                elenum=length(B)+1;
                insert=0;
                k=k+1;
            elseif (k == rows(floats) && match == 0)
                %printf("%d\n",)
                %printf("floats(k+1): %s\nk: %d\nc(i,1): %d\n",floats(k,:),k, c{i,1})
                printf("%d\n",match)
                addelement;waitfor(h_push_save);
                set(h_edit_elename,'String',"Hello World!");

                warning("Please fill in data for the following: %s", c{i,1});
                save ('testdb5.mat','acrels','cms','format','miscs','anchors','chains','floats','wires');
                pause;
                k=1;
            else
                k=k+1;
            endif
        endwhile

        for j = 1:rows(wires)
            if (startsWith(wires(j,:), c(i,1), "IgnoreCase", true) == 1) 
                type=2;

                elenum=length(B)+1;
                insert=elenum;
                mb=length(B);
                bump=[insert+1:mb+1];
                moorele(bump,:)=moorele(elenum:mb,:);
                B(bump)=B(elenum:mb);
                H(:,bump)=H(:,elenum:mb);
                Cd(bump)=Cd(elenum:mb);
                ME(bump)=ME(elenum:mb);


                moorele(elenum,:)=wires(j,format(1,1):format(1,2));
                B(elenum)=str2num(wires(j,format(2,1):format(2,2)));
                H(1,elenum)=str2num(wires(j,format(3,1):format(3,2)))/100; % convert to metres pm
                H(2,elenum)=str2num(wires(j,format(4,1):format(4,2)))/100;
                H(3,elenum)=str2num(wires(j,format(5,1):format(5,2)))/100;
                H(4,elenum)=0;
                ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
                if H(1,elenum)==1,
                    %printf("i: %d\n", i)
                    H(1,elenum)=c{i,4};
                    H(4,elenum)=1; % flag for wire/chain elements, sub-divide later
                    mat=str2num(wires(j,format(7,1):format(7,2)));
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
                end
                Cd(elenum)=str2num(wires(j,format(6,1):format(6,2)));
                elenum0=elenum;
                elenum=length(B)+1;
                insert=0;
            endif
        endfor


        for j = 1:rows(chains)
            if (startsWith(chains(j,:), c(i,1), "IgnoreCase", true) == 1) 

                elenum=length(B)+1;
                insert=elenum;
                mb=length(B);
                bump=[insert+1:mb+1];
                moorele(bump,:)=moorele(elenum:mb,:);
                B(bump)=B(elenum:mb);
                H(:,bump)=H(:,elenum:mb);
                Cd(bump)=Cd(elenum:mb);
                ME(bump)=ME(elenum:mb);


                moorele(elenum,:)=chains(j,format(1,1):format(1,2));
                B(elenum)=str2num(chains(j,format(2,1):format(2,2)));
                H(1,elenum)=str2num(chains(j,format(3,1):format(3,2)))/100; % convert to metres pm
                H(2,elenum)=str2num(chains(j,format(4,1):format(4,2)))/100;
                H(3,elenum)=str2num(chains(j,format(5,1):format(5,2)))/100;
                H(4,elenum)=0;
                ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
                if type == 2 || type == 3, % then a wire/chain element, get length
                    if H(1,elenum)==1,
                        getwirel;waitfor(h_edit_wirel); % wait for this window(4) to close
                        H(1,elenum)=wire_length;
                        H(4,elenum)=1; % flag for wire/chain elements, sub-divide later
                        mat=str2num(chains(j,format(7,1):format(7,2)));
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
                    end
                end
                Cd(elenum)=str2num(chains(j,format(6,1):format(6,2)));
                elenum0=elenum;
                elenum=length(B)+1;
                insert=0;
            endif
        endfor




        for j = 1:rows(anchors)
            if (startsWith(anchors(j,:), c(i,1), "IgnoreCase", true) == 1) 

                elenum=length(B)+1;
                insert=elenum;
                mb=length(B);
                bump=[insert+1:mb+1];
                moorele(bump,:)=moorele(elenum:mb,:);
                B(bump)=B(elenum:mb);
                H(:,bump)=H(:,elenum:mb);
                Cd(bump)=Cd(elenum:mb);
                ME(bump)=ME(elenum:mb);


                moorele(elenum,:)=anchors(j,format(1,1):format(1,2));
                B(elenum)=str2num(anchors(j,format(2,1):format(2,2)));
                H(1,elenum)=str2num(anchors(j,format(3,1):format(3,2)))/100; % convert to metres pm
                H(2,elenum)=str2num(anchors(j,format(4,1):format(4,2)))/100;
                H(3,elenum)=str2num(anchors(j,format(5,1):format(5,2)))/100;
                H(4,elenum)=0;
                ME(elenum)=inf;  % by default set modulus of elasticity to infinity (no stretch)
                if type == 2 || type == 3, % then a wire/chain element, get length
                    if H(1,elenum)==1,
                        getwirel;waitfor(h_edit_wirel); % wait for this window(4) to close
                        H(1,elenum)=wire_length;
                        H(4,elenum)=1; % flag for wire/chain elements, sub-divide later
                        mat=str2num(anchors(j,format(7,1):format(7,2)));
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
                    end
                end
                Cd(elenum)=str2num(anchors(j,format(6,1):format(6,2)));
                elenum0=elenum;
                elenum=length(B)+1;
                insert=0;
            endif
        endfor


    endfor
    %for i = 4:rows(c)
    %    for j = 1:rows(floats)
    %        if (startsWith(floats(j,:), c(i,1), "IgnoreCase", true) == 1) 
    %            var1=floats(j,:);
    %            count = count+1;
    %            printf("Match Wires: %d --- %s \n", count,var1)
    %        endif
    %    endfor
    %endfor

    save('moor007.mat','U','V','W','z','rho','time','H','B','Cd','ME','moorele');
    load ('moor007.mat');
    moordesign(100);


endfunction
