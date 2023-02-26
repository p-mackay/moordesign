classdef mooring

    properties
        U
        v_load
    endproperties

    methods
        function obj = mooring(U)
        %class constructor
            obj.U = U;
        endfunction

        function obj = mooring(v_load)
        %class constructor
            obj.v_load = v_load;
        endfunction

    endmethods
endclassdef



