from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
number_of_processors = comm.Get_size()

if rank != 0:
    message="Hello from "+ str(rank)
    comm.send(message,dest=0)
else:
    for procid in range(1, number_of_processors):
        message=comm.recv(source=procid)
        print("Process 0 receives message from process",procid,":",message)
