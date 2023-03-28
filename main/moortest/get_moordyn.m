classdef get_moordyn
    properties
        Wa      %Total Tension on Anchor [kg]                 
        VWa     %Vertical load [kg]                           
        HWa     %Horizontal load [kg]                         
        TWa     %Safe wet anchor mass [kg]                    
                %* 2.2 [lb]                                  
                %Safe dry steel anchor mass = TWa/0.87       
                %Safe dry concrete anchor mass = TWa/0.65    

        WoB     %Weight under anchor
    endproperties

    methods
        function obj = mooring(Wa,VWa,HWa,TWa,WoB)
        %class constructor
            obj.Wa = Wa;
            obj.VWa = VWa;
            obj.HWa = HWa;
            obj.TWa = TWa;
            obj.WoB = WoB;
        endfunction

    endmethods
endclassdef



