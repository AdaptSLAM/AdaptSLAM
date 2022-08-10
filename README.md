The AdaptSLAM implementation is based on [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) and [Edge-SLAM](https://github.com/droneslab/edgeslam).

#### Prerequisites.
Setup the [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3/blob/master/README.md) prerequisites.

#### Our testing setup
  * Dell XPS 8930 desktop with Intel (R) Core (TM) i7-9700K CPU@3.6GHz and NVIDIA GTX 1080 GPU, and a Lenovo Legion 5 laptop (with an AMD Ryzen 7 4800H CPU and an NVIDIA
GTX 1660 Ti GPU) using a virtual machine with 4-core CPUs and 8GB of RAM.
  * Ubuntu 18.04LTS.
  * OpenCV 3.4.2.
  * Eigen3 3.2.10.
 
#### Building AdaptSLAM
a. Clone the repository.
  ```
  git clone https://github.com/AdaptSLAM/AdaptSLAM.git
  ```
b. Build the Thirdparty libraries and AdaptSLAM.
 ```
 cd AdaptSLAM
 chmod +x build.sh
 ./build.sh
 ```
#### Running Examples

a. Download the [EuRoC V102 sequence](http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room2/V2_02_medium/V2_02_medium.zip).

b. Execute the following script:
```
./Examples/Monocular/mono_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular/EuRoC.yaml V102FileDirectory ./Examples/Monocular/EuRoC_TimeStamps/V102.txt dataset-V102_mono
```
Change ```V102FileDirectory``` to the directory where the dataset has been uncompressed. 
