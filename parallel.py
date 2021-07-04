import multiprocessing
import time
import random
import sys
import subprocess
import sys
import os
import argparse


TIMEOUT = 200
NUM_PROCESSES = 1

parser = argparse.ArgumentParser(description='Run processes in parallel')
parser.add_argument('--filename', action='store', dest='filename', type=str, help='name of file with list of commands to run')	           
parser.add_argument('--num_processes', type=int, dest='num_processes', default=NUM_PROCESSES, help='number of processes to use')
parser.add_argument('--timeout', type=int, dest='timeout', default=TIMEOUT, help='process timeout in seconds')					

def run_command(cmd):
	cmd_args = cmd.strip().split(' ')
	outfile_name = cmd_args[-1]
	torun = cmd_args[:-1]
	with open(outfile_name, "w") as outfile:
		t1 = time.time()
		print(cmd + "started " + str(t1))
		try:
			subprocess.run(torun, stdout=outfile, stderr=outfile, timeout=args.timeout)
		except subprocess.TimeoutExpired:
			print('TIMEOUT DETECTED: subprocess')				
			outfile.write("TIMEOUT")
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

	with multiprocessing.Pool(args.num_processes) as pool:
		pool.map(run_command, cmds, 4)


if __name__ == '__main__':
	multiprocessing.freeze_support()
	args = parser.parse_args()
	read_and_execute(args.filename)
