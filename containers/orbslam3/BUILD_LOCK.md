# E001 Build Lock

The E001 container is aligned to the frozen ORB-SLAM3 source documentation.

- Base OS: Ubuntu 18.04.
- ORB-SLAM3: `4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4`.
- Pangolin: `dd801d244db3a8e27b7fe8020cd751404aa818fd`, the commit referenced by the upstream annotated `v0.6` tag.
- ORB-SLAM3 bundled DBoW2/g2o remain those contained in the frozen ORB-SLAM3 tree.

Both source checkouts are verified with `git rev-parse HEAD` during image construction. The build fails if either supplied ref is not a full 40-hex commit.

Distribution package versions (OpenCV, Eigen and system libraries) are not claimed immutable merely from the Dockerfile. The scientific run must retain the final image digest and package inventory. A successful Dockerfile build is evidence of executability, not algorithmic performance.
