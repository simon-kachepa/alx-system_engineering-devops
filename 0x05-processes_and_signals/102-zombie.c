#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <stdbool.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_loop - Run an infinite while loop.
 * Return: 0 (Success).
*/
int infinite_loop(void)
{
	while (true)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five zombie processes.
 * Return: 0 (Success).
*/
int main(void)
{
	pid_t my_pid;
	char count = 0;

	while (count < 5)
	{
		my_pid = fork();
		if (my_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", my_pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_loop();

	return (EXIT_SUCCESS);
}
