
ell=0;io=0;
for el=1:mm,
    ell=ell+1;
line=line0;
tmp=num2str(el);
line(4-length(tmp):3)=tmp;
line(5:20)=moorele(el,:);
tmp=num2str(H(1,el),'%8.2f');
if ~isempty(Z) & H(4,el) == 1, % a wire, consider some stretching
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
   tmp=num2str(hght,'%8.2f');
   line(50-length(tmp):49)=tmp;
   elseif ~isempty(Z) & H(4,el) ~=1 & el ~= mm, % this is an instrument/buoy...
   io=io+1;
   tmp=num2str(Z(iobj(io)),'%8.2f');
   line(50-length(tmp):49)=tmp;
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
   tmp=num2str(psi(jobj(jo))*180/pi,'%4.1f');
   line(95-length(tmp):94)=tmp;
   jo=jo+1;
   tmp=num2str(Ti(jobj(jo)+1)/9.81,'%6.1f');
   line(89-length(tmp):88)=tmp;
   tmp=num2str(psi(jobj(jo)+1)*180/pi,'%4.1f');
   line(101-length(tmp):100)=tmp;
   end
   if ~isempty(Z) & el == mm, % this is the anchor
   io=io+1;
   tmp=num2str(Z(iobj(io))/2,'%8.2f');
   line(50-length(tmp):49)=tmp;
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
   figure(5);
ypos=1-ell/90;
h=text(-0.1,ypos,line);
set(h,'Units','normalized','Position',[-0.075 ypos],'FontName','Courier New','FontSize',fs);
else
disp(line);
end
if command==1 & ell==80, % for printer output, go to next page
ell=1;
figure(5);
orient tall;
unis = get(gcf,'units');
ppos = get(gcf,'paperposition');
set(gcf,'units',get(gcf,'paperunits'));
pos  = get(gcf,'position');
pos(3:4) = ppos(3:4);
set(gcf,'position',pos);
set(gcf,'units',unis);
print -f5 -v;
clf;axis off
orient tall
ypos=1+3/90;
h=text(-0.1,ypos,'   In-Line');
set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
ypos=1+2/90;
h=text(-0.1,ypos,hdr1);
set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
ypos=1+1/90;
h=text(-0.1,ypos,hdr2);
set(h,'Units','Normalized','Position',[-0.075 ypos],'Fontname','Courier New','FontSize',fs);
end
end;
