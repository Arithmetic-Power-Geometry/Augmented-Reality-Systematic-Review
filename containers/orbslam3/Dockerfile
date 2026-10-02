FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ARG ORB_SLAM3_REF
RUN test -n "$ORB_SLAM3_REF"
RUN apt-get update && apt-get install -y --no-install-recommends build-essential cmake git ca-certificates pkg-config libeigen3-dev libopencv-dev libgl1-mesa-dev libglew-dev libboost-dev libboost-thread-dev libboost-filesystem-dev && rm -rf /var/lib/apt/lists/*
WORKDIR /opt
RUN git clone https://github.com/stevenlovegrove/Pangolin.git && cd Pangolin && git checkout v0.6 && mkdir build && cd build && cmake .. && cmake --build . -j2 && cmake --install .
RUN git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git && cd ORB_SLAM3 && git checkout "$ORB_SLAM3_REF"
WORKDIR /opt/ORB_SLAM3
RUN chmod +x build.sh && ./build.sh
