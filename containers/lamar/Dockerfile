FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
ARG LAMAR_REF
RUN test -n "$LAMAR_REF"
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates build-essential cmake python3.10 python3-pip python3.10-venv && rm -rf /var/lib/apt/lists/*
WORKDIR /opt
RUN git clone https://github.com/microsoft/lamar-benchmark.git && cd lamar-benchmark && git checkout "$LAMAR_REF"
WORKDIR /opt/lamar-benchmark
CMD ["/bin/bash"]
