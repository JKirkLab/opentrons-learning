# FAQ
This is a compilation of certain interesting tidbits we've noticed while working with the robot. 

### Q: Why does the Robot make a weird sound when the gantry moves in any diagonal direction? 

A: We don’t know for sure, but it doesn’t seem to have an effect on the performance of the robot. 

### Q: Why does the robot use multiple pipettes for inserting samples in replicate for many protocols, instead of aspirating the total amount and distributing that amount across the replicates? 

A: It is possible to distribute the volume by aspirating the total amount, but we’re not sure if there may be some unintended interactions between replicate wells when inserting the same pipette into different wells with liquid already inside the well. Further testing is probably necessary to ensure that it works just as well as using one tip for each replicate.  

### Q: Why does there seem to be a small amount of liquid left in the pipette after dispensing? 

A: This was something we noticed during testing; however, given the results of the assays (generally judged by how good the standard curve looks and how far apart each replicate is), we decided that it was negligible. There are certain ways to prevent this from happening, such as by aspirating slightly more than the intended volume and dispensing the intended volume. 

### Q: Why does there seem to be liquid on the outside of the pipette? Is there any way to fix this? 

A: Certain liquids in protocols seem to behave slightly differently (especially the reagents in qPCR). These liquids tend to collect on the outside of the pipette tip during aspiration; however, it does not seem to negatively affect the performance of the robot. 

### Q: Why is the user required to perform certain steps, such as inserting the working reagent? 

A: The user is required to perform certain steps due to inherent limitations in the labware. Inserting working reagent is often left to the user because the level of liquid in the well to be aspirated from would be too low, leading to inconsistent results. We’re currently looking for ways to get around this issue with custom labware. 

### Q: My robot collided with something! What do I do now? 

A: Press the big red button so that the protocol stops. Then twist the red button clockwise. This should prompt the user to either save the liquid within the pipette or then drop the tip. If the liquid inside the pipette tip is important then follow the instructions on the screen, otherwise instruct the robot to drop the tip.  

### Q: Why is the heater shaker module included in some protocols where it’s not used? 

A: It was originally included in protocols due to concerns about any collisions that might occur if the robot didn’t recognize that it was in the deck.  

### Q: Why do some protocols have repeated labware appear in the same slots during set up? 

A: Due to the way lids are implemented, labware has to be managed by an external class which deletes and reloads labware as necessary. When the robot analyzes the code, it will see that the same piece of labware will have been deleted and reloaded multiple times to account for the lid being placed on top of it. Therefore, it will show the same labware multiple during setup.  