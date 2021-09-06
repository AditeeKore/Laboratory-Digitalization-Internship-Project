from import_export import resources
from .models import AllLabinfo, Lab7A, Lab7A_SW_Inst, Lab7B, Lab7B_SW_Inst, Lab7C, Lab7C_SW_Inst, Lab7D, Lab7D_SW_Inst,  Lab7E, Lab7E_SW_Inst, tt_file

class uploadresource(resources.ModelResource):
    class meta:
        model = AllLabinfo
        model = Lab7A
        model = Lab7B
        model = Lab7C
        model = Lab7D
        model = Lab7E
        model = Lab7A_SW_Inst
        model = Lab7B_SW_Inst
        model = Lab7C_SW_Inst
        model = Lab7D_SW_Inst
        model = Lab7E_SW_Inst
        # model = tt_file