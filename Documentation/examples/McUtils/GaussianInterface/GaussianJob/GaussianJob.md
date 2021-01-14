```python
from McUtils.GaussianInterface import GaussianJob 

job = GaussianJob(
        "water scan",
        description="Simple water scan",
        config= GaussianJob.Config(
            NProc = 4,
            Mem = '1000MB'
        ),
        job= GaussianJob.Job(
            'Scan'
        ),
        system = GaussianJob.System(
            charge=0,
            molecule=[
                ["O", "H", "H"],
                [
                    [0, 0, 0],
                    [.987, 0, 0],
                    [0, .987, 0]
                ]
            ],
            vars=[
                GaussianJob.System.Variable("y1", 0., 10., .1),
                GaussianJob.System.Constant("x1", 10)
            ]
    
        )
    )
# print(job.write(), file=sys.stderr)
self.assertIsInstance(job.format(), str)
```