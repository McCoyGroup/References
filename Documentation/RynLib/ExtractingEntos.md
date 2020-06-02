# Extracting Entos

When using Entos, we link it in at runtime. This is for license reasons/convenience. 

To get a version of Entos to use, we extract the appropriate path from a base `entos` image.
We either do this using `docker cp` or by using `singularity build --sandbox <entos_img> <local/path>` and copy the file out of the sandbox directory.
