function test_addelement;
	% Program to make a GUI for modifying a mooring element in the database

	global U V W z rho
	global H B Cd ME moorele
	global chains wires chains acrels cms anchors miscs format
	global typelist type list addel mat
	global h_menu_type h_menu_list h_menu_addel h_menu_material
	global h_push_add h_edit_elename h_edit_elebuoy h_edit_eledim h_edit_elecd
	global fs


	load mooring_hardware
	load mdcodes2

	%
	%   h_menu_addel=uicontrol('Style','popupmenu',...
	%      'Callback','test_addelement(2)','FontSize',fs,...
	%      'String','Examine|Add Element|Delete Element|Modify Element',...
	%      'Units','Normalized',...
	%      'Position',[.3 .695 .4 .1]);
	%
	%   elseif addel == 2,
	%    h_push_add=uicontrol('Style','Pushbutton',...
	%      'String','Add','FontSize',fs,...
	%      'Units','normalized',...
	%      'Position',[.05 .1 .2 .08],...
	%      'Callback','test_addelement(4)');
	%end
	%


	[m,n]=size(chains);




	name = c{4,1};
	buoy = c{4,2};
	dim = str2num("4 0 0");
	cd = str2num("1.65");
	mat = 1;

	buoy=num2str(buoy,'%8.3f');
	dim1=num2str(dim(1),'%5.1f');


	tbuoy='        ';
	tbuoy((9-length(buoy)):8)=buoy;  % must pad front with blanks  

	text='*                ';
	text(1:length(name))=name;

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
	disp("FLOATS(M)"), disp(chains(m-1))

	chains(m+1,:)=newele;
	chains

