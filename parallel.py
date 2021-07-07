import multiprocessing
import time
import random
import sys
import subprocess
import sys
import os
import argparse
import resource
import shlex

TIMEOUT = 200
MEMLIMIT = 3 * 1024 * 1024 * 1024
NUM_PROCESSES = 1

parser = argparse.ArgumentParser(description='Run processes in parallel')
parser.add_argument('--filename', action='store', dest='filename', type=str, help='name of file with list of commands to run')
parser.add_argument('--num_processes', type=int, dest='num_processes', default=NUM_PROCESSES, help='number of processes to use')
parser.add_argument('--timeout', type=int, dest='timeout', default=TIMEOUT, help='process timeout in seconds')
parser.add_argument('--memlimit', type=int, dest='memlimit', default=MEMLIMIT, help='memory limit in bytes')

def run_command(cmd):
	cmd_args = shlex.split(cmd)
	outfile_name = cmd_args[-1]
	torun = cmd_args[:-1]
	with open(outfile_name, "w") as outfile:
		t1 = time.time()
		print(cmd + "started " + str(t1))
		try:
			resource.setrlimit(resource.RLIMIT_AS, (args.memlimit, resource.RLIM_INFINITY))
			resource.setrlimit(resource.RLIMIT_CPU, (args.timeout, resource.RLIM_INFINITY))
			subprocess.call(torun, stdout=outfile, stderr=outfile)
#		except subprocess.TimeoutExpired:
#			print('TIMEOUT DETECTED: subprocess')
#			outfile.write("TIMEOUT")
		except Exception as exc:
			print(cmd + 'CAUGHT EXCEPTION: ' + str(exc))
			outfile.write('CAUGHT EXCEPTION: ' + str(exc))
			raise(exc)
		t2 = time.time()
		print("ended "  + str(t2) + " --- took " + str(t2 - t1))
		outfile.close()

def read_and_execute(filename):
	with open(filename, "r") as f:
		cmds = f.readlines()
		f.close()

	pool = multiprocessing.Pool(args.num_processes)
	pool.map(run_command, cmds, args.num_processes)


if __name__ == '__main__':
	multiprocessing.freeze_support()
	args = parser.parse_args()
	read_and_execute(args.filename)
