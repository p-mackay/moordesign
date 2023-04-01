function testxls;
    % Program to make a GUI for modifying a mooring element in the database

    global U V W z rho
    global H B Cd ME moorele
    global floats wires chains acrels cms anchors miscs format
    global typelist type list addel mat
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
    global fs
    global hdr1 hdr2
    global hw


    pkg load io
    %load xlsToMat.mat % data from xlsx file contained in varable c
    %load testdb2.mat %initialize empty database
    load testdb6.mat
    hw={};

    %[ifile,ipath]=uigetfile({'*.xlsx'},'Load Spread Sheet');
    %[a,b,c]=xlsread(ifile);
    %save xlsdbdata.mat c
    %[start,stop] = rangetest(c);
    
    %hardware
    
    hdr1={'Buoyancy', 'Length', 'Width of', 'Diameter of', ...
            'Drag Coef', 'Material'};
    hdr2={'(kg)','(cm)','CYL(cm)','SPH(cm)'};

    %xlswrite('example2.xlsx',hdr1, 'Sheet1', 'B1:G1');
    
    %for i = length(hdr1)
    xlswrite('example3.xlsx',hdr1,'Sheet1','B1:G1');
    xlswrite('example3.xlsx',hdr2,'Sheet1','B2:G2');

    
    %first convert to a cell array
    for i = 1:rows(chains)
        hw(i,1)={chains(i,format(1,1):format(1,2))};
    endfor

    xlswrite('example3.xlsx',hw,'Sheet1',['A3:A' num2str(3+rows(chains))]);

    




    %xlswrite('example3.xlsx',hw,'Sheet1', 'A3:A100');







    %--------------------------------
    %format=[1,30;32,39;41,45;48,51;53,57;59,62;64,64]
endfunction

