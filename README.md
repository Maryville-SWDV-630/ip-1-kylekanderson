## SWDV-630: Object-Oriented Coding
## Kyle Anderson
## Week 1 Assignment

## 4) Explain the difference between interfaces and implementation.

The difference between interfaces and implementation is one of the major benefits of Object-Oriented Programming. Interfaces describe the means in which objects interact with each other. They are the publicly exposed points of an object that are available for other objects to interact with. On the other hand, Implementation describes the internal workings of an object. These details are private and not visible to other objects.

## 5) Using both visual and written descriptions, think through the interface-implementation of a large scale storage system.   In many systems today, we have the ability to store information from a single application to a variety of storage devices - local storage (hard drive, usb), the cloud and/or some new medium in the future.   How would you design an interface structure such that all of the possible implementations could store data effectively.

On a high-level, a storage interace like the one described would likely include methods for creating, reading, updating, and deleting data. Without the specific needs of the consumers of the interface, I would consider building the interface to target a specific storage medium by default, but allow the user to provide a target medium as a parameter, if they so choose. Documentation or another interface supplying the available media would need to be provided as well. A basic "Create" interface would allow the consumer to provide an identifier for their data, the data itself, and (optionally) the storage media/location for storage. The interface could return a boolean to indicate if the storage operation proceeded successfully or not. A "Read" interface would allow the consumer to provide the identifier to for their data and (optionally) the storage media/location. The interface would return the data (or possibly a dictionary of data if multiple results are found). An "Update" interface would allow the consumer to provide an identifier, the new data to be stored, and (optionally) the storage media/location. The interface could return a boolean indicating if the update was successfully performed. Finally, a "Delete" interface would allow the consumer to provide an identifier and (optionally) the storage media/location. Again, the interface could provide a boolean indicating if the operation was successful.

As far as the implementation portion of the interface, I would begin by building the storage integrations with well-established, high performant media. Then, iterate over time to expand the available options to include more peripheral media and any new technology. This would ensure that the interface would remain backwards compatible with existing functionality as it is being improved on.
