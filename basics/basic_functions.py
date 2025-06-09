from opentrons import protocol_api

metadata = {
    'protocolName': 'Basic Pipetting Tutorial',
    'author': '<mqiao@luc.edu>',
    'description': 'A simple tutorial demonstrating basic pipetting actions',
    'apiLevel': '2.21'  
}

def run(protocol: protocol_api.ProtocolContext):


    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', location = "C2")  
    tiprack = protocol.load_labware('opentrons_flex_96_tiprack_200ul', location = "C3")     

    left_pipette = protocol.load_instrument('flex_8_channel_50', mount='left')
    right_pipette = protocol.load_instrument('flex_8_channel_1000', mount='right')

    right_pipette.configure_nozzle_layout(style='single', start='H1')

    #Pick up tip
    
    right_pipette.pick_up_tip()

    # Aspirate 100 µL from A1
    right_pipette.aspirate(100, plate.wells_by_name()['A1'])

    # Dispense into B1
    right_pipette.dispense(100, plate.wells_by_name()['B1'])

    # Mix 3 times in B1 (aspirate and dispense)
    right_pipette.mix(3, 50, plate.wells_by_name()['B1'])

    # Drop tip
    right_pipette.drop_tip()

