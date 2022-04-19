# Translation-Project-Accelerator

Currently a prototype.

# How to run it

1. Create a `TigerGraph` Database at `Cloud` or `local`
2. Change the below connection information at `init_data.py` and `/server/app.py`
   ```
   server = 'https://{your TigerGraph Server}'
   ```
3. Create your virtualenv and activate it.
4. Install the required referrences with `requirements.txt`
   ```
    pip install -r requirements.txt
   ```
5. Install `Spacy` model
   ```
   python3 -m spacy download en_core_web_sm
   ```
6. Run `init_data.py` to insert init data into `TigerGraph` database.
   ```
   python3 init_data.py
   ```
7. Create and install query at your `TigerGraph` database with `my_custom.tg_jaccard_nbor_ss.gsql`, Note: the query name MUST be `tg_jaccard_nbor_ss`
8. go to `./server` directory and run below command to start backend server
   ```
    flask run
   ```
9. go to `./client` directory and run below command to start frontend server
   ```
    yarn start
   ```

# Test Data for Demo

## Find Matched Translator

Book name:

```
C# 10 in a Nutshell
```

Table of contents:

```
Preface
Intended Audience
How This Book Is Organized
What You Need to Use This Book
Conventions Used in This Book
Using Code Examples
O’Reilly Online Learning
How to Contact Us
Acknowledgments
1. Introducing C# and .NET
Object Orientation
Type Safety
Memory Management
Platform Support
CLRs, BCLs, and Runtimes
Common Language Runtime
Base Class Library
Runtimes
Niche Runtimes
A Brief History of C#
What’s New in C# 10
What’s New in C# 9.0
What’s New in C# 8.0
What’s New in C# 7.x
What’s New in C# 6.0
What’s New in C# 5.0
What’s New in C# 4.0
What’s New in C# 3.0
What’s New in C# 2.0
2. C# Language Basics
A First C# Program
Compilation
Syntax
Identifiers and Keywords
Literals, Punctuators, and Operators
Comments
Type Basics
Predefined Type Examples
Custom Types
Types and Conversions
Value Types Versus Reference Types
Predefined Type Taxonomy
Numeric Types
Numeric Literals
Numeric Conversions
Arithmetic Operators
Increment and Decrement Operators
Specialized Operations on Integral Types
8- and 16-Bit Integral Types
Special Float and Double Values
double Versus decimal
Real Number Rounding Errors
Boolean Type and Operators
bool Conversions
Equality and Comparison Operators
Conditional Operators
Strings and Characters
Char Conversions
String Type
Arrays
Default Element Initialization
Indices and Ranges
Multidimensional Arrays
Simplified Array Initialization Expressions
Bounds Checking
Variables and Parameters
The Stack and the Heap
Definite Assignment
Default Values
Parameters
Ref Locals
Ref Returns
var—Implicitly Typed Local Variables
Target-Typed new Expressions
Expressions and Operators
Primary Expressions
Void Expressions
Assignment Expressions
Operator Precedence and Associativity
Operator Table
Null Operators
Null-Coalescing Operator
Null-Coalescing Assignment Operator
Null-Conditional Operator
Statements
Declaration Statements
Expression Statements
Selection Statements
Iteration Statements
Jump Statements
Miscellaneous Statements
Namespaces
File-Scoped Namespaces (C# 10)
The using Directive
The global using Directive (C# 10)
using static
Rules Within a Namespace
Aliasing Types and Namespaces
Advanced Namespace Features
3. Creating Types in C#
Classes
Fields
Constants
Methods
Instance Constructors
Deconstructors
Object Initializers
The this Reference
Properties
Indexers
Static Constructors
Static Classes
Finalizers
Partial Types and Methods
The nameof operator
Inheritance
Polymorphism
Casting and Reference Conversions
Virtual Function Members
Abstract Classes and Abstract Members
Hiding Inherited Members
Sealing Functions and Classes
The base Keyword
Constructors and Inheritance
Overloading and Resolution
The object Type
Boxing and Unboxing
Static and Runtime Type Checking
The GetType Method and typeof Operator
The ToString Method
Object Member Listing
Structs
Struct Construction Semantics
Read-Only Structs and Functions
Ref Structs
Access Modifiers
Examples
Friend Assemblies
Accessibility Capping
Restrictions on Access Modifiers
Interfaces
Extending an Interface
Explicit Interface Implementation
Implementing Interface Members Virtually
Reimplementing an Interface in a Subclass
Interfaces and Boxing
Default Interface Members
Enums
Enum Conversions
Flags Enums
Enum Operators
Type-Safety Issues
Nested Types
Generics
Generic Types
Why Generics Exist
Generic Methods
Declaring Type Parameters
typeof and Unbound Generic Types
The default Generic Value
Generic Constraints
Subclassing Generic Types
Self-Referencing Generic Declarations
Static Data
Type Parameters and Conversions
Covariance
Contravariance
C# Generics Versus C++ Templates
4. Advanced C#
Delegates
Writing Plug-In Methods with Delegates
Instance and Static Method Targets
Multicast Delegates
Generic Delegate Types
The Func and Action Delegates
Delegates Versus Interfaces
Delegate Compatibility
Events
Standard Event Pattern
Event Accessors
Event Modifiers
Lambda Expressions
Explicitly Specifying Lambda Parameter and Return Types
Capturing Outer Variables
Lambda Expressions Versus Local Methods
Anonymous Methods
try Statements and Exceptions
The catch Clause
The finally Block
Throwing Exceptions
Key Properties of System.Exception
Common Exception Types
The TryXXX Method Pattern
Alternatives to Exceptions
Enumeration and Iterators
Enumeration
Collection Initializers
Iterators
Iterator Semantics
Composing Sequences
Nullable Value Types
Nullable<T> Struct
Implicit and Explicit Nullable Conversions
Boxing and Unboxing Nullable Values
Operator Lifting
bool? with & and | Operators
Nullable Value Types and Null Operators
Scenarios for Nullable Value Types
Alternatives to Nullable Value Types
Nullable Reference Types
The Null-Forgiving Operator
Separating the Annotation and Warning Contexts
Treating Nullable Warnings as Errors
Extension Methods
Extension Method Chaining
Ambiguity and Resolution
Anonymous Types
Tuples
Naming Tuple Elements
ValueTuple.Create
Deconstructing Tuples
Equality Comparison
The System.Tuple classes
Records
Background
Defining a Record
Nondestructive Mutation
Property Validation
Calculated Fields and Lazy Evaluation
Primary Constructors
Records and Equality Comparison
Patterns
var Pattern
Constant Pattern
Relational Patterns
Pattern Combinators
Tuple and Positional Patterns
Property Patterns
Attributes
Attribute Classes
Named and Positional Attribute Parameters
Applying Attributes to Assemblies and Backing Fields
Applying Attributes to Lambda Expressions (C# 10)
Specifying Multiple Attributes
Caller Info Attributes
CallerArgumentExpression (C# 10)
Dynamic Binding
Static Binding Versus Dynamic Binding
Custom Binding
Language Binding
RuntimeBinderException
Runtime Representation of Dynamic
Dynamic Conversions
var Versus dynamic
Dynamic Expressions
Dynamic Calls Without Dynamic Receivers
Static Types in Dynamic Expressions
Uncallable Functions
Operator Overloading
Operator Functions
Overloading Equality and Comparison Operators
Custom Implicit and Explicit Conversions
Overloading true and false
Unsafe Code and Pointers
Pointer Basics
Unsafe Code
The fixed Statement
The Pointer-to-Member Operator
The stackalloc Keyword
Fixed-Size Buffers
void*
Native-Sized Integers
Function Pointers
[SkipLocalsInit]
Preprocessor Directives
Conditional Attributes
Pragma Warning
XML Documentation
Standard XML Documentation Tags
User-Defined Tags
Type or Member Cross-References
5. .NET Overview
.NET Standard
.NET Standard 2.0
.NET Standard 2.1
Older .NET Standards
.NET Framework and .NET 6 Compatibility
Runtime and C# Language Versions
Reference Assemblies
The CLR and BCL
System Types
Text Processing
Collections
Querying
XML and JSON
Diagnostics
Concurrency and Asynchrony
Streams and Input/Output
Networking
Assemblies, Reflection, and Attributes
Dynamic Programming
Cryptography
Advanced Threading
Parallel Programming
Span<T> and Memory<T>
Native and COM Interoperability
Regular Expressions
Serialization
The Roslyn Compiler
Application Layers
ASP.NET Core
Windows Desktop
UWP and WinUI 3
MAUI
6. .NET Fundamentals
String and Text Handling
Char
String
Comparing Strings
StringBuilder
Text Encodings and Unicode
Dates and Times
TimeSpan
DateTime and DateTimeOffset
DateOnly and TimeOnly
DateTime and Time Zones
DateTimeOffset and Time Zones
TimeZoneInfo
Daylight Saving Time and DateTime
Formatting and Parsing
ToString and Parse
Format Providers
Standard Format Strings and Parsing Flags
Numeric Format Strings
NumberStyles
Date/Time Format Strings
DateTimeStyles
Enum Format Strings
Other Conversion Mechanisms
Convert
XmlConvert
Type Converters
BitConverter
Globalization
Globalization Checklist
Testing
Working with Numbers
Conversions
Math
BigInteger
Half
Complex
Random
BitOperations
Enums
Enum Conversions
Enumerating Enum Values
How Enums Work
The Guid Struct
Equality Comparison
Value Versus Referential Equality
Standard Equality Protocols
Equality and Custom Types
Order Comparison
IComparable
< and >
Implementing the IComparable Interfaces
Utility Classes
Console
Environment
Process
AppContext
7. Collections
Enumeration
IEnumerable and IEnumerator
IEnumerable<T> and IEnumerator<T>
Implementing the Enumeration Interfaces
The ICollection and IList Interfaces
ICollection<T> and ICollection
IList<T> and IList
IReadOnlyCollection<T> and IReadOnlyList<T>
The Array Class
Construction and Indexing
Enumeration
Length and Rank
Searching
Sorting
Reversing Elements
Copying
Converting and Resizing
Lists, Queues, Stacks, and Sets
List<T> and ArrayList
LinkedList<T>
Queue<T> and Queue
Stack<T> and Stack
BitArray
HashSet<T> and SortedSet<T>
Dictionaries
IDictionary<TKey,TValue>
IDictionary
Dictionary<TKey,TValue> and Hashtable
OrderedDictionary
ListDictionary and HybridDictionary
Sorted Dictionaries
Customizable Collections and Proxies
Collection<T> and CollectionBase
KeyedCollection<TKey,TItem> and DictionaryBase
ReadOnlyCollection<T>
Immutable Collections
Creating Immutable Collections
Manipulating Immutable Collections
Builders
Immutable Collections and Performance
Plugging in Equality and Order
IEqualityComparer and EqualityComparer
IComparer and Comparer
StringComparer
IStructuralEquatable and IStructuralComparable
8. LINQ Queries
Getting Started
Fluent Syntax
Chaining Query Operators
Composing Lambda Expressions
Natural Ordering
Other Operators
Query Expressions
Range Variables
Query Syntax Versus SQL Syntax
Query Syntax Versus Fluent Syntax
Mixed-Syntax Queries
Deferred Execution
Reevaluation
Captured Variables
How Deferred Execution Works
Chaining Decorators
How Queries Are Executed
Subqueries
Subqueries and Deferred Execution
Composition Strategies
Progressive Query Building
The into Keyword
Wrapping Queries
Projection Strategies
Object Initializers
Anonymous Types
The let Keyword
Interpreted Queries
How Interpreted Queries Work
Combining Interpreted and Local Queries
AsEnumerable
EF Core
EF Core Entity Classes
DbContext
Object Tracking
Change Tracking
Navigation Properties
Deferred Execution
Building Query Expressions
Delegates Versus Expression Trees
Expression Trees
9. LINQ Operators
Overview
Sequence→Sequence
Sequence→Element or Value
Void→Sequence
Filtering
Where
Take, TakeLast, Skip, and SkipLast
TakeWhile and SkipWhile
Distinct and DistinctBy
Projecting
Select
SelectMany
Joining
Join and GroupJoin
The Zip Operator
Ordering
OrderBy, OrderByDescending, ThenBy, and ThenByDescending
Grouping
GroupBy
Chunk
Set Operators
Concat, Union, and UnionBy
Intersect, Intersect By, Except, and ExceptBy
Conversion Methods
OfType and Cast
ToArray, ToList, ToDictionary, ToHashSet, and ToLookup
AsEnumerable and AsQueryable
Element Operators
First, Last, and Single
ElementAt
MinBy and MaxBy
DefaultIfEmpty
Aggregation Methods
Count and LongCount
Min and Max
Sum and Average
Aggregate
Quantifiers
Contains and Any
All and SequenceEqual
Generation Methods
Empty
Range and Repeat
10. LINQ to XML
Architectural Overview
What Is a DOM?
The LINQ to XML DOM
X-DOM Overview
Loading and Parsing
Saving and Serializing
Instantiating an X-DOM
Functional Construction
Specifying Content
Automatic Deep Cloning
Navigating and Querying
Child Node Navigation
Parent Navigation
Peer Node Navigation
Attribute Navigation
Updating an X-DOM
Simple Value Updates
Updating Child Nodes and Attributes
Updating Through the Parent
Working with Values
Setting Values
Getting Values
Values and Mixed Content Nodes
Automatic XText Concatenation
Documents and Declarations
XDocument
XML Declarations
Names and Namespaces
Namespaces in XML
Specifying Namespaces in the X-DOM
The X-DOM and Default Namespaces
Prefixes
Annotations
Projecting into an X-DOM
Eliminating Empty Elements
Streaming a Projection
11. Other XML and JSON Technologies
XmlReader
Reading Nodes
Reading Elements
Reading Attributes
Namespaces and Prefixes
XmlWriter
Writing Attributes
Writing Other Node Types
Namespaces and Prefixes
Patterns for Using XmlReader/XmlWriter
Working with Hierarchical Data
Mixing XmlReader/XmlWriter with an X-DOM
Working with JSON
Utf8JsonReader
Utf8JsonWriter
JsonDocument
JsonNode
12. Disposal and Garbage Collection
IDisposable, Dispose, and Close
Standard Disposal Semantics
When to Dispose
Clearing Fields in Disposal
Anonymous Disposal
Automatic Garbage Collection
Roots
Finalizers
Calling Dispose from a Finalizer
Resurrection
How the GC Works
Optimization Techniques
Forcing Garbage Collection
Tuning Garbage Collection at Runtime
Memory Pressure
Array Pooling
Managed Memory Leaks
Timers
Diagnosing Memory Leaks
Weak References
Weak References and Caching
Weak References and Events
13. Diagnostics
Conditional Compilation
Conditional Compilation Versus Static Variable Flags
The Conditional Attribute
Debug and Trace Classes
Fail and Assert
TraceListener
Flushing and Closing Listeners
Debugger Integration
Attaching and Breaking
Debugger Attributes
Processes and Process Threads
Examining Running Processes
Examining Threads in a Process
StackTrace and StackFrame
Windows Event Logs
Writing to the Event Log
Reading the Event Log
Monitoring the Event Log
Performance Counters
Enumerating the Available Counters
Reading Performance Counter Data
Creating Counters and Writing Performance Data
The Stopwatch Class
Cross-Platform Diagnostic Tools
dotnet-counters
dotnet-trace
dotnet-dump
14. Concurrency and Asynchrony
Introduction
Threading
Creating a Thread
Join and Sleep
Blocking
Local Versus Shared State
Locking and Thread Safety
Passing Data to a Thread
Exception Handling
Foreground Versus Background Threads
Thread Priority
Signaling
Threading in Rich Client Applications
Synchronization Contexts
The Thread Pool
Tasks
Starting a Task
Returning values
Exceptions
Continuations
TaskCompletionSource
Task.Delay
Principles of Asynchrony
Synchronous Versus Asynchronous Operations
What Is Asynchronous Programming?
Asynchronous Programming and Continuations
Why Language Support Is Important
Asynchronous Functions in C#
Awaiting
Writing Asynchronous Functions
Asynchronous Lambda Expressions
Asynchronous Streams
Asynchronous Methods in WinRT
Asynchrony and Synchronization Contexts
Optimizations
Asynchronous Patterns
Cancellation
Progress Reporting
The Task-Based Asynchronous Pattern
Task Combinators
Asynchronous Locking
Obsolete Patterns
Asynchronous Programming Model
Event-Based Asynchronous Pattern
BackgroundWorker
15. Streams and I/O
Stream Architecture
Using Streams
Reading and Writing
Seeking
Closing and Flushing
Timeouts
Thread Safety
Backing Store Streams
FileStream
MemoryStream
PipeStream
BufferedStream
Stream Adapters
Text Adapters
Binary Adapters
Closing and Disposing Stream Adapters
Compression Streams
Compressing in Memory
Unix gzip File Compression
Working with ZIP Files
File and Directory Operations
The File Class
The Directory Class
FileInfo and DirectoryInfo
Path
Special Folders
Querying Volume Information
Catching Filesystem Events
OS Security
Running in a Standard User Account
Administrative Elevation and Virtualization
Memory-Mapped Files
Memory-Mapped Files and Random File I/O
Memory-Mapped Files and Shared Memory (Windows)
Cross-Platform Interprocess Shared Memory
Working with View Accessors
16. Networking
Network Architecture
Addresses and Ports
URIs
HttpClient
GetAsync and Response Messages
SendAsync and Request Messages
Uploading Data and HttpContent
HttpMessageHandler
Proxies
Authentication
Headers
Query Strings
Uploading Form Data
Cookies
Writing an HTTP Server
Using DNS
Sending Mail with SmtpClient
Using TCP
Concurrency with TCP
Receiving POP3 Mail with TCP
17. Assemblies
What’s in an Assembly
The Assembly Manifest
The Application Manifest (Windows)
Modules
The Assembly Class
Strong Names and Assembly Signing
How to Strongly Name an Assembly
Assembly Names
Fully Qualified Names
The AssemblyName Class
Assembly Informational and File Versions
Authenticode Signing
How to Sign with Authenticode
Resources and Satellite Assemblies
Directly Embedding Resources
.resources Files
.resx Files
Satellite Assemblies
Cultures and Subcultures
Loading, Resolving, and Isolating Assemblies
Assembly Load Contexts
The Default ALC
The “Current” ALC
Assembly.Load and Contextual ALCs
Loading and Resolving Unmanaged Libraries
AssemblyDependencyResolver
Unloading ALCs
The Legacy Loading Methods
Writing a Plug-In System
18. Reflection and Metadata
Reflecting and Activating Types
Obtaining a Type
Type Names
Base Types and Interfaces
Instantiating Types
Generic Types
Reflecting and Invoking Members
Member Types
C# Members Versus CLR Members
Generic Type Members
Dynamically Invoking a Member
Method Parameters
Using Delegates for Performance
Accessing Nonpublic Members
Generic Methods
Anonymously Calling Members of a Generic Interface
Reflecting Assemblies
Modules
Working with Attributes
Attribute Basics
The AttributeUsage Attribute
Defining Your Own Attribute
Retrieving Attributes at Runtime
Dynamic Code Generation
Generating IL with DynamicMethod
The Evaluation Stack
Passing Arguments to a Dynamic Method
Generating Local Variables
Branching
Instantiating Objects and Calling Instance Methods
Exception Handling
Emitting Assemblies and Types
The Reflection.Emit Object Model
Emitting Type Members
Emitting Methods
Emitting Fields and Properties
Emitting Constructors
Attaching Attributes
Emitting Generic Methods and Types
Defining Generic Methods
Defining Generic Types
Awkward Emission Targets
Uncreated Closed Generics
Circular Dependencies
Parsing IL
Writing a Disassembler
19. Dynamic Programming
The Dynamic Language Runtime
Numeric Type Unification
Dynamic Member Overload Resolution
Simplifying the Visitor Pattern
Anonymously Calling Members of a Generic Type
Implementing Dynamic Objects
DynamicObject
ExpandoObject
Interoperating with Dynamic Languages
Passing State Between C# and a Script
20. Cryptography
Overview
Windows Data Protection
Hashing
Hash Algorithms in .NET
Hashing Passwords
Symmetric Encryption
Encrypting in Memory
Chaining Encryption Streams
Disposing Encryption Objects
Key Management
Public-Key Encryption and Signing
The RSA Class
Digital Signing
21. Advanced Threading
Synchronization Overview
Exclusive Locking
The lock Statement
Monitor.Enter and Monitor.Exit
Choosing the Synchronization Object
When to Lock
Locking and Atomicity
Nested Locking
Deadlocks
Performance
Mutex
Locking and Thread Safety
Thread Safety and .NET Types
Thread Safety in Application Servers
Immutable Objects
Nonexclusive Locking
Semaphore
Reader/Writer Locks
Signaling with Event Wait Handles
AutoResetEvent
ManualResetEvent
CountdownEvent
Creating a Cross-Process EventWaitHandle
Wait Handles and Continuations
WaitAny, WaitAll, and SignalAndWait
The Barrier Class
Lazy Initialization
Lazy<T>
LazyInitializer
Thread-Local Storage
[ThreadStatic]
ThreadLocal<T>
GetData and SetData
AsyncLocal<T>
Timers
PeriodicTimer
Multithreaded Timers
Single-Threaded Timers
22. Parallel Programming
Why PFX?
PFX Concepts
PFX Components
When to Use PFX
PLINQ
Parallel Execution Ballistics
PLINQ and Ordering
PLINQ Limitations
Example: Parallel Spellchecker
Functional Purity
Setting the Degree of Parallelism
Cancellation
Optimizing PLINQ
The Parallel Class
Parallel.Invoke
Parallel.For and Parallel.ForEach
Task Parallelism
Creating and Starting Tasks
Waiting on Multiple Tasks
Canceling Tasks
Continuations
Task Schedulers
TaskFactory
Working with AggregateException
Flatten and Handle
Concurrent Collections
IProducerConsumerCollection<T>
ConcurrentBag<T>
BlockingCollection<T>
Writing a Producer/Consumer Queue
23. Span<T> and Memory<T>
Spans and Slicing
CopyTo and TryCopyTo
Working with Text
Memory<T>
Forward-Only Enumerators
Working with Stack-Allocated and Unmanaged Memory
24. Native and COM Interoperability
Calling into Native DLLs
Type and Parameter Marshaling
Marshaling Common Types
Marshaling Classes and Structs
In and Out Marshaling
Calling Conventions
Callbacks from Unmanaged Code
Callbacks with Function Pointers
Callbacks with Delegates
Simulating a C Union
Shared Memory
Mapping a Struct to Unmanaged Memory
fixed and fixed {...}
COM Interoperability
The Purpose of COM
The Basics of the COM Type System
Calling a COM Component from C#
Optional Parameters and Named Arguments
Implicit ref Parameters
Indexers
Dynamic Binding
Embedding Interop Types
Type Equivalence
Exposing C# Objects to COM
Enabling Registry-Free COM
25. Regular Expressions
Regular Expression Basics
Compiled Regular Expressions
RegexOptions
Character Escapes
Character Sets
Quantifiers
Greedy Versus Lazy Quantifiers
Zero-Width Assertions
Lookahead and Lookbehind
Anchors
Word Boundaries
Groups
Named Groups
Replacing and Splitting Text
MatchEvaluator Delegate
Splitting Text
Cookbook Regular Expressions
Recipes
Regular Expressions Language Reference
Index
About the Authors
```

## Help in Translation

No need
