function exportdb1;
    % Program to make a GUI for modifying a mooring element in the database
    %{
    The variable chains is a char array. I think you should take the text out and then the numbers out and write them separately.

    For the text,

    txt = cellstr (chains(:,1:30));
    xlswrite(thisxl,txt,'Sheet1', 'A3');
    The last argument for xlswrite anchors the top-left corner of where the data will be placed and the lower right-hand corner is determined by the size of the data itself—no need to be fancy and try to calculate the range yourself.

    The numeric data can be extracted with

    data = str2num (chains(:,31:end));
    xlswrite(thisxl,data,'Sheet1', 'B3');
    %}

    global U V W z rho
    global H B Wt Cd ME moorele
    global floats wires chains acrels cms anchors miscs format
    global typelist type list addel mat
    global h_menu_type h_menu_list h_menu_addel h_menu_material
    global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
    global fs
    global hdr1 hdr2
    global hw hw1
    global currstart currend
    global thisxl

    pkg load io
    %load xlsToMat.mat % data from xlsx file contained in varable c
    %load emptydb.mat %initialize empty database
    load mdcodes.mat
    hw={};
    hw1={};
    bgcolor='#e8e8e8';

    thisxl=getxlname();

    hdr1={'Buoyancy', 'Weight', 'Length', 'Width of', 'Diameter of', ...
    'Drag Coef', 'Material'};
    hdr2={'(kg)','(kg)','(cm)','CYL(cm)','SPH(cm)'};

    %xlswrite('example2.xlsx',hdr1, 'Sheet1', 'B1:G1');
    
    %for i = length(hdr1)
    xlswrite(thisxl,hdr1,'Sheet1','B1:G1');
    xlswrite(thisxl,hdr2,'Sheet1','B2:G2');

 
    
    loading=waitbar(1);
    %HARDWARE
    %element name
    currstart=3;
    currend=2+rows(chains);
    xlswrite(thisxl,'Hardware','Sheet1','A2');%manually write title of category


    %prints names of elements
    %
    for i = 1:rows(chains)%first convert to a cell array
        hw(i,1)=chains(i,format(1,1):format(1,2));
    endfor
    xlswrite(thisxl,hw,'Sheet1',[char(65) '3:' char(65) num2str(3+rows(chains))]);
    hw={};%clear the matrix 

    %element buoyancy
    for i = 1:rows(chains)
        [temp1]=strsplit(chains(i,format(2,1):format(2,2)));
        disp(temp1)
        hw(i,1) = str2num(temp1{1,2});
        hw1(i,1) = str2num(temp1{1,3});
    endfor
    xlswrite(thisxl,hw,'Sheet1',['B3:B18']);
    xlswrite(thisxl,hw1,'Sheet1',['C3:C18']);
    %hw={};
    %hw1={};



    close(loading);
    printf("Successfully written to: %s\n",thisxl);


    %xlswrite(thisxl,hw,'Sheet1', 'A3:A100');








    %--------------------------------
    format=[1,30;32,39;41,45;48,51;53,57;59,62;64,64];
endfunction

