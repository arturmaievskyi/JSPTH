from JSPTH.ClasesCode import EventEmitter as EE

# Create an event emitter instance
emitter = EE()

# Define event listeners
def greet_listener(name):
    print(f"Hello, {name}!")

def farewell_listener(name):
    print(f"Goodbye, {name}!")

# Register events
emitter.on('greet', greet_listener)
emitter.on('farewell', farewell_listener)

# Emit events
emitter.emit('greet', 'Alice')      # Output: Hello, Alice!
emitter.emit('farewell', 'Bob')     # Output: Goodbye, Bob!

# Register one-time event
emitter.once('greet', lambda name: print(f"This will run only once for {name}."))

# Emit again
emitter.emit('greet', 'Charlie')    # Output: Hello, Charlie!
                                    # Output: This will run only once for Charlie.

# Emit again (one-time listener is now removed)
emitter.emit('greet', 'Dave')       # Output: Hello, Dave!

# Remove specific listener
emitter.off('greet', greet_listener)

# Emit again (no output as greet_listener has been removed)
emitter.emit('greet', 'Eve')

# Remove all listeners
emitter.remove_all_listeners()

# Emit again (no output as all listeners are removed)
emitter.emit('farewell', 'Bob')
