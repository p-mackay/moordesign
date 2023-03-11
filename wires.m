addelement.m:global floats wires chains acrels cms anchors miscs format
addelement.m:      list=wires;
addelement.m:                [m,n]=size(wires);
addelement.m:                    if sum(strcmp(text,wires(ii,1:17))) ~= 0,
addelement.m:                    wires(m+1,:)=newele;
addelement.m:                    wires
addelement.m:            [m,n]=size(wires);
addelement.m:            disp(['!! I am deleting: ',wires(val,:)]);
addelement.m:            wires=wires(id,:);
addelement.m:      save([opath ofile],'acrels','cms','format','miscs','anchors','chains','floats','wires');
addelement.m:                [m,n]=size(wires);
addelement.m:                   if sum(strcmp(text,wires(ii,1:17))) ~= 0,
addelement.m:                   wires(imod,:)=newele;
addelement.m:                   wires
globalchange.m:global floats wires chains acrels cms anchors miscs format 
globalchange.m:      list2=wires;
modmoor.m:global floats wires chains acrels cms anchors miscs format typelist type list
modmoor.m:      list=wires;
modmoorco.m:global floats wires chains acrels cms anchors miscs format typelist type list 
modtow.m:global floats wires chains acrels cms anchors miscs format typelist type list
modtow.m:      list=wires;
modtowco.m:global floats wires chains acrels cms anchors miscs format typelist type list 
plot_elements.m:      [ne,le]=size(wires);
plot_elements.m:         if strcmp(line(1:16),wires(ie,1:16)),  % check wires/ropes
towdyn.m:   z(indxz+1)=1.2*maxz; % deepen water depth to account for long tow wires
