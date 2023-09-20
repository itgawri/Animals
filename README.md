# Animals
This project revolves around managing information about various animals using Python classes. The core classes involved in this project are Pet, Cat, Dog, and a subclass of Dog called Poodle. Each class represents different types of animals, with specific attributes and behaviors.

Here's a brief overview of the key functionalities and methods of these classes:

Pet Class:

Represents a generic pet with attributes like type, name, and sound.
Provides methods to make the pet speak and play.
Cat Class:

Inherits from the Pet class and specializes in cat-related attributes.
Includes an additional attribute, coat_length, which specifies the length of the cat's coat.
Provides a method, purr(), to simulate a cat's purring sound.
Dog Class:

Inherits from the Pet class and specializes in dog-related attributes.
Includes an additional attribute, size, indicating the size of the dog.
Overrides the speak() method to customize the sound based on the dog's size.
Introduces a new method, wag_tail(), to simulate a dog wagging its tail.
Poodle Class (Subclass of Dog):

Inherits from the Dog class and focuses on Poodle-specific attributes.
Sets the is_hypoallergenic attribute to True for Poodles.
Adds a method, groom(), to signify the grooming process for Poodles.

This project is designed to showcase object-oriented programming in Python, including inheritance and method overriding. It allows you to create and manage different types of pets, each with its unique characteristics and behaviors. You can add new attributes and methods to further extend the functionality of these classes to suit your needs.
