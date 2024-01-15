This Airbnb project includes a command-line tool and various classes for creating and managing instances of different property types. The command-line tool allows users to perform actions like creating, showing, and updating instances through simple commands.

## The Use of Command-Line Tool

1. Start the Tool:
   - Run `$ ./console.py` to start the command-line tool.

2. Available Commands:
   - **create:** Create a new instance of a property (e.g., BaseModel).
   - **show:** Display details of an instance by providing the class name and ID.
   - **destroy:** Delete an instance based on the class name and ID.
   - **all:** List all instances of a specific class.
   - **update:** Modify attributes of an instance.

3. Examples:
   - Creating a BaseModel instance: `$ create BaseModel`
   - Showing details of an instance: `$ show BaseModel 1234-1234-1234`
   - Deleting an instance: `$ destroy BaseModel 1234-1234-1234`
   - Listing all instances of a class: `$ all BaseModel`
   - Updating an instance attribute: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`

## BaseModel Class

- **Attributes:**
  - **id:** Unique identifier.
  - **created_at:** Date and time of creation.
  - **updated_at:** Date and time of the last update.

- **Methods:**
  - **save:** Update the `updated_at` attribute.
  - **to_dict:** Return a dictionary representation of the instance.

## FileStorage Class

- **Methods:**
  - **all:** Return all stored objects.
  - **new:** Add an object to storage.
  - **save:** Save objects to a JSON file.
  - **reload:** Load objects from the JSON file.

## Property Classes

- User, State, City, Amenity, Place, and Review classes inherit from BaseModel.
- They have specific attributes representing user details, location, amenities, etc.

## Console Usage

- The console allows users to interact with the property classes, perform actions, and manage instances.

Contributors: -Merveille MK
              - Jules G. 
