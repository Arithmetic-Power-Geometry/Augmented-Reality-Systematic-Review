FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
ARG VINS_MONO_REF
RUN test -n "$VINS_MONO_REF"
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl git build-essential cmake && rm -rf /var/lib/apt/lists/*
COPY containers/vinsmono/install_vins_dependencies.sh /tmp/install_vins_dependencies.sh
RUN chmod +x /tmp/install_vins_dependencies.sh
WORKDIR /opt
RUN git clone https://github.com/HKUST-Aerial-Robotics/VINS-Mono.git && cd VINS-Mono && git checkout "$VINS_MONO_REF"
CMD ["/bin/bash"]
