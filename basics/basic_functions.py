from opentrons import protocol_api

metadata = {
    'protocolName': 'Basic Pipetting Tutorial',
    'author': '<mqiao@luc.edu>',
    'description': 'A simple tutorial demonstrating basic pipetting actions',
    'apiLevel': '2.21'  
}

def run(protocol: protocol_api.ProtocolContext):


    plate = protocol.load_labware('corning_96_wellplate_360ul_flat', '1')  # deck slot 1
    tiprack = protocol.load_labware('opentrons_96_tiprack_300ul', '2')     # deck slot 2

    pipette = protocol.load_instrument('p300_single', mount='right', tip_racks=[tiprack])

    #Pick up tip
    
    pipette.pick_up_tip()

    # Aspirate 100 µL from A1
    pipette.aspirate(100, plate.wells_by_name()['A1'])

    # Dispense into B1
    pipette.dispense(100, plate.wells_by_name()['B1'])

    # Mix 3 times in B1 (aspirate and dispense)
    pipette.mix(3, 50, plate.wells_by_name()['B1'])

    # Drop tip
    pipette.drop_tip()

