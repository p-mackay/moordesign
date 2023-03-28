global moorele
global moorele H B ME X Y Z Ti iobj jobj psi  % for in-line and mooring elements
global HCO BCO CdCO mooreleCO ZCO Iobj Jobj Pobj % for clamp-on devices
global Z0co Zfco Xfco Yfco psifco
global Zoo
global Ht Bt Cdt MEt moorelet Usp Vsp % for a Towed Body
global Z

dZ=Zoo-Z;
jo=0;
io=0;
line0 = '0'
mm=size(moorele);
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
end;
