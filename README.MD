# MPI Implementation in Python
A sample application that calculates the area under a curve using the trapezoidal rule given a list of coordinates. It uses processors to calculate partial solutions of the calculations and sent to a single process that sums the partials.

## Pre-requisites
- An implementation of MPI installed locally.
- numpy
- mpi4py

## Running the solution
``mpiexec -n 6 python -m mpi4py mpi_area_under_curve.py``
> The code is written with the assumption that 6 processors will be created.