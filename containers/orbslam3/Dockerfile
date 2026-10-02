FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
ARG ORB_SLAM3_REF
ARG PANGOLIN_REF
RUN echo "$ORB_SLAM3_REF" | grep -Eq '^[0-9a-f]{40}$' && echo "$PANGOLIN_REF" | grep -Eq '^[0-9a-f]{40}$'
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential cmake git ca-certificates pkg-config libeigen3-dev libopencv-dev \
    libgl1-mesa-dev libglew-dev libboost-dev libboost-thread-dev libboost-filesystem-dev \
    python3 python3-numpy && rm -rf /var/lib/apt/lists/*
WORKDIR /opt
RUN git clone https://github.com/stevenlovegrove/Pangolin.git && \
    cd Pangolin && git checkout "$PANGOLIN_REF" && test "$(git rev-parse HEAD)" = "$PANGOLIN_REF" && \
    mkdir build && cd build && cmake .. && cmake --build . -j2 && cmake --install .
RUN git clone https://github.com/UZ-SLAMLab/ORB_SLAM3.git && \
    cd ORB_SLAM3 && git checkout "$ORB_SLAM3_REF" && test "$(git rev-parse HEAD)" = "$ORB_SLAM3_REF"
WORKDIR /opt/ORB_SLAM3
RUN chmod +x build.sh && ./build.sh
RUN test -x Examples/Stereo-Inertial/stereo_inertial_euroc && \
    printf 'ORB_SLAM3=%s\nPANGOLIN=%s\n' "$ORB_SLAM3_REF" "$PANGOLIN_REF" > /opt/BUILD_PROVENANCE.txt
