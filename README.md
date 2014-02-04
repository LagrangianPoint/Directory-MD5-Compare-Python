Directory MD5 Compare (Python)
============================

Tools for helping you compare two mirror servers to find out if one of then has been compromised by an attacker.

This program should work in any operating system.

## Requirements:
- Python 2.7


## Usage:
1. Run :
	```
	python show-all-files.py
	```
	
	on each of the servers that could have been compromised and the server that you know has not been attacked.
	You can exclude certain directories by adding them to the list **listUnwanted**
	This process could take a lot of time.
2. Copy the output files to your local environment.
3. Run:
	```
	python compare-md5-files.py UNHACKED-SERVER.txt HACKED-SERVER.txt
	```
	
	This will display which files had a different MD5 checksum, which might indicate that those files could be compromised.

