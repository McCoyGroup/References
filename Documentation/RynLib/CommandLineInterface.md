#RynLib Command-Line Interface

Since this is happening inside a container, we provide a command-line interface to the packages inside. This looks like:

```ignorelang
$ rynlib [--<flags>] group command [args]
```

You can find more info by running with the `--help` flag

```ignorelang
$ rynlib --help
rynlib [--output|--error|--script|--root|--noomp|--t|--interact] GRP CMD [ARGS] runs RynLib with the specified command
rynlib --help all: list all available commands
rynlib --help grp: list commands in grp
````

If we run `rynlib --help all` we get the full CLI documentation, such as it is

```ignorelang
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

