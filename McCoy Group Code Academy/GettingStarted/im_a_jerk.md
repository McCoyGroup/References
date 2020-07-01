```python
person = "Ryna"
place = "New Jersye"
bad_place = "Princeton"
print(f"{person} is from {place}. You know what's in {place}? {bad_place}")
```

then to run this we'll do

```console
$ python3 im_a_jerk.py
Ryna is from New Jersye. You know what's in New Jersye? Princeton
```

but...well that feels like a bit of a low blow (sorry Ryna).
So let's change this up to be a bit nicer.
We'll replace Princeton with an objectively better place, like Trenton.
So we'll change our script to look like

```python
person = "Ryna"
place = "New Jersye"
better_place = "Trenton"
print(f"{person} is from {place}. You know what's in {place}? {better_place}")
```

and then we get

```console
$ python3 im_a_jerk.py
Ryna is from New Jersye. You know what's in New Jersye? Trenton
```

at this stage we can do all sorts of stuff.

We could change our script so that instead of having to change up the actual body of the script we load the `person`, `place`, and `bad_place` from another file. Or we could pass them directly on the command line, (i.e. with `$ python3 im_a_jerk.py Mark Michigan Marquette`).
The possibilities are endless, and the best thing to do is explore for yourself.
