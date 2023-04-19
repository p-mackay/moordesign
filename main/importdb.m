function importdb;
    % Program to make a GUI for modifying a mooring element in the database

    global U V W z rho
    global H B Wt Cd ME moorele
    global floats wires chains acrels cms anchors miscs format
    global typelist type list addel mat
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
    global fs
    global c


    pkg load io
    %load xlsToMat.mat % data from xlsx file contained in varable c
    load emptydb.mat %initialize empty database

    [ifile,ipath]=uigetfile({'*.xlsx'},'Load Spread Sheet');
    [a,b,c]=xlsread([ipath ifile]);
    save xlsdbdata.mat c
    [start,stop] = getxlrange(c);

    for i = 1:6
        printf("%d --- %d\n", start(1,i),stop(1,i));
    endfor


    loading=waitbar(1);
    %hardware
    for i = start(1,1):stop(1,1)
        [m,n]=size(chains);
        name = c{i,1};
        buoy = [c{i,2} c{i,3}];
        printf("buoy: %d %d\n",buoy(1),buoy(2));
        dim = [c{i,4} c{i,5} c{i,6}];
        printf("dim: %d\n",dim);
        cd = c{i,7};
        mat = c{i,8};
        % Name of element --------------------------------
        text='*                              ';
        text(1:length(name))=name;
        % Name of element --------------------------------
        % Buoyancy of element --------------------------------
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;

        % Buoyancy of element --------------------------------
        % Dimensions of element --------------------------------
        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        % Dimensions of element --------------------------------
        % Drag Coef of element --------------------------------
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        % Drag Coef of element --------------------------------
        % Material of element --------------------------------
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        % Material of element --------------------------------
        newele=[text tbuoy tdim tcd tmat];
        disp(newele)
        chains(m+1,:)=newele;
    endfor

    %--------------------------------

    %floatation
    for i = start(1,2):stop(1,2)
        [m,n]=size(floats);
        name = c{i,1};
        buoy = [c{i,2} c{i,3}];
        dim = [c{i,4} c{i,5} c{i,6}];
        cd = c{i,7};
        mat = c{i,8};
        text='*                              ';
        text(1:length(name))=name;
         
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;

        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        newele=[text tbuoy tdim tcd tmat];
        disp(newele)
        floats(m+1,:)=newele;
    endfor

    %current meters
    for i = start(1,3):stop(1,3)
        [m,n]=size(cms);
        name = c{i,1};
        buoy = [c{i,2} c{i,3}];
        dim = [c{i,4} c{i,5} c{i,6}];
        cd = c{i,7};
        mat = c{i,8};
        text='*                              ';
        text(1:length(name))=name;
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;
        %
        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        newele=[text tbuoy tdim tcd tmat];
        newele=[text tbuoy tdim tcd tmat];
%        disp(newele)
        cms(m+1,:)=newele;
    endfor
    %releases
    for i = start(1,4):stop(1,4)
        [m,n]=size(acrels);
        name = c{i,1};
        buoy = [c{i,2} c{i,3}];
        dim = [c{i,4} c{i,5} c{i,6}];
        cd = c{i,7};
        mat = c{i,8};
        text='*                              ';
        text(1:length(name))=name;
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;
        %
        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        newele=[text tbuoy tdim tcd tmat];
        newele=[text tbuoy tdim tcd tmat];
%        disp(newele)
        acrels(m+1,:)=newele;
    endfor
    %miscellaneous instruments
    for i = start(1,5):stop(1,5)
        [m,n]=size(miscs);
        name = c{i,1};
        buoy = [c{i,2} c{i,3}];
        dim = [c{i,4} c{i,5} c{i,6}];
        cd = c{i,7};
        mat = c{i,8};
        text='*                              ';
        text(1:length(name))=name;
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;
        %
        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        newele=[text tbuoy tdim tcd tmat];
        newele=[text tbuoy tdim tcd tmat];
%        disp(newele)
        miscs(m+1,:)=newele;
    endfor
    %mooring lines
    for i = start(1,6):stop(1,6)
        [m,n]=size(wires);
        name = c{i,1};
        buoy = [c{i,2} c{i,3}];
        dim = [c{i,4} c{i,5} c{i,6}];
        cd = c{i,7};
        mat = c{i,8};
        text='*                              ';
        text(1:length(name))=name;
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;
        %
        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        newele=[text tbuoy tdim tcd tmat];
        newele=[text tbuoy tdim tcd tmat];
%        disp(newele)
        wires(m+1,:)=newele;
    endfor
    %--------------------------------
    %Anchors
        [m,n]=size(anchors);
        anchors = "";
        name = "Anchor";
        buoy = [-1500 0];
        dim = [0 0 0];
        cd = 0;
        mat = 1;
        text='*                              ';
        text(1:length(name))=name;
        tbuoy='                 ';
        if abs(buoy(1)) < 1000, 
            buoy1=num2str(buoy(1),'%8.3f');
        else
            buoy1=num2str(buoy(1),'%8.2f');
        end
        buoy2=num2str(buoy(2),'%8.1f');
        tbuoy((9-length(buoy1)):8)=buoy1;  % must pad front with blanks
        tbuoy((18-length(buoy2)):17)=buoy2;
        %
        tdim='                  ';
        if dim(1) < 1000,
            dim1=num2str(dim(1),'%5.1f');
        else
            dim1=num2str(dim(1),'%5.0f');
        end
        tdim((7-length(dim1)):6)=dim1;
        dim2=num2str(dim(2),'%5.1f');
        tdim((13-length(dim2)):12)=dim2;
        dim3=num2str(dim(3),'%5.1f');
        tdim((19-length(dim3)):18)=dim3;
        tcd='     ';
        cd=num2str(cd,'%4.2f');
        tcd((6-length(cd)):5)=cd;
        tmat='  ';
        mat=num2str(mat,'%1.0f');
        tmat(2)=mat;
        newele=[text tbuoy tdim tcd tmat];
        newele=[text tbuoy tdim tcd tmat];
%        disp(newele)
        anchors(m+1,:)=newele;

        close(loading);

    format=[1,30;32,48;50,54;57,60;62,66;68,71;73,73];
    printf("Successfully Imported: %s\n",ifile);


    [ofile,opath]=uiputfile('mdcodes.mat','Save A New MDCODES.MAT');
    save ([opath ofile],'acrels','cms','format','miscs','anchors','chains','floats','wires');
    printf("Saved: %s\n",ofile);

endfunction
