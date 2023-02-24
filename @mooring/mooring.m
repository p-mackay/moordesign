classdef mooring

    properties
        float;
        wire;
        chain;
        shackle;
        cur_mtr;
        acou_rel;
    endproperties

    methods
        function obj = mooring(float, wire, chain, shackle, cur_mtr, acou_rel)
        %class constructor
            obj.float = float;
            obj.wire = wire;
            obj.chain = chain;
            obj.shackle = shackle;
            obj.cur_mtr = cur_mtr;
            obj.acou_rel = acou_rel;
        endfunction
        
        function float = get.float(obj)
            float = obj.float;
        endfunction




    endmethods
endclassdef



