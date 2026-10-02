ARG OPENVINS_REF
FROM ubuntu:22.04
ARG OPENVINS_REF
RUN test -n "$OPENVINS_REF"
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /opt
RUN git clone https://github.com/rpng/open_vins.git && cd open_vins && git checkout "$OPENVINS_REF"
CMD ["/bin/bash"]
