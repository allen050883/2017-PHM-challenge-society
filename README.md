# 2017-PHM-challenge-society  
  
### System Description  
***This year’s challenge continues the trend started in the previous years and is focused on the combination of physics-based modeling and statistical approaches for prediction. It is recommended that the solution you design and implement use physics-based modeling elements. Points will be given to those approaches that provide a physical connection to the data such as health states of various components, relationship between data and model parameters or states, etc.The system under investigation is a conventional bogie vehicle. Figure 1 depicts a schematic diagram of a bogie vehicle model, consisting of a vehicle body, two bogies and four wheelsets. The simplified model includes coil springs and dampers used in the primary suspension, and air springs in the secondary suspension. Sensors are placed on the wheelsets, on the bogie frames and on the car body as shown in the figure. Random track irregularities, roughness and faults will induce vibrations along each axis.The vehicle is operated on tracks with different irregularities, layouts, contact geometries and speeds. Additionally the vehicle parameters like loading, stiffness and damping rates vary in some range even in experiments without faults in the components.***  
![alt](https://www.phmsociety.org/sites/phmsociety.org/files/PHM17DCFig1.png)  
*Figure 1. Diagram of a simplified vehicle model (See [1]). Red dots are sensor locations.*  
  
In this challenge, features from the following sensors are available:  
<az_il, az_ir - vertical acceleration of wheelset axle (i = 1,2,3,4)  
<azp_il, azp_ir - vertical acceleration on bogie frame primary suspension level (above wheelset axle, i = 1,2 for leading bogie, and i = 3,4 for trailing bogie)  
<azs_i, azs_i - vertical acceleration on car body secondary suspension level (i = 1 above the leading bogie, and i = 2 above the trailing bogie)  
Additionally, the vehicle speed, the actual car body mass (including loading) and the track on which the train is currently driving are available.
