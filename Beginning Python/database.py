# Listing 10-8. A Simple Database Application
# database.py
import sys, shelve
def store_person(db):
  """
  Query user for data and store it in the shelf object
  """
  pid = raw_input('Enter unique ID number: ')
  person = {}
  person['name'] = raw_input('Enter name: ')
  person['age'] = raw_input('Enter age: ')
  person['phone'] = raw_input('Enter phone number: ')
  
  db[pid] = person

def lookup_person(db):
  """
  Query user for ID and desired field, and fetch the corresponding data from
  the shelf object
  """
  pid = raw_input('Enter ID number: ')
  field = raw_input('What would you like to know? (name, age, phone) ')
  field = field.strip().lower()
  print field.capitalize() + ':', \
    db[pid][field]

def print_help():
  print 'The available commands are:'
  print 'store : Stores information about a person'
  print 'lookup : Looks up a person from ID number'
  print 'quit : Save changes and exit'
  print '? : Prints this message'

def enter_command():
  cmd = raw_input('Enter command (? for help): ')
  cmd = cmd.strip().lower()
  return cmd

def main():
  database = shelve.open('C:\\database.dat') # You may want to change this name
  try:
    while True:
      cmd = enter_command()
      if cmd == 'store':
        store_person(database)
      elif cmd == 'lookup':
        lookup_person(database)
      elif cmd == '?':
        print_help()
      elif cmd == 'quit':
        return
  finally:
    database.close()
if __name__ == '__main__': main()

The program shown in Listing 10-8 has several interesting features:
• Everything is wrapped in functions to make the program more structured. (A possible
improvement is to group those functions as the methods of a class.)
• The main program is in the main function, which is called only if __name__ == '__main__'.
That means you can import this as a module and then call the main function from another
program.
• I open a database (shelf) in the main function, and then pass it as a parameter to the other
functions that need it. I could have used a global variable, too, because this program is
so small, but it’s better to avoid global variables in most cases, unless you have a reason
to use them.
• After reading in some values, I make a modified version by calling strip and lower on
them because if a supplied key is to match one stored in the database, the two must be
exactly alike. If you always use strip and lower on what the users enter, you can allow
them to be sloppy about using uppercase or lowercase letters and additional white-
space. Also, note that I’ve used capitalize when printing the field name.
• I have used try and finally to ensure that the database is closed properly. You never
know when something might go wrong (and you get an exception), and if the program
terminates without closing the database properly, you may end up with a corrupt data-
base file that is essentially useless. By using try and finally, you avoid that.
