"""
Created on Wed Mar 12
@author: mqiao
"""

from opentrons import protocol_api
from opentrons.protocol_api import SINGLE

# metadata
metadata = {
    "protocolName": "Aliquot Samples",
    "author": "<mqiao@luc.edu>",
    "description": "Aliquots samples for a specified volume",
}

requirements = {"robotType": "Flex", "apiLevel": "2.21"} 

def add_parameters(parameters):   

    tip_alpha_ = ["A", "B", "C", "D", "E", "F","G","H"]
    tip_alpha = lambda: [{"display_name": str(i), "value": i } for i in tip_alpha_]

    tip_num_ = ["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10","a11","a12"]
    tip_num = lambda: [{"display_name": str(i[1:]), "value": str(i) } for i in tip_num_]

    parameters.add_str(variable_name="tip_alpha_val_50", 
    display_name="Starting Tip Row Name_50",
    description="Row name of starting tip", 
    default="A",
    choices=tip_alpha())

    parameters.add_str(variable_name="tip_num_val_50",
    display_name="Starting Tip Column Number_50",
    description="Column of starting tip",
    default="a1",
    choices=tip_num())

    parameters.add_int(variable_name="num_aliquots", 
    display_name="Number of aliquots",
    description="Number of aliquots to be made", 
    default=1,
    minimum=1,
    maximum=23)

    parameters.add_int(variable_name = "aliquot_vol",
    display_name = "Aliquot Volume in uL",
    description="Volume of each aliquot",
    default = 20,
    minimum = 5,
    maximum = 40)
    
def init_labware(protocol):
    """Loads all labware and returns a dictionary of labware objects."""
    labware = {
        "partial_rack_50": protocol.load_labware("opentrons_flex_96_tiprack_50ul", location="B1"),
        "eppendorf_rack": protocol.load_labware("opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap", location="B2"),
        "trash": protocol.load_trash_bin("A3"),
    }
    return labware

def init_pipettes(protocol):
    """Loads pipettes and returns them as a tuple."""
    right_pipette = protocol.load_instrument("flex_8channel_1000", mount="right")
    right_pipette.configure_nozzle_layout(style=SINGLE, start="H1")

    left_pipette = protocol.load_instrument("flex_8channel_50", mount="left")
    left_pipette.configure_nozzle_layout(style=SINGLE, start="H1")

    return left_pipette, right_pipette
    
def run(protocol: protocol_api.ProtocolContext): 

    labware = init_labware(protocol)
    left_pipette, right_pipette = init_pipettes(protocol)

    num_aliquots = protocol.params.num_aliquots
    aliquot_vol = protocol.params.aliquot_vol

    start_tip_alpha_num_50 = protocol.params.tip_alpha_val_50 + protocol.params.tip_num_val_50[1:]
    pipette_slot_list = [f"{letter}{num}" for letter in "ABCDEFGH" for num in range(1, 13)] 

    curr_tip_50 = pipette_slot_list.index(start_tip_alpha_num_50)
    eppendorf_rack_coord = [f"{letter}{number}" for letter in 'ABCD' for number in range (1,7)]  
    eppendorf_rack_coord.pop(0)

    left_pipette.pick_up_tip(location = labware['partial_rack_50'][pipette_slot_list[curr_tip_50]])
    curr_tip_50 += 1 
    for i in range(num_aliquots):
        left_pipette.aspirate(aliquot_vol, labware['eppendorf_rack']['A1'])
        left_pipette.dispense(aliquot_vol, labware['eppendorf_rack'][eppendorf_rack_coord[i]])
        
    left_pipette.drop_tip()


