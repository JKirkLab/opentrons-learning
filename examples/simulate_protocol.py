from opentrons.simulate import simulate, format_runlog

protocol_file = open("./Protocols/test_tilting_reservoir.py")

runlog, _bundle = simulate(protocol_file,
                           custom_labware_paths=["../RobotProtocols"] )

print(format_runlog(runlog)) 