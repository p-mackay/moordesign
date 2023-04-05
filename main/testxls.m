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
    global currstart currend
    global thisxl


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
    
    thisxl = 'example5.xlsx';
    hdr1={'Buoyancy', 'Length', 'Width of', 'Diameter of', ...
            'Drag Coef', 'Material'};
    hdr2={'(kg)','(cm)','CYL(cm)','SPH(cm)'};

    %xlswrite('example2.xlsx',hdr1, 'Sheet1', 'B1:G1');
    
    %for i = length(hdr1)
    xlswrite(thisxl,hdr1,'Sheet1','B1:G1');
    xlswrite(thisxl,hdr2,'Sheet1','B2:G2');

 
    
    %HARDWARE
    %element name
    currstart=3;
    currend=2+rows(chains);
    %xlswrite(thisxl,'Hardware','Sheet1','A2');%manually write title of category
    %for i = 1:rows(chains)
    %    hw(i,1)=chains(i,format(1,1):format(1,2));
    %endfor
    %xlswrite(thisxl,hw,'Sheet1',['A3:A' num2str(3+rows(chains))]);
    %hw={};

    %for j = 2:7
    %    hw={};%clear the matrix 
    %    for i = 1:rows(chains)%first convert to a cell array
    %        hw(i,1)=str2num(chains(i,format(j,1):format(j,2)));
    %    endfor
    %    xlswrite(thisxl,hw,'Sheet1',[char(65+j-1) num2str(currstart) ':' char(65+j-1) num2str(currend)]);
    %endfor
    %printf("%d  %d\n",currstart, currend);
    %hw={};

    xlswrite(thisxl,'Flotation','Sheet1','A2');%manually write title of category
    for i = 1:rows(floats)
        if(hw{i,1}(! isascii(hw{i,1})))
            printf("%s\n", hw(i,1));
            break;
            hw{i,1}(!isasccii(hw{i,1}))=[];
            hw(i,1)=floats(i,format(1,1):format(1,2));
            printf("%s\n", hw(i,1));
        else
            hw(i,1)=floats(i,format(1,1):format(1,2));
            printf("%s\n", hw(i,1));
        endif
    endfor
    %xlswrite(thisxl,hw(1,1),'Sheet1',['A3']);
    %xlswrite(thisxl,hw(7,1),'Sheet1',['A4']);
    %xlswrite(thisxl,hw,'Sheet1',['A3:A' num2str(3+rows(floats))]);
    %hw={};

    %for j = 2:7
    %    hw={};%clear the matrix 
    %    for i = 1:rows(floats)%first convert to a cell array
    %        hw(i,1)=str2num(floats(i,format(j,1):format(j,2)));
    %    endfor
    %    xlswrite(thisxl,hw,'Sheet1',[char(65+j-1) num2str(currstart) ':' char(65+j-1) num2str(currend)]);
    %endfor
    %printf("%d  %d\n",currstart, currend);
    %hw={};



    %FLOATATION
    %currstart=currstart+currend+1;
    %currend=currstart+rows(floats);
    %printf("%d  %d\n",currstart, currend);
    %%xlswrite(thisxl,'Hardware','Sheet1','A2');%manually write title of category
    %for i = 1:rows(floats)
    %    hw(i,1)=floats(i,format(1,1):format(1,2));
    %endfor
    %printf("A%s:A%s\n",num2str(currstart),num2str(currend));
    %xlswrite(thisxl,hw,'Sheet1',['A21:A34']);
    %xlswrite(thisxl,hw,'Sheet1',['A' num2str(currstart) ':A' num2str(currend)]);
    %hw={};

    %for j = 2:7
    %    hw={};%clear the matrix 
    %    for i = 1:rows(floats)%first convert to a cell array
    %        hw(i,1)=str2num(floats(i,format(j,1):format(j,2)));
    %    endfor
    %    %xlswrite(thisxl,hw,'Sheet1',[char(65+j-1) num2str(currstart) ':' char(65+j-1) num2str(currend)]);
    %    xlswrite(thisxl,hw,'Sheet1',[char(65+j-1) num2str(23) ':' char(65+j-1) num2str(100)]);
    %endfor
    %hw={};



    %currstart = currstart+currend;
    %currend = currstart+rows(floats);
    %for j = 1:7
    %    for i = 1:rows(floats)%first convert to a cell array
    %        hw(i,1)=floats(i,format(j,1):format(1,2));
    %    endfor
    %    xlswrite('example3.xlsx',hw,'Sheet1',[char(65+j-1) num2str(currstart) ':' char(65+j-1) num2str(currend)]);
    %    hw={};%clear the matrix 
    %endfor






    %%element buoyancy
    %for i = 1:rows(chains)
    %    hw(i,1)=str2num(chains(i,format(2,1):format(2,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['B3:B' num2str(3+rows(chains))]);
    %hw={};

    %%element length
    %for i = 1:rows(chains)
    %    hw(i,1)=str2num(chains(i,format(3,1):format(3,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['C3:C' num2str(3+rows(chains))]);
    %hw={};
    %
    %%element width
    %for i = 1:rows(chains)
    %    hw(i,1)=str2num(chains(i,format(4,1):format(4,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['D3:D' num2str(3+rows(chains))]);
    %hw={};

    %%element diameter
    %for i = 1:rows(chains)
    %    hw(i,1)=str2num(chains(i,format(5,1):format(5,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['E3:E' num2str(3+rows(chains))]);
    %hw={};

    %%element drag coef 
    %for i = 1:rows(chains)
    %    hw(i,1)=str2num(chains(i,format(6,1):format(6,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['F3:F' num2str(3+rows(chains))]);
    %hw={};

    %%element drag coef 
    %for i = 1:rows(chains)
    %    hw(i,1)=str2num(chains(i,format(7,1):format(7,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['G3:G' num2str(3+rows(chains))]);
    %hw={};
    %currstart=3+rows(chains);


    %%FLOATATION
    %%element name
    %for i = 1:rows(floats)%first convert to a cell array
    %    hw(i,1)=floats(i,format(1,1):format(1,2));
    %endfor
    %xlswrite('example3.xlsx','Hardware','Sheet1',['A' num2str(3+currstart)]);%manually write title of category
    %xlswrite('example3.xlsx',hw,'Sheet1',['A' num2str(4+currstart) ':A' num2str(3+rows(floats))]);
    %hw={};%clear the matrix 

    %%element buoyancy
    %for i = 1:rows(floats)
    %    hw(i,1)=str2num(floats(i,format(2,1):format(2,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['B3:B' num2str(3+rows(floats))]);
    %hw={};

    %%element length
    %for i = 1:rows(floats)
    %    hw(i,1)=str2num(floats(i,format(3,1):format(3,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['C3:C' num2str(3+rows(floats))]);
    %hw={};
    %
    %%element width
    %for i = 1:rows(floats)
    %    hw(i,1)=str2num(floats(i,format(4,1):format(4,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['D3:D' num2str(3+rows(floats))]);
    %hw={};

    %%element diameter
    %for i = 1:rows(floats)
    %    hw(i,1)=str2num(floats(i,format(5,1):format(5,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['E3:E' num2str(3+rows(floats))]);
    %hw={};

    %%element drag coef 
    %for i = 1:rows(floats)
    %    hw(i,1)=str2num(floats(i,format(6,1):format(6,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['F3:F' num2str(3+rows(floats))]);
    %hw={};

    %%element drag coef 
    %for i = 1:rows(floats)
    %    hw(i,1)=str2num(floats(i,format(6,1):format(6,2)));
    %endfor
    %xlswrite('example3.xlsx',hw,'Sheet1',['F3:F' num2str(3+rows(floats))]);
    %hw={};




    %xlswrite('example3.xlsx',hw,'Sheet1', 'A3:A100');







    %--------------------------------
    %format=[1,30;32,39;41,45;48,51;53,57;59,62;64,64]
endfunction

