# tmuk14-Particle-Sandbox
A particle sandbox for simulating simple particles such as sand, water and other elements. Made with Pygame

- Simon Lorentzon    [Somoin](https://github.com/Somoin)
- Alexander Lundahl  [Aleccoz](https://github.com/Aleccoz)
- Edrin Zahiri       [EdrinZahiri](https://github.com/EdrinZahiri)

# Declaration

I, Simon Lorentzon, declare that I am the sole author of the content I add to this repository. <br/>
I, Alexander Lundahl, declare that I am the sole author of the content I add to this repository. <br/>
I, Edrin Zahiri, declare that I am the sole author of the content I add to this repository. <br/>

# Particle Sandbox
A particle simulator using the concept of Cellular Automaton. <br/>
The program is a desktop GUI where you can select different materials / elements that you can place on the screen with the mouse, each with different behaviors. <br/>

Basic Examples: 
- Sand particles that fall and clump up
- Water particles that flow
- Concrete particles that are static

# Implementation
The language used is Python using the [Pygame](https://www.pygame.org/news) library. 

# How to run
Ensure Pygame is installed and run main.py from inside the src directory.

# Testing
To run the unit test you need to install [pytest](https://docs.pytest.org/en/stable/getting-started.html). <br/>
When inside the src directory write into the terminal: python -m pytest unit_test.py 

# Generate code coverage
To generate code coverage you need to install [Coverage.py](https://coverage.readthedocs.io/en/7.8.0/). <br/>
When inside the src directory write into the terminal: python -m coverage run main.py <br/>
After you run the program and test every feature you can close it and write into the terminal: python -m coverage report <br/>
You can also create an HTML file with the command: python -m coverage html

# Kanban Board
https://github.com/users/Somoin/projects/1/views/1
