# Command-Line Interface

Since this is happening inside a container, we provide a command-line interface to the packages inside. This looks like:

```console
$ rynlib [--<flags>] group command [args]
```

You can find more info by running with the `--help` flag

```console
$ rynlib --help
rynlib [--output|--error|--script|--root|--noomp|--t|--interact] GRP CMD [ARGS] runs RynLib with the specified command
rynlib --help all: list all available commands
rynlib --help grp: list commands in grp
````

If we run `rynlib --help all` we get the full CLI documentation, such as it is

```console
$ rynlib --help all
rynlib  [--<flags>]  GRP  CMD  [ARGS]  runs  RynLib  with  the  specified  command
Flags:
  --help:  print  this  help  message
  --help  <grp>:
    all:  list  all  available  commands
    grp:  list  commands  in  grp
  --output=<FILE>:  bind  stdout  to  FILE
  --error=<FILE>:  bind  stderr  to  FILE
  --script=<FILE>:  run  FILE  in  the  RynLib  environment
  --root=<PATH>:  specify  the  root  directory  to  do  resource  resolution  from
  --interact:  start  an  interactive  session  after  running  the  command
  --fulltb:  turn  on  full  tracebacks
  --noomp:  turn  off  OpenMP  parallelism
  --thomp:  specify  the  number  of  OpenMP  threads  that  were  set  outside  the  program  (if  !=  os.cpu_count)
  --notbb:  turn  off  Threaded  Building  Blocks  parallelism
  --thtbb:  specify  the  number  of  TBB  threads  that  were  set  outside  the  program  (if  !=  os.cpu_count)

config:
    build-libs
      Builds (or rebuilds) the libraries that the container uses. Shouldn't need to be called outside of Dockerfile/Singularity.def
    run-tests
      Runs the unit tests distributed with the package. Can be run in debug mode or validation mode.
    set-config
      Set configuration options for RynLib -- currently inactive
    reset
      Resets RynLib configuration to its default state. Useful for updates.
    install-mpi
      Installs MPI. Shouldn't need to be called outside of Dockerfile/Singularity.def
    reload-dumpi
      Rebuilds just the Dumpi library that handles the MPI communication
    configure-mpi
      Installs MPI and rebuilds Dumpi

sim:
    list
      Lists the simulations that have been added
    add
      Adds a new simulation. Args: NAME SRC
    remove
      Removes a simulation. Args: NAME
    run
      Runs a simulation. Args: NAME
    restart
      Restarts a stopped simulation. Args: NAME
    status
      Gets the status of a simulation. Args: NAME
    list-samplers
      Lists the added importance samplers
    list-archive
      Lists the archived simulations
    archive
      Archives a simulation. Args: NAME
    add-sampler
      Adds an importance sampler. Args: NAME SRC --config=CONFIG_FILE
    remove-sampler
      Removes an importance sampler. Args: NAME
    test-sampler
      Tests an importance sampler. Args: NAME
    test-HO
      Runs a harmonic oscillator DMC as a test

pot:
    list
      Lists the potentials that have been added
    add
      Adds a new potential. Args: NAME SRC
    remove
      Removes a potential. Args: NAME
    import
      Imports a potential from an existing archive. Args: NAME SRC
    export
      Export a potential to an archive. Args: NAME SRC
    compile
      Ensures that a potential has been compiled. Args: NAME
    status
      Checks the status of a potential. Args: NAME
    configure-entos
      Configures the built in Entos potential
    test-entos
      Tests the built in Entos potential
    test-HO
      Tests the built in Harmonic Oscillator potential
    test-entos-mpi
      Tests Entos via MPI
    test-ho-mpi
      Tests the HO via MPI
    test
      Tests a generic potential. Args: NAME
    test-mpi
      Tests a generic potential under MPI. Args: NAME
```

## Environment Variables & Bash Flags

All of that is just for the actual containerized application itself. 
The `rynlib` command also provides convenience syntax/flags/variables for running things, to make it easier to remember how stuff works.

### Environment Variables

All environment variables are prefaced with `RYNLIB`.
The current list of them is

```shell
RYNLIB_CONFIG_PATH=<PATH/IN/CONTAINER>
  the path to use for finding/storing simulations, potentials, etc. (default: $PWD/config)
RYNLIB_ENTOS_PATH=<PATH/ON/HOST>
  the path to the Entos folder to use when using Entos as a potential (default: None)
RYNLIB_IMAGE=<IMAGE_OR_SIF>
  the image to use when running rynlib (default: rynimg or rynimg.sif)
RYNLIB_CONTAINER_RUNNER=<EXEC>
  the executable to use for running containers (default: platform dependent, locally docker)
```

There are a few flags that _can_ be changed, but aren't really intended to be changed

```shell
RYNLIB_IMAGE_NAME="rynimg"
  the base name of the image we're working with
RYNLIB_DOCKER_IMAGE="mccoygroup/rynlib:$RYNLIB_IMAGE_NAME"
  the DockerHub location for the image
RYNLIB_SINGULARITY_EXTENSION="-centos"
  the extension to the image name used when running with Singularity (well really just on a CentOS based HPC)
RYNLIB_SHIFTER_IMAGE="registry.services.nersc.gov/b3m2a1/$RYNLIB_IMAGE_NAME"
  the image hosted on the NeRSC image registry -- not really used anymore, but easy to update so left as is
```

### Bash Flags

All bash flags start with a single `-` and come before any `--` options or container commands. 
The current list of those is

```ignorelang
-n <NUMBER>
  run using the `mpirun` command inside the container spawing NUMBER jobs
-L <PATH>
  run using the specified path to the RynLib source code -- allows for quick tests and changes, since small source changes don't require a full rebuild
-e
  echo the command that would be run -- necessary in some cases where external `mpirun` refuses to run the `rynlib` bash function
-V [EXTERNAL_PATH]:[CONTAINER_PATH],[EXTERNAL_PATH]:[CONTAINER_PATH]...
  bind the specified directories into the container -- useful for getting data in/out
-W <PATH>
  run using PATH as the initial working directory
-E <EXEC>
  run using EXEC as the container entrypoint, rather than CLI.py -- useful for starting /bin/bash
-M <FILE>
  run using a memory profiler and write the results to FILE -- useful for finding memory leaks on the C++ side
```