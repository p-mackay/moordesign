classdef Mooring

properties
height
Udis
Vdis
Wdis
rhodis
endproperties

	methods
function thisMooring = Mooring(height, Udis, Vdis, Wdis, rhodis)
	thisMooring.height = height;
	thisMooring.Udis = Udis;
	thisMooring.Vdis = Vdis;
	thisMooring.Wdis = Wdis;
	thisMooring.rhodis = rhodis;
	endfunction
	endmethods
	endclassdef



