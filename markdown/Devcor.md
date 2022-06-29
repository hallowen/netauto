# DEVCOR

## 1. Designing for Maintainability

- Modular Code
- Code Reuse
- Dependency Management

### Functional and NonFunctional Requirements

**Functional requirements** specify what the software should do

- User stories and use cases helps to gather functional requirements.
- Functional requirements needs to be testable in some way.
- Contain only a single functionality

eg: User can access documents via WEBUI
User can create, edit and delete documents.

**NonFunctional requirements** tell how a system should perform.

- These are usually related to the architecture of the system.
- Software product qualities
- It is usually the technical requirements of the system.
- These are usually the quality attributes
- Non functional requirements can span an antire application/system and needs to be considered by all the developers working on the project.

eg: The system must support atleast 10,000 concurrent users.
Users are required to register before they can start using the system.
The system should be available atleast 99 percent of the time.

- Availability
- Backup
- Compliance
- Data Integrity
- Disaster Recovery
- Extensibility
- Functional Stability
- Maintainability
- Observability
- Open Source
- Performance Effeciency
- Portability
- Reliability
- Resilence
- Reponsiveness
- Scalability
- Testability
- Transparency
- Usability

Following are the benefits of having Non-Functional requirements implemented.

- Increased code quality
- Better speed and performance
- Fewer bugs and errors
- More uptime
- Improved security
- Reduced maintenance cost
- Better user experience

Following are some of the best practices when designing a software

- Modular design
- Naming conventions
- Software confgureation management
- Coding standards
- Common toolset
- Object oriented design

**SOLID Principle**
SOLD is an acronym for five software design principles:

1. ***Single responsibility principle***: One class should have only a single reponsibility
2. ***Open-closed principle***: Components like classes, methods etc should be open for exenstion but closed for modificiation
3. ***Liskov's substitution principle***: Derived types must be completely substitutable for their base types
4. ***Interface segregation principle***: Clients should not be forced to depend upon the interfaces they do not use.
5. ***Dependency inversion principle***: Program to an interface, bnot to an implementation. 

***Facade pattern*** is used to implement single responsibility principle.

During the implementation phase

- Major decisions should have been made but can be revisted.
- Consistency and co-ordination within the team are important
- Stick to common tools, languages and techniques.
- Bad implementation decreases application quality.
- Be aware of "Bus Factor"
- Good implementation reduces implementation and maintenance times and lowers the learning curve.

**Common Tools**
- Linters will analyze the code and style the code.
- Adhere to a naming and coding convention.
- Shared libraries and development tools.
- Software configuration management system.

**DRY(Don't Repeat Yourself)**

Maven(JAVA) and NPM(node.js) are the dependency management tools.

**Software Configuration Management** includes the following

- Version Control
- Configuration Control
- Build Management
- Environment Management(System hardware and software, licenses)
- Bug Tracking

Modular software design enforces the following software qualities

- Composability: Ability to combine multiple modules.
- Decomposability
- Understandability
- Continuity
- Protection

High cohesity and loose coupling is preferred.

Dependency injection defines 4 different roles within a domain

1. Service: An object that can be used
2. Client: An entity that uses the said service
3. Interface: Defines how the client may use the service
4. Injector: Constructs the service and injects into thr client.

There are 3 distinct injection methods

- Constructor Injection(Dependencies provided by the constructor)
- Setter Injection(Client exposes the injector method)
- Interface Injection(Interface provides the injector method)

S




