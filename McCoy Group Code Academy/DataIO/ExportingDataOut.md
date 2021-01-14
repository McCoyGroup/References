# Getting Data out of Your Code

We've dealt with the process of getting data _into_ your programs, but sometimes you need to get it out, too. 
Maybe your calculation took a long time and you don't want to have to rerun it.
Maybe you'd like to use the results of this calculation as an intermediate in other ones.
The possibilities are myriad.
And so how do we want to do this?

Well, as we've been saying, [if you can, use NumPy](NumpyFiles.md).
If you can't that's where things get interesting.

<div class="alert alert-warning" markdown="1">
##### A Note on `np.savetxt()`

As we noted [before](LoadingDataIn.md#a-note-on-nploadtxt), sometimes life throws a wrench in your plans to do the right thing, and someone (usually using Fortran) needs tabular data.
If that's the case, the NumPy [`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html) function is going to be your friend.
</div>


### Just Use JSON

The theme of pretty much everything we've been saying up until now is that if you can't use NumPy, just use JSON.
So what does this look like in practice?

Well let's imagine we ran a discrete variable representation calculation and we've got a bunch of stuff we want to save

```python
dvr_name = 'my_dvr'
dvr_type = 'ColbertMiller1D'
dvr_range = [-1, 1]
dvr_points = 500
dvr_grid = ... # an vector from the calculation
dvr_pe = ... # a potential energy matrix
dvr_ke = ... # a kinetic energy matrix
dvr_engs = ... # vector of energies
dvr_wfns = ... # matrix of wavefunction values
```

Now we want to dump all of this to a JSON file.

Unfortunately, NumPy has no built-in way to write stuff to JSON, so we can't just say

```python
import json

with open("my_dvr_results.json", "w") as res:
    json.dump(
        dict(
            name = dvr_name,
            type = dvr_type,
            range = dvr_range,
            points = dvr_points,
            grid = dvr_grid,
            potential_energy = dvr_pe,
            kinetic_energy = dvr_ke,
            energies = dvr_engs,
            wavefunctions = dvr_wfns
            ),
        res
    )
```

instead we need to do one of three things, convert to regular python lists, write a hybrid format, or use HDF5.

#### array.tolist()

The first, and the one we recommend for most cases, is to use the `.tolist()` function supported by NumPy arrays to convert them into regular python lists.
JSON can deal with regular python lists.

That would look like

```python
import json

with open("my_dvr_results.json", "w") as res:
    json.dump(
        dict(
            name = dvr_name,
            type = dvr_type,
            range = dvr_range,
            points = dvr_points,
            grid = dvr_grid.tolist(),
            potential_energy = dvr_pe.tolist(),
            kinetic_energy = dvr_ke.tolist(),
            energies = dvr_engs.tolist(),
            wavefunctions = dvr_wfns.tolist()
            ),
        res
    )
```

#### Hybrid Formats

The second option is to use a _hybrid format_. This is going to be most useful when we're working with very large arrays and the memory penalty of `tolist` is too high.
These formats will store all _metadata_ in JSON format, but allow arrays to be written out in a more efficient format, which NumPy has support for.

Here's one example of how this can work. Our layout will be

```lang-none
{
    ...,
    arrays: [
        {key: 'array_1', dtype: 'float64', shape: [120, 5, 3]},
        {key: 'array_2', dtype: 'int32', shape: [500]},
        ...
    ]
}
flattened array 1 
flattened array 2
...
```

where we've written the metadata out over multiple lines, but for ease of processing we'll actually leave it as one line.

We can perform this like

<div class="card in-out-block" markdown="1">

```python
import json

meta = {
    'name': 'my_data',
    'range': [-1, 1],
    'npoints': len(grid),
    'arrays': [
        {'key':'grid', 'shape':grid.shape, 'dtype':grid.dtype.name},
        {'key':'energies', 'shape':engs.shape, 'dtype':engs.dtype.name},
        {'key':'wavefunctions', 'shape':wfns.shape, 'dtype':wfns.dtype.name}
    ]
}

with open('my_dvr_results.jsnp') as file:
    json.dump(meta, file)
    for array in [grid, engs, wfns]: # must align with what's in the meta data
        file.write("\n")
        array.flatten().tofile(file, sep=" ")
with open('my_dvr_results.jsnp') as file: # just so we can see what's inside
    print(file.read())
```
<div class="card-body out-block" markdown="1">

```lang-none
{"name": "my_data", "range": [-1, 1], "npoints": 50, "arrays": [{"key": "grid", "shape": [50], "dtype": "float64"}, {"key": "energies", "shape": [5], "dtype": "float64"}, {"key": "wavefunctions", "shape": [50, 5], "dtype": "float64"}]}
0.21901924207629442 0.2845811641290318 0.35014308618176915 0.41570500823450646 0.4812669302872438 0.5468288523399811 0.6123907743927185 0.6779526964454559 0.7435146184981932 0.8090765405509306 0.874638462603668 0.9402003846564053 1.0057623067091426 1.0713242287618798 1.1368861508146173 1.2024480728673548 1.268009994920092 1.3335719169728293 1.3991338390255668 1.464695761078304 1.5302576831310415 1.5958196051837787 1.6613815272365162 1.7269434492892535 1.7925053713419907 1.8580672933947282 1.9236292154474655 1.989191137500203 2.05475305955294 2.1203149816056777 2.185876903658415 2.251438825711152 2.3170007477638896 2.382562669816627 2.448124591869364 2.5136865139221016 2.579248435974839 2.6448103580275766 2.7103722800803136 2.775934202133051 2.8414961241857886 2.9070580462385256 2.972619968291263 3.0381818903440005 3.103743812396738 3.169305734449475 3.2348676565022125 3.30042957855495 3.365991500607687 3.4315534226604245
0.009001295964747488 0.027003887894241883 0.04500647982373659 0.06300907175323109 0.08101166368272575
-1.6297059196185867e-18 -2.1238603683495063e-17 -1.9600717185203036e-16 -1.3731601478408739e-15 -8.218185917980731e-15 -4.227914540010922e-17 -5.084342248937425e-16 -4.332144517493014e-15 -3.002680951714255e-14 -1.7897819993578514e-13 -9.059740244995207e-16 -1.0543155141422734e-14 -8.611109629014152e-14 -5.698475466077956e-13 -3.2404706891417078e-12 -1.7171629954202116e-14 -1.9092558963231228e-13 -1.4889229044500666e-12 -9.40214519164098e-12 -5.098064790049858e-11 -2.846932711821115e-13 -3.018161112932004e-12 -2.2424111219488243e-11 -1.3478927106839047e-10 -6.95067122466062e-10 -4.129171172995085e-12 -4.164009671710429e-11 -2.940051363784702e-10 -1.6777664190098841e-09 -8.205015616928294e-09 -5.239333858522271e-11 -5.012599259980382e-10 -3.3540088695643536e-09 -1.8117105418786575e-08 -8.376076604111632e-08 -5.815883186681261e-10 -5.263432211396559e-09 -3.327149414785951e-08 -1.6954856246750568e-07 -7.384017445826375e-07 -5.647821592968985e-09 -4.8192586037549805e-08 -2.867863628349973e-07 -1.3735044168554768e-06 -5.611658815615956e-06 -4.79812813409137e-08 -3.846084822713215e-07 -2.146043916755955e-06 ... 1.3735044166976815e-06 -5.61165881554646e-06 -5.815882009044431e-10 5.2634320539981354e-09 -3.3271493829883616e-08 1.695485625130424e-07 -7.38401744783632e-07 -5.239331244898199e-11 5.012601383956994e-10 -3.354008387025528e-09 1.8117105545311923e-08 -8.37607662871476e-08 -4.129388444613319e-12 4.164022492814449e-11 -2.940047539953715e-10 1.6777664070224127e-09 -8.205015798783275e-09 -2.848981448658778e-13 3.018074203228939e-12 -2.2424040720969595e-11 1.347890895594096e-10 -6.95067270195125e-10 -1.720736448735197e-14 1.9076352665703666e-13 -1.4890047052317808e-12 9.402089435454086e-12 -5.098067554187757e-11 -9.335616305004049e-16 1.0374985115028238e-14 -8.613933684963118e-14 5.699183398999688e-13 -3.2405077703636008e-12 -7.337023374629885e-17 3.9588334188743134e-16 -4.302858625647169e-15 3.011676891027034e-14 -1.7903129531564725e-13 1.423766939174147e-17 -1.5833142601610604e-17 -1.778352319409878e-16 1.4410574036154364e-15 -8.225059630431985e-15
```
</div></div>

When we ingest this, we'll do so using NumPy's [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html) method as well as the `readline` method of a file.

This will look like

<div class="card in-out-block" markdown="1">

```python
import json, numpy as np

with open('my_dvr_results.jsnp') as file:
    meta_line = file.readline()
    file_data = json.loads(meta_line)
    for arr_spec in file_data['arrays']:
        shp = arr_spec['shape']
        num_elements = int(np.prod(shp))
        arr = np.fromfile(file, dtype=arr_spec['dtype'], count=num_elements, sep=" ")
        file_data[arr_spec['key']] = arr.reshape(shp)
print(file_data) # just so we can confirm the right stuff is coming out
```

<div class="card-body out-block" markdown="1">

```python
{'name': 'my_data',
 'range': [-1, 1],
 'npoints': 50,
 'arrays': [{'key': 'grid', 'shape': [50], 'dtype': 'float64'},
  {'key': 'energies', 'shape': [5], 'dtype': 'float64'},
  {'key': 'wavefunctions', 'shape': [50, 5], 'dtype': 'float64'}],
 'grid': array([0.21901924, 0.28458116, 0.35014309, 0.41570501, 0.48126693,
        0.54682885, 0.61239077, 0.6779527 , 0.74351462, 0.80907654,
        0.87463846, 0.94020038, 1.00576231, 1.07132423, 1.13688615,
        1.20244807, 1.26800999, 1.33357192, 1.39913384, 1.46469576,
        1.53025768, 1.59581961, 1.66138153, 1.72694345, 1.79250537,
        1.85806729, 1.92362922, 1.98919114, 2.05475306, 2.12031498,
        2.1858769 , 2.25143883, 2.31700075, 2.38256267, 2.44812459,
        2.51368651, 2.57924844, 2.64481036, 2.71037228, 2.7759342 ,
        2.84149612, 2.90705805, 2.97261997, 3.03818189, 3.10374381,
        3.16930573, 3.23486766, 3.30042958, 3.3659915 , 3.43155342]),
 'energies': array([0.0090013 , 0.02700389, 0.04500648, 0.06300907, 0.08101166]),
 'wavefunctions': array([[-1.62970592e-18, -2.12386037e-17, -1.96007172e-16,
         -1.37316015e-15, -8.21818592e-15],
        [-4.22791454e-17, -5.08434225e-16, -4.33214452e-15,
         -3.00268095e-14, -1.78978200e-13],
        [-9.05974024e-16, -1.05431551e-14, -8.61110963e-14,
         -5.69847547e-13, -3.24047069e-12],
        [-1.71716300e-14, -1.90925590e-13, -1.48892290e-12,
         -9.40214519e-12, -5.09806479e-11],
        ...
        [-1.72073645e-14,  1.90763527e-13, -1.48900471e-12,
          9.40208944e-12, -5.09806755e-11],
        [-9.33561631e-16,  1.03749851e-14, -8.61393368e-14,
          5.69918340e-13, -3.24050777e-12],
        [-7.33702337e-17,  3.95883342e-16, -4.30285863e-15,
          3.01167689e-14, -1.79031295e-13],
        [ 1.42376694e-17, -1.58331426e-17, -1.77835232e-16,
          1.44105740e-15, -8.22505963e-15]])}
```
</div></div>

Another option, and one that will also help cut down on the size of all of the files, is to use the fact that all modern languages support reading `.zip` files, either natively or, for Fortran, through a DLL.
Rather than put all of these arrays in the same `.txt` file, we can put them in separate ones which can be loaded with NumPy's [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt) method and whose names are defined in a `data.json` file inside the ZIP. 
Here's a sample implementation for writing one of these hybrid files

```python
import zipfile, json, numpy as np, tempfile as tf, os

meta = {
    'name': 'my_data',
    'range': [-1, 1],
    'npoints': len(grid),
    'arrays': [
        {'key':'grid', 'shape':grid.shape, 'dtype':grid.dtype.name},
        {'key':'energies', 'shape':engs.shape, 'dtype':engs.dtype.name},
        {'key':'wavefunctions', 'shape':wfns.shape, 'dtype':wfns.dtype.name}
    ]
}

with zipfile.ZipFile('my_dvr_results.zip', 'w') as res:
    with tf.TemporaryDirectory() as tmp_dir:
        meta_dump = os.path.join(tmp_dir, 'data.json')
        with open(meta_dump, 'w') as dump:
            json.dump(meta, dump)
        res.write(meta_dump, arcname='data.json')
        for array, spec in zip([grid, engs, wfns], meta['arrays']):
            arr_dump = os.path.join(tmp_dir, spec['key'])
            np.savetxt(arr_dump, array.flatten(), newline=" ")
            res.write(arr_dump, arcname=spec['key'])
```

and here's how you'd read the file that was built

```python
import zipfile, json, numpy as np

with zipfile.ZipFile('my_dvr_results.zip') as file:
    with file.open('data.json') as header:
        file_data = json.load(header)
    for arr_spec in file_data['arrays']:
        name = arr_spec['key']
        shp = arr_spec['shape']
        num_elements = int(np.prod(shp))
        with file.open(name) as arr_dat:
            arr = np.loadtxt(arr_dat, dtype=arr_spec['dtype'])
            file_data[name] = arr.reshape(shp)
```

just for interest's sake, memory-wise the first format seems to be a bit more compact, but the latter obviously has the benefit that it is easier to decompose. The second can also potentially benefit from changing up the `compression` and `compressionlevel` on the `ZipFile` object.

#### HDF5

If you've got to move between platforms (esp. if you've got to use Fortran or C++) and JSON isn't cutting it, [HDF5](https://support.hdfgroup.org/HDF5/doc/H5.intro.html) might worth the plunge.

## This isn't Data Presentation

Note that we've focused on data _export_, not presentation.
In general, you don't want to mix the two. 
A table for a paper shouldn't be how you save your results.
If you _do_ want to learn about data presentation, we've got a section on [plotting](../Plotting) that you should check out.

<span class="text-muted">Next:</span>
 [NumPy Data Files](NumpyFiles.md)<br/>
<span class="text-muted">Previous:</span>
 [Getting Data into your Program](LoadingDataIn.md)

Got questions? Ask them on the [McCoy Group Stack Overflow](https://stackoverflow.com/c/mccoygroup/questions/ask)
{: .alert .alert-info}

---
[Edit on GitHub](https://github.com/McCoyGroup/References/edit/gh-pages/McCoy%20Group%20Code%20Academy/DataIO/ExportingDataOut.md)
