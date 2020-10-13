## Wanyee Stephen 100565 ICS4A

from mpi4py import MPI
import numpy as np


# Calculates the area under curve using trapezoidal rule
def trapezoidal_rule(x, y):
    subintervals = x.size - 1
    y_right = y[1:]  # right endpoints
    y_left = y[:-1]  # left endpoints
    a = x[0]
    b = x[-1]
    dx = (b - a)/subintervals
    area = (dx/2) * np.sum(y_right + y_left)
    return area

# Splits the coordinates array into five chunks for each process
def get_chunks(coordinates_series):
    chunks = []
    for index in range(len(coordinates_series)):
        if(index+1 < len(coordinates_series)):
            chunks.append(np.array([coordinates_series[index], coordinates_series[index+1]]))
    return np.array(chunks)

# Define the coordinates
x = np.array([0, 2, 4, 6, 8, 10])
y = np.array([4, 6, 6, 4, 4, 5])

# Get the chunks
x_chunks = get_chunks(x)
y_chunks = get_chunks(y)

# Setup the MPI communication
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
number_of_processors = comm.Get_size()

# Calculate partial area in rank 1,2,3,4,5 and send to rank (processor) 0
final_area = 0
if rank != 0:
    partial_area = trapezoidal_rule(x_chunks[rank-1], y_chunks[rank-1])
    comm.send(partial_area,dest=0)
else:
    for procid in range(1, number_of_processors):
        received_partial_area = comm.recv(source=procid)
        final_area += received_partial_area
        print("Process 0 receives message from process",procid,": ",received_partial_area)
        if (procid == number_of_processors-1):
            print("Area under the curve is: ", final_area)
