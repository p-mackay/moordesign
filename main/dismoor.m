function dismoor(command)
    % function to display the present mooring elements in the command window

    global U V W z rho % U,V,W velocity profiles -- z height profile 
    global moorele H B ME X Y Z Ti iobj jobj psi  % for in-line and mooring elements
    global HCO BCO CdCO mooreleCO ZCO Iobj Jobj Pobj % for clamp-on devices
    global Z0co Zfco Xfco Yfco psifco
    global Zoo
    global Ht Bt Cdt MEt moorelet Usp Vsp % for a Towed Body
    global text_data
    global anc_info ele_data
    global ifile
    global testvar
    global thisele
    global thisele1 elesize
    global dpth hght



    %ct = strftime ("%e_%B_%Y", localtime (time ())); %current time
    %fileOut = ["Mooring_Elements" ct ".pdf"]; %pdf file produced 
    text_data = "";
    %velocity_data = getvelocity(40);
    %text_data = [nthargout(5,@moordyn)];
    %text_data = [text_data newline velocity_data newline];

    moorele=char(moorele); % reset these matrices as character strings
    mooreleCO=char(mooreleCO);
    moorelet=char(moorelet);

    if nargin==0,
        command=0;
    end
    line0='  0                                                                                                 ';
    if ~isempty(H) & isempty(Ht),
        [mm,nm]=size(moorele);
    else % this is a towed body case
        moorele=moorelet;
        H=Ht;B=Bt;ME=MEt;
        [mm,nm]=size(moorelet);
        psisave=psi;psi=pi-psi;psi(1)=0;
    end

    io=0;
    jo=0;
    [mz1,nz1]=size(Z);
    [mzo,nzo]=size(Zoo);
    if mz1==mzo, 
        dZ=Zoo-Z;
        dZco=Z0co-Zfco;
    elseif mz1==nzo,
        dZ=Zoo'-Z;
        dZco=Z0co'-Zfco;   
    end
    clear line
    if ~isempty(H) & isempty(Ht),
        hdr1=' # Mooring Element   Length[m] Buoy[kg] Height[m]    dZ[m]   dX[m]   dY[m]   Tension[kg]   Angle[deg]';
        %     1234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123
        text_data = [text_data newline hdr1];
        if isempty(Z),
            hdr2='                                         (top)                               Top  Bottom   Top Bottom';
            text_data = [text_data newline hdr2];
        else
            hdr2='                                        (middle)                             Top  Bottom   Top Bottom';
            text_data = [text_data newline hdr2];
        end
    else % then this is a towed body solution
        hdr1=' # Towed Element     Length[m] Buoy[kg]  Depth[m]    dZ[m]   dX[m]   dY[m]   Tension[kg]   Angle[deg]';
        %     1234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123
        text_data = [text_data newline hdr1];
        if isempty(Z),
            hdr2='                                        (bottom)                             Bottom  Top   Bottom Top';
            text_data = [text_data newline hdr2];
        else
            hdr2='                                        (middle)                             Bottom  Top   Bottom Top';
            text_data = [text_data newline hdr2];
        end
    end

    % first display the In-Line mooring components, then do the Clamp-on, then tally up all components
    %if command==1, % then print to printer
    %pf=figure(5);clf 
    %axis off
    %fs=8;
    %set(pf,'PaperOrient','Portrait','PaperUnits',...
    %'Normalized','PaperPosition',[0 0 1 1],'Visible','on');
    %dates=num2str(fix(clock),'%3.0f');dates(8)='/';dates([14 17])=':';
    %tit=['Mooring Design and Dynamics  ',dates];
    %ht=title(tit);
    %pos=get(ht,'Position');
    %set(ht,'Position',[pos(1) pos(2)*1.02 pos(3)],'Fontname','Courier New','FontSize',fs*1.2);
    %orient tall
    %ypos=1+3/90;
    %h=text(-0.1,ypos,'   In-Line');
    %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
    %ypos=1+2/90;
    %h=text(-0.1,ypos,hdr1);
    %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
    %ypos=1+1/90;
    %h=text(-0.1,ypos,hdr2);
    %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
    %else % display to the command window
    %	disp(' ');
    %	disp('   In-Line');
    %	disp(hdr1);
    %	disp(hdr2);
    %	refresh
    %end
    %
    ell=0;
    jo=0;io=0;
    for el=1:mm,
        ell=ell+1;
        line=line0;
        tmp=num2str(el);
        line(4-length(tmp):3)=tmp; %element number
        thisele = moorele(el,:);
        %sz = columns(strtrim(thisele)); 

        if (thisele(! isascii(thisele)))
            thisele(! isascii(thisele))=[];
            thisele=[thisele "   "];
            %line(sz)=[line "  "];
            %thisele1 = line(5:36);
            line(5:34)=thisele(1,:);
            %break;
        else
            line(5:34)=moorele(el,:); %element name
        endif
        thisele1 = line(5:34);
        %testvar = line(5:34);
        tmp=num2str(H(1,el),'%8.2f');
        if ~isempty(Z) && H(4,el) == 1, % a wire, consider some stretching
            jo=jo+1;
            if (jo+1)>length(jobj);
                tmp=num2str(H(1,el)*(1+2*(Ti(jobj(jo))+Ti(jobj(jo)+1))/(pi*H(2,el)^2*ME(el))),'%8.2f');
            else
                tmp=num2str(H(1,el)*(1+2*(Ti(jobj(jo))+Ti(jobj(jo+1)+1))/(pi*H(2,el)^2*ME(el))),'%8.2f');
            end      
        end
        line(31-length(tmp):30)=tmp;
        tmp=num2str(B(el),'%8.2f');
        line(40-length(tmp):39)=tmp;
        if isempty(Z),
            hght=sum(H(1,el:mm));  % Height at the top of this element
            %dpth=hght-z(1);
            printf("%d\n",dpth);
            tmp=num2str(hght,'%8.2f');
            line(50-length(tmp):49)=tmp;
            %printf("%d Hello World! tmp = %s length(tmp): %d\n",el,tmp, length(tmp));
        elseif ~isempty(Z) & H(4,el) ~=1 & el ~= mm, % this is an instrument/buoy...
            io=io+1;
            tmp=num2str(Z(iobj(io)),'%8.2f');
            line(50-length(tmp):49)=tmp;
            %%d printf("%d: Hello World! tmp = %s length(tmp): %d\n",el,tmp, length(tmp));
            tmp=num2str(dZ(iobj(io)),'%5.1f');
            line(59-length(tmp):58)=tmp;
            tmp=num2str(X(iobj(io)),'%5.1f');
            line(67-length(tmp):66)=tmp;
            tmp=num2str(Y(iobj(io)),'%5.1f');
            line(75-length(tmp):74)=tmp;
            tmp=num2str(Ti(iobj(io))/9.81,'%6.1f');
            line(82-length(tmp):81)=tmp;
            tmp=num2str(psi(iobj(io))*180/pi,'%4.1f');
            line(95-length(tmp):94)=tmp;
            tmp=num2str(Ti(iobj(io)+1)/9.81,'%6.1f');
            line(89-length(tmp):88)=tmp;
            tmp=num2str(psi(iobj(io)+1)*180/pi,'%4.1f');
            line(101-length(tmp):100)=tmp;
        elseif ~isempty(Z) & H(4,el) == 1, % this is a wire/rope/chain section
            tmp=num2str(Ti(jobj(jo))/9.81,'%6.1f');
            line(82-length(tmp):81)=tmp;
            %printf("%d: Hello World! tmp = %s length(tmp): %d\n",el,tmp, length(tmp));
            tmp=num2str(psi(jobj(jo))*180/pi,'%4.1f');
            line(95-length(tmp):94)=tmp;
            jo=jo+1;
            tmp=num2str(Ti(jobj(jo)+1)/9.81,'%6.1f');
            line(89-length(tmp):88)=tmp;
            tmp=num2str(psi(jobj(jo)+1)*180/pi,'%4.1f');
            line(101-length(tmp):100)=tmp;
        end
        if ~isempty(Z) && el == mm, % this is the anchor
            io=io+1;
            tmp=num2str(Z(iobj(io))/2,'%8.2f');
            line(50-length(tmp):49)=tmp;
            %printf("%d: Hello World! tmp = %s length(tmp): %d\n",el,tmp, length(tmp));
            tmp=num2str(dZ(iobj(io)),'%5.1f');
            line(59-length(tmp):58)=tmp;
            tmp=num2str(X(iobj(io)),'%5.1f');
            line(67-length(tmp):66)=tmp;
            tmp=num2str(Y(iobj(io)),'%5.1f');
            line(75-length(tmp):74)=tmp;
            tmp=num2str(Ti(end)/9.81,'%8.1f');
            line(85-length(tmp):84)=tmp;
            tmp=num2str(psi(end)*180/pi,'%4.1f');
            line(95-length(tmp):94)=tmp;
        end
        if command==1,
            %figure(5);
            %ypos=1-ell/90;
            %h=text(-0.1,ypos,line);
            %set(h,'Units','normalized','Position',[-0.075 ypos],'FontName','Courier New','FontSize',fs);
            %disp("%d: Hello 1")
            %disp(line);
            text_data = [text_data newline line];
        else
            %disp(line);
        end
        if command==1 && ell==80, % for printer output, go to next page
            ell=1;
            %figure(5);
            %orient tall;
            disp("1HELLLLLLLLO")
            %disp(mobj.height)

            tmpfname = tempname ();
            fid = fopen (tmpfname, "w+");
            fprintf (fid, "%s", text_data)
            fclose (fid)
            edit (tmpfname)

            %print -f5 -dpsc;
            %print -dpng
            %print -deps figure5.eps
            %print -f5 figure5.pdf
            %open figure5.pdf
            %print (5, fileOut);
            %print -f5 fileOut; 
            %saveas (5, fileOut);
            %open (fileOut); 

            %clf ();axis off
            %orient tall
            %ypos=1+3/90;
            %h=text(-0.1,ypos,'   In-Line');
            %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
            %ypos=1+2/90;
            %h=text(-0.1,ypos,hdr1);
            %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
            %ypos=1+1/90;
            %h=text(-0.1,ypos,hdr2);
            %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
        end
    end;

    % now display any Clamp-On devices
    if ~isempty(H) & isempty(Ht),
        hdr1=' #  Device Type    Attched to     m Up      Height[m]    dZ[m]   dX[m]   dY[m]   Angle[deg]';
        %     1234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123456
        hdr2='                   Element #  This Element  (middle)';
    else
        hdr1=' #  Device Type    Attched to     m Up      Depth [m]    dZ[m]   dX[m]   dY[m]   Angle[deg]';
        %     1234567891123456789212345678931234567894123456789512345678961234567897123456789812345678991234567890123456
        hdr2='                   Element #  This Element  (middle)';
    end

    mm=0;
    if ~isempty(BCO),mm=length(BCO);end
        if mm>0,
            ellz=ell+2;
            % first display the In-Line mooring components, then do the Clamp-on, then tally up all
            if command==1, % then print to printer
                %ypos=1-ellz/90;
                %h=text(-0.1,ypos,'   Clamp-On Devices');
                %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                %ellz=ellz+1;
                %ypos=1-ellz/90;
                %h=text(-0.1,ypos,hdr1);
                %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                %ellz=ellz+1;
                %ypos=1-ellz/90;
                %h=text(-0.1,ypos,hdr2);
                %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
            else % display to the command window
                disp(' ');
                disp('   Clamp-On Devices');
                disp(hdr1);
                disp(hdr2);
                refresh
            end
            %
            ell=ellz; %re-initialize the line number
            for elco=1:mm, % this loops through the clamp-on device list
                el=Jobj(elco); % the number of the mooring element this device is attached to
                io=0;jo=0;
                for ellh=1:el,
                    if H(4,ellh)~=1, io=io+1; end
                        if H(4,ellh)==1, jo=jo+1; end % identify the wire/rope segment
                        end
                        perc=Pobj(elco); % the percentage along this element.
                        ell=ell+1;
                        line=line0;
                        tmp=num2str(elco);
                        line(4-length(tmp):3)=tmp;
                        line(5:20)=mooreleCO(elco,:);
                        line(26-length(num2str(Jobj(elco))):25)=num2str(Jobj(elco));
                        %line(21:36)=moorele(Jobj(elco),:);
                        if ~isempty(Z) & H(4,el) == 1, % a wire, consider some stretching
                            %      tmp=num2str(perc*H(1,el)*(1+2*(Ti(jobj(jo+1))+Ti(jobj(jo+2)+1))/(pi*H(2,el)^2*ME(el))),'%8.2f');
                            tmp=num2str(perc*H(1,el)*(1+2*(Ti(jobj(jo))+Ti(jobj(jo+1)+1))/(pi*H(2,el)^2*ME(el))),'%8.2f');
                        else
                            tmp=num2str(perc*H(1,el),'%8.2f');
                        end
                        line(41-length(tmp):40)=tmp; % distance along this mooring element
                        if isempty(Z),
                            hght=ZCO(elco); % by definition, this is the "initial/desired" height
                            tmp=num2str(hght,'%8.2f');
                            line(54-length(tmp):53)=tmp;
                        else % then we've got a solution and the estimated position of this device
                            tmp=num2str(Zfco(elco),'%8.2f');
                            line(53-length(tmp):52)=tmp;
                            tmp=num2str(dZco(elco),'%6.2f');
                            line(63-length(tmp):62)=tmp;
                            tmp=num2str(Xfco(elco),'%5.1f');
                            line(71-length(tmp):70)=tmp;
                            tmp=num2str(Yfco(elco),'%5.1f');
                            line(79-length(tmp):78)=tmp;
                            tmp=num2str(psifco(elco)*180/pi,'%4.1f');
                            line(89-length(tmp):88)=tmp;
                        end
                        if command==1,
                            %figure(5);
                            %ypos=1-ell/90;
                            %h=text(-0.1,ypos,line);
                            %set(h,'Units','normalized','Position',[-0.075 ypos],'FontName','Courier New','FontSize',fs);
            disp("%d: Hello 2")
                            disp(line);
                            text_data = [text_data newline line];
                        else
                            disp(line);
                        end
                        if command==1 & ell==80, % for printer output, go to next page
                            ell=1;
                            %figure(5);
                            %orient tall;
                            %unis = get(gcf,'units');
                            %ppos = get(gcf,'paperposition');
                            %set(gcf,'units',get(gcf,'paperunits'));
                            %pos  = get(gcf,'position');
                            %pos(3:4) = ppos(3:4);
                            %set(gcf,'position',pos);
                            %set(gcf,'units',unis);

                            disp("2HELLLLLLLLO")
                            %disp(mobj.height)

                            tmpfname = tempname ();
                            fid = fopen (tmpfname, "w+");
                            %text_data = [text_data line];
                            fprintf (fid, "%s", text_data)
                            fclose (fid)
                            edit (tmpfname)

                            %saveas (5, fileOut);
                            %print -f5 -dpsc;
                            %print -f5 fileOut; 
                            %print (5, fileOut);
                            %saveas (5, fileOut);
                            %open (fileOut); 
                            %print -deps figure5.eps
                            %print -f5 figure5.pdf
                            %open figure5.pdf

                            %clf ();axis off
                            %orient tall
                            %ypos=1+3/90;
                            %h=text(-0.1,ypos,'   In-Line');
                            %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                            %ypos=1+2/90;
                            %h=text(-0.1,ypos,hdr1);
                            %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                            %ypos=1+1/90;
                            %h=text(-0.1,ypos,hdr2);
                            %set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                        end
                    end;
                end
                % now make a tally of all components
                [mm,nm]=size(moorele);  % start with the in-line components
                moortally=zeros(mm,2);
                mt=0;mtco=0;
                if mm>1,
                    icnt=1;
                    moortally(icnt,1:2)=[1 1];
                    for el=2:mm,
                        ifound=0;
                        for j=1:icnt,
                            if strcmp(moorele(moortally(j,1),:),moorele(el,:))==1, % then we found another
                                if H(4,el)~=1,
                                    moortally(j,2)=moortally(j,2)+1; % sum the # of these
                                else
                                    moortally(j,2)=moortally(j,2)+H(1,el); % sum wire/rope lengths
                                end
                                ifound=1;
                            end
                        end
                        if ifound==0, % this is the first of this type
                            icnt=icnt+1;  % number of active components in list
                            if H(4,el)~=1,
                                moortally(icnt,1:2)=[el 1];
                            else
                                moortally(icnt,1:2)=[el H(1,el)]; % sum wire/rope lengths
                            end
                        end
                    end
                    moortally=moortally(1:icnt,:);
                    % now tally clamp-on devices
                    mmco=length(BCO);
                    if mmco>0,
                        moortallyco=zeros(mmco,2);
                        icnt=1;
                        moortallyco(icnt,1:2)=[1 1];  % the first clamp-on device
                        if mmco>1,
                            for elco=2:mmco,
                                ifound=0;
                                for j=1:icnt,
                                    if strcmp(mooreleCO(moortallyco(j,1),:),mooreleCO(elco,:))==1, % strings match
                                        moortallyco(j,2)=moortallyco(j,2) + 1; % sum the # of these
                                        ifound=1;
                                    end
                                end
                                if ifound==0,  % then this is the first of this type
                                    icnt=icnt+1;
                                    moortallyco(icnt,1:2)=[elco 1];
                                end
                            end
                        end  
                        moortallyco=moortallyco(1:icnt,:);
                        [mtco,ntco]=size(moortallyco);   % mtco = number of different clamp-on devices
                    end
                    [mt,nt]=size(moortally);	% mt = number of different mooring components
                    if mtco<1, 
                        mtco=0;
                        hdr3=' Tally of all In-Line mooring/tow components by type.';
                        hdr4=' #    Element Name        Total Number/Length';
                        %     12345678911234567892123456789312345678941234567895123456789612345678712345678981234567899
                    else
                        hdr3=' Tally of all In-Line mooring/tow components by type       and       Clamp-on Devices.';
                        hdr4=' #    Element Name        Total Number/Length          #   Device Name       Total Number';
                    end

                    if command==1,
                        %	ypos=(mt+2)/90-.1;
                        %	h=text(-0.1,ypos,hdr3);
                        %	set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                        %	ypos=(mt+1)/90-.1;
                        %	h=text(-0.1,ypos,hdr4);
                        %	set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
                    else
                        disp(' ');
                        disp(hdr3);
                        disp(hdr4);
                    end
                    ii=0;
                    for i=1:mt,
                        %%printf("%d: Hello");
                        ii=ii+1; % count for clamp-on devices
                        line=line0;
                        line(1)=' ';
                        line(4-length(num2str(i)):3)=num2str(i);
                        line(6:35)=moorele(moortally(i,1),:);
                        line(31-length(num2str(moortally(i,2),6)):30)=num2str(moortally(i,2),6);
                        if ii <= mtco,
                            line(57-length(num2str(ii)):56)=num2str(ii);
                            line(60:75)=mooreleCO(moortallyco(ii,1),:);
                            line(87-length(num2str(moortallyco(ii,2))):86)=num2str(moortallyco(ii,2));
                        end
                        if H(4,moortally(i,1))==1, line(32)='m'; end
                            if command==1,
                                %figure(5);
                                %ypos=(mt-i)/90-.1;
                                %h=text(-0.1,ypos,line);
                                %set(h,'Units','normalized','Position',[-0.075 ypos],'FontName','Courier New','FontSize',fs);
                            else
                                disp(line);
                            end
                        end
                        if mtco > mt, % then there are more clamp-on devices than mooring elements
                            iii=ii;
                            for ii=iii+1:length(BCO),
                                line=line0;
                                line(1)=' ';
                                line(57-length(num2str(ii)):56)=num2str(ii);
                                line(60:75)=mooreleCO(moortallyco(ii,1),:);
                                line(87-length(num2str(moortallyco(ii,2))):86)=num2str(moortally(ii,2));
                                if command==1,
                                    %figure(5);
                                    %ypos=(mt-i)/90-.1;
                                    %h=text(-0.1,ypos,line);
                                    %set(h,'Units','normalized','Position',[-0.075 ypos],'FontName','Courier New','FontSize',fs);
                                    text_data = [text_data newline line];
            disp("%d: Hello 3")
                                else
                                    disp(line);
                                end
                            end
                        end
                    end
                    %
                    if command==1,
                        %figure(5);
                        %orient tall;
                        % wysiwyg
                        %unis = get(gcf,'units');
                        %ppos = get(gcf,'paperposition');
                        %set(gcf,'units',get(gcf,'paperunits'));
                        %pos  = get(gcf,'position');
                        %pos(3:4) = ppos(3:4);
                        %set(gcf,'position',pos);
                        %set(gcf,'units',unis);
                        hdr5=' Tally of all In-Line mooring/tow components by type.';
                        hdr6=' #    Element Name        Total Number/Length';

                        ele_data = ""; %tally of mooring elements
                        vel_data = ""; %velocity data

                        hdr4 = 'Height[m]    U [m/s]    V [m/s]    W [m/s] Density [kg/m^3]'
                        vel_data = [vel_data hdr4]
                        for i=1:length(z),
                            if z(i)>999.99,
                                vel_data = [vel_data newline [' ',num2str([z(i) U(i) V(i) W(i) rho(i)],'%11.2f')]];
                            elseif z(i)<1000 & z(i)>99.99,
                                vel_data = [vel_data newline ['  ',num2str([z(i) U(i) V(i) W(i) rho(i)],'%11.2f')]];
                            elseif z(i)<100 & z(i)>9.99,
                                vel_data = [vel_data newline ['   ',num2str([z(i) U(i) V(i) W(i) rho(i)],'%11.2f')]];
                            elseif z(i)<10,
                                vel_data = [vel_data newline ['    ',num2str([z(i) U(i) V(i) W(i) rho(i)],'%11.2f')]];
                            endif
                        endfor
                        %[mm,nm]=size(moorele);  % start with the in-line components
                        %moortally=zeros(mm,2);
                        %mt=0;mtco=0;

                        ele_data=[ele_data hdr5 newline hdr6 newline];
                        ii=0;
                        for i=1:mt,
                            %%printf("%d: Hello");
                            ii=ii+1; % count for clamp-on devices
                            line=line0;
                            line(1)=' ';
                            line(4-length(num2str(i)):3)=num2str(i);
                            line(6:35)=moorele(moortally(i,1),:);
                            line(31-length(num2str(moortally(i,2),6)):30)=num2str(moortally(i,2),6);
                            %line1 = line(4-length(num2str(i)):3);
                            if (i < 10)
                                line1 = [" " num2str(i)];
                            else
                                line1 = num2str(i);
                            endif
                            %line2(! isascii(line2)) = [];
                            this2 = moorele(moortally(i,1),:); 
                            if (this2(! isascii(this2)))
                                line2 = [moorele(moortally(i,1),:) "  "];
                            else
                                line2 = moorele(moortally(i,1),:); 
                            endif
                            line3 = line(31-length(num2str(moortally(i,2),6)):30);
                            %printf("%s %s %s\n",line1,line2,line3);
                            %disp(size(line))
                            %ele_data = [ele_data line(1) num2str(i) " " line2 newline];
                            %ele_data = [line(4-length(num2str(i)):3) " " line(6:35) newline];


                            if ii <= mtco,
                                line(57-length(num2str(ii)):56)=num2str(ii);
                                line(60:75)=mooreleCO(moortallyco(ii,1),:);
                                line(87-length(num2str(moortallyco(ii,2))):86)=num2str(moortallyco(ii,2));
                            endif
                        endfor


                        %ct = strftime ("%e_%B_%Y", localtime (time ())); %current time
                        ct = strftime ("%Y-%m-%d", localtime (time ())); %current time

                        tmpfname = tempname ();
                        fid = fopen (tmpfname, "w+");
                        %--------------------------
                        %start writing to temp file

                        %text_data = [text_data line];
                        %if (!isempty(ifile))
                        %    fprintf (fid, " %s      ", ifile)
                        %endif
                        this2 = moorele(moortally(i,1),:); 
                        if (this2(! isascii(this2)))
                            line2 = [moorele(moortally(i,1),:) "  "];
                        else
                            line2 = moorele(moortally(i,1),:); 
                        endif

                        fprintf (fid, "Date: %s     ", ct)
                        fprintf (fid, "Mooring File Name: %s     ", ifile)
                        fprintf (fid, "Mooring Name: %s", ifile)
                        fprintf (fid, "%s", newline)
                        fprintf (fid, "%s", text_data)
                        fprintf (fid, "%s", newline)
                        fprintf (fid, "%s", newline)
                        fprintf (fid, "%s", vel_data)
                        fprintf (fid, "%s", newline)
                        fprintf (fid, "%s", newline)
                        fprintf (fid, "%s", anc_info)
                        fclose (fid)
                        edit (tmpfname)




                        %end writing to temp file
                        %------------------------

                        %saveas (5, fileOut);
                            %print -f5 -dpsc;
                        %print -deps figure5.eps
                        %print -f5 figure5.pdf
                        %open figure5.pdf

                        %set(pf,'Visible','off');
                        %print -f5 fileOut; 
                        %print (5, fileOut);
                        %saveas (5, fileOut);
                        %open (fileOut); 
                        %print -dps MDDout.ps   % if you want a postscript file
                        %close(5);
                        clear text_data
                        clear vel_data
                        clear anc_info
                    else
                        disp(' ');
                        clear text_data
                        clear vel_data
                        clear anc_info
                    end
                    if ~isempty(Ht), moorele=[]; H=[]; B=[]; ME=[]; psi=psisave; end
                        drawnow
                        % fini
                        clear text_data
                        clear vel_data
                        clear anc_info
