# Musical Instruments – Strategy Design Pattern

## Project Overview

This project demonstrates the implementation of the **Strategy Design Pattern** using Python and a collection of musical instruments. The objective is to explore how object-oriented programming principles can be used to create flexible, reusable, and maintainable software.

Each musical instrument has its own playing behavior, which is implemented independently from the instrument itself. By separating these behaviors into individual classes, the program allows instruments to change how they are played without modifying their underlying structure.

This project was developed as part of **COP4814 – Component-Based Software Development** at Florida International University (FIU).

## Key Features

- **Strategy Design Pattern:** Separates instrument objects from their playing behaviors, allowing behaviors to be changed dynamically.
- **Object-Oriented Programming:** Demonstrates inheritance, abstraction, polymorphism, and encapsulation.
- **Abstract Classes:** Uses Python's `ABC` and `abstractmethod` to establish a common structure for instruments and playing behaviors.
- **Dynamic Behavior Changes:** Allows an instrument's playing behavior to be modified during execution.
- **Reusable Components:** Playing behaviors can be shared across multiple instrument classes.

## Musical Instruments

The application includes five instrument classes:

- **Double Bass:** Played using a bow.
- **Clarinet:** Played by buzzing a reed.
- **Harp:** Played by plucking strings.
- **Tuba:** Played by buzzing the lips.
- **Violin:** Played using a bow.

Each instrument inherits from the abstract `Instrument` class and implements its own `display()` method.

## Playing Behaviors

The project implements playing strategies through a common `PlayBehavior` interface.

These include:

- `PlayWithBow`
- `BuzzAReed`
- `PluckWithFingers`
- `BuzzWithLips`

Each strategy defines how an instrument is played, making it possible to reuse or replace behaviors independently of the instrument classes.

## Technologies Used

- **Python 3** – Core programming language
- **Object-Oriented Programming (OOP)** – Software design and organization
- **Python ABC Module** – Abstract classes and methods
- **Strategy Design Pattern** – Flexible behavior management
- **Git & GitHub** – Version control and project hosting

## How the Program Works

1. An abstract `Instrument` class establishes the common structure for musical instruments.
2. Individual instrument classes inherit from `Instrument`.
3. Playing behaviors are implemented as separate strategy classes.
4. Each instrument is assigned a playing behavior when initialized.
5. The `perform_play()` method delegates the playing action to the assigned strategy.
6. The `set_play_behavior()` method allows an instrument to change its behavior at runtime.

This structure demonstrates how the Strategy Design Pattern promotes flexibility by favoring composition over tightly coupled implementations.

## Running the Project

**1. Clone the repository**

```bash
git clone https://github.com/olufemifadipe/Musical-Instruments-Strategy-Pattern.git
```

**2. Navigate to the project directory**

```bash
cd Musical-Instruments-Strategy-Pattern
```

**3. Run the Python application**

```bash
python "Musical- Instruments-Strategy-Pattern.py"
```

The program displays each musical instrument and demonstrates its assigned playing behavior.

## Learning Outcomes

Through this project, I gained practical experience in:

- Understanding and applying software design patterns.
- Creating abstract classes and implementing inheritance.
- Using polymorphism to support interchangeable behaviors.
- Separating software components to improve maintainability.
- Implementing reusable strategies instead of hardcoding behaviors.
- Organizing Python applications using object-oriented design principles.

## Future Improvements

Future enhancements could include adding more musical instruments, implementing additional playing techniques, and creating an interactive interface that allows users to select instruments and change their playing behaviors.

## Author

**Olufemi Rafael Fadipe**  
B.S. Information Technology  
Florida International University (FIU)

*Developed as part of COP4814 – Component-Based Software Development.*
