# 2017-PHM-challenge-society  
***  
### System Description  
***This year’s challenge continues the trend started in the previous years and is focused on the combination of physics-based modeling and statistical approaches for prediction. It is recommended that the solution you design and implement use physics-based modeling elements. Points will be given to those approaches that provide a physical connection to the data such as health states of various components, relationship between data and model parameters or states, etc.The system under investigation is a conventional bogie vehicle. Figure 1 depicts a schematic diagram of a bogie vehicle model, consisting of a vehicle body, two bogies and four wheelsets. The simplified model includes coil springs and dampers used in the primary suspension, and air springs in the secondary suspension. Sensors are placed on the wheelsets, on the bogie frames and on the car body as shown in the figure. Random track irregularities, roughness and faults will induce vibrations along each axis.The vehicle is operated on tracks with different irregularities, layouts, contact geometries and speeds. Additionally the vehicle parameters like loading, stiffness and damping rates vary in some range even in experiments without faults in the components.***  
![alt](https://www.phmsociety.org/sites/phmsociety.org/files/PHM17DCFig1.png)  
*Figure 1. Diagram of a simplified vehicle model (See [1]). Red dots are sensor locations.*  
  
In this challenge, features from the following sensors are available:  
>az_il, az_ir - vertical acceleration of wheelset axle (i = 1,2,3,4)  
>azp_il, azp_ir - vertical acceleration on bogie frame primary suspension level (above wheelset axle, i = 1,2 for leading bogie, and i = 3,4 for trailing bogie)  
>azs_i, azs_i - vertical acceleration on car body secondary suspension level (i = 1 above the leading bogie, and i = 2 above the trailing bogie)  

Additionally, the vehicle speed, the actual car body mass (including loading) and the track on which the train is currently driving are available.  
  
**Table 1: The following table indicates the available features and the sensor underlying the raw data for each feature. Five features are given as a feature set for each sensor, representing spectral information in non-overlapping frequency bands for increasing frequencies. The k-th (k=1...5) feature in each feature set is computed in the same way across sensors.**  
|Feature set per sensor|	Sensors|
|f101 - f105|	azs_1|
|f106 - f110|	azp_1r|
|f111 - f115|	azp_1l|
|f116 - f120|	azp_2r|
|f121 - f125|	azp_2l|
|f126 - f130|	az_1r|
|f131 - f135|	az_1l|
|f136 - f140|	az_2r|
|f141 - f145|	az_2l|
|f146 - f150|	azs_2|
|f151 - f155|	azp_3r|
|f156 - f160|	azp_3l|
|f161 - f165|	azp_4r|
|f166 - f170|	azp_4l|
|f171 - f175|	az_3r|
|f176 - f180|	az_3l|
|f181 - f185|	az_4r|
|f186 - f190|	az_4l|
