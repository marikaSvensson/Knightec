/* C example
compile commando : mpicc main.c -o main 
run       -||-   : mpirun -2 ./main*/ 

#include <mpi.h>
#include <stdio.h>

int main (int argc, char* argv[]){
	int rank, size;
	
	MPI_Init(&argc, &argv); /* starts MPI */
	MPI_Comm_rank(MPI_COMM_WORLD, &rank); /* current process id*/
	MPI_Comm_size(MPI_COMM_WORLD, &size); /* #processes */
	printf("Hello world from process %d of %d \n", rank, size);
	MPI_Finalize();
	return  0;
}
