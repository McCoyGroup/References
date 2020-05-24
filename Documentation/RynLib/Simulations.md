# Simulations

The core use case of RynLib is to provide a convenient, scalable simulation environment for diffusion Monte Carlo.
To make that possible, all of the rest of this stuff was built out.

Dealing with simulations will (hopefully) feel very reminiscent of dealing with the potentials and importance samplers, though.

### Getting a Simulation Into a Container

The first thing we need to do is get a simulation set up that we can actually run, the command for this is

```shell
rynlib sim add NAME SRC
```

and here 