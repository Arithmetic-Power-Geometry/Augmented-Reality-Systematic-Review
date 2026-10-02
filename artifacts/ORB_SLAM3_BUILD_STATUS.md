# ORB-SLAM3 Build Evidence Status

A dedicated GitHub Actions build-smoke workflow now exists for the frozen E001 image.

The workflow:
1. builds ORB-SLAM3 from the frozen 40-hex commit;
2. builds Pangolin from the commit targeted by annotated tag v0.6;
3. verifies the EuRoC stereo-inertial executable exists;
4. prints embedded source provenance;
5. captures the Docker image ID and complete Debian package inventory;
6. uploads that inventory as a workflow artifact.

**Important:** committing this workflow is not evidence that the image has built successfully. Build status becomes evidence only after a specific workflow run is observed as successful. Scientific E001 execution remains blocked until that evidence or an equivalent recorded local build exists.
