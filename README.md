This is a cool little tool for working through all modules within the python standard library. There are 133 modules in 
total and Python Module of the Week (http://pymotw.com/2/) does an amazing job detailing each one. This program will
scrape the site once and store links to the modules in a small Sqlite3 database. It will then pull a random module from 
the database and launch it in your default browser. 

There are a few requirements so please start by creating a virtual environment and loading requirements.txt.

pip install -r requirements.txt

The website can then be launched by running stdlib_grab.py.

python stdlib_grab.py

The database updates automatically so the same module will never appear twice. Enjoy!

-------------------------------------------------------------------------------------
Big thanks to Doug Hellmann, http://doughellmann.com/, who runs and maintains PYMOTW! 

