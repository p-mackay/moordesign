function test_addelement;
	% Program to make a GUI for modifying a mooring element in the database

	global U V W z rho
	global H B Cd ME moorele
	global chains wires chains acrels cms anchors miscs format
	global typelist type list addel mat
	global h_menu_type h_menu_list h_menu_addel h_menu_material
	global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
	global fs


	load updated_Hardware
	load testdb2 %initialize empty database

    [m,n]=size(floats);

    name = c{i,1};
    buoy = c{i,2};
    dim = [c{i,3} c{i,4} c{i, 5}];
    cd = c{i,6};
    mat = c{i,7};


    for i = 3:10


        [m,n]=size(chains);

        name = c{i,1};
        buoy = c{i,2};
        dim = [c{i,3} c{i,4} c{i, 5}];
        cd = c{i,6};
        mat = c{i,7};

        buoy=num2str(buoy,'%8.3f');
        dim1=num2str(dim(1),'%5.1f');

        text='*                              ';
        text(1:length(name))=name;

        tbuoy='        ';
        tbuoy((9-length(buoy)):8)=buoy;  % must pad front with blanks  


        tdim='                  ';
        dim1=num2str(dim(1),'%5.1f');


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
        disp(newele)

        chains(m+1,:)=newele;
        chains
    endfor

    [ofile,opath]=uiputfile('testdb.mat','Save A New MDCODES.MAT');
    save ([opath ofile],'acrels','cms','format','miscs','anchors','chains','floats','wires');

