# Extracting Entos

When using Entos, we link it in at runtime. This is for license reasons/convenience. 

To get a version of Entos to use, we extract the appropriate path from a base `entos` image.
We either do this using `docker cp` and related commands or, more commonly on Mox, using `singularity`.

To do that, we get the Entos image tag from our collaborators and pull it by using 

```sh
singularity build --sandbox --docker-login tmp docker://<ENTOS_IMAGE>
```

and then we pull out the folder we link in using

```sh
mv tmp/opt/entos entos_<SYSTEM>_<COMMITID>
```

which can then be used inside RynLib by setting `RYNLIB_ENTOS_PATH`.

---
[Edit on GitHub <i class="fab fa-github" aria-hidden="true"></i>](https://github.com/McCoyGroup/References/edit/gh-pages/Documentation/RynLib/ExtractingEntos.md)
