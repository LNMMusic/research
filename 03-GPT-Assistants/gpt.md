# Write instructions on GPT Assistant as functions

## Functions
In programming languages such as C++, Rust, Golang, Python, NodeJS, etc, functions are blocks of code that perform a specific task. This allows to encapsulate code and reuse it in different parts of the program. It helps with the principles of DRY (Don't Repeat Yourself) and KISS (Keep It Simple Stupid).

**Elements**
- Input: The input of the function. It can be zero or more parameters.
- Process: The logic of the function that performs the task (based on the input)
- Output: The output of the function. It can be zero or more parameters.

**Advantages**
- SRP: Functions help to follow the Single Responsibility Principle. Each function should perform a single task.
- Reusability: Functions can be reused in different parts of the program.
- Modularity: Functions can be used to break down a complex program into smaller and simpler modules.
- Abstraction: Functions can be used to hide the implementation details of a program.
- Maintainability: Functions help to make the code more readable and maintainable.

**Declaration**
> JavaScript (ES6)
```js
// Function declaration
function functionName(parameter1, parameter2, ...) {
  // Code to be executed
}
```

> Python
```py
# Function declaration
def functionName(parameter1:str, parameter2:str, ...):
  # Code to be executed
```

> Golang
```go
// Function declaration
func functionName(parameter1, parameter2 string) (return1, return2 string) {
    // Code to be executed
    return "return1", "return2"
}
```

---

## Write instructions on GPT
The main reason why using GPT Engines is because they can apply NLP interpretation and Code interpretation (which requires a huge amount of training). This dynamic allow us to create function where the applied process is not as straightforward as a simple addition, and the data must be analized and interpreted in complex ways, where using programming languages would be a huge challenge.

Example: analizing an string to detect certain patterns of NLP in a phrase. We can't just use tons of `if` statements to detect all the possible patterns. We might think on using Regex, but we can take a more flexible approach using NLP, a better engine for this task.

With the new update of custom GPT assistant, we can use this GPT engines as programming languages to declare our own functionalities, via instructions. We can declare this instructions as if we were writing a function, with the key difference that our declaration is not based on strict syntax, but using NLP (Natural Language Processing).

### Title and Description
The title and description of the task to be performed.

### Input
The input of the function.

We should specify the format and the parameters.
Format:
- custom
- golang
- python
- json

Examples:
- custom
```custom
Parameters:
- Number: float
- Schema: type Schema {
  Field1 <primitive type>
  Field2 <primitive type>
  Field3 <primitive type>
}
```

- golang
```go
var Number float
var Schema struct {
  Field1 any
  Field2 any
  Field3 any
}
```

- python
```py
Number:float = 0
Schema = {
  "Field1": any,
  "Field2": any,
  "Field3": any
}
```

- json (not a programming language, but useful for examples of schemes)
```json
{
  "number": 0,
  "schema": {
    "field1": null,
    "field2": null,
    "field3": null
  }
}
```

### Process
The logic of the function that performs the task (based on the input). It can be written as a list of instructions or set of rules.
In the rules you can specify `conditions`, `errors`, `types of procedures` (such as using NLP Intepreter or Code Interpreter), and many more topics.

### Output
The output of the function.
- primitive types: string, int, float, bool, etc.
- complex types: schemes, structs, classes, etc.

### Examples
You can provide GPT Assistant with examples of the input and the expected output to guide the model a bit more (similar to TDD in testing or Backpropagation in Neural Networks)

---

## Instruction Template
```md
## GPT Title
This GPT Assistant ...

### Input
Format: json, golang, python, custom

Parameters:
- primitive types: string, int, float, bool, etc.
- complex types: schemes, structs, classes, etc.

### Process
Description of the logic process of the function.

Rules:
- ...
- ...
- ...

### Output
Format: json, golang, python, custom

Parameters:
- primitive output: string, int, float, bool, etc.
- complex output: schemes, structs, classes, etc.

### Examples
**Example 1**
- Input: ...
- Expected Output: ...

**Example 2**
- Input: ...
- Expected Output: ...
```

---

## Instruction Template - Sum Function Example
```md
## Sum Function
This GPT Assistant takes 2 float and returns the sum of them.

### Input
Format: json

Parameters:
{
  "Number1": float,
  "Number2": float
}

### Process
GPT Assistant takes the 2 float and applies the addition between them.

Rules:
- If at least one of the float is negative, throw an error.
- If at least one of the float is greater than 100, throw an error.

### Output
Format: json

Parameters:
{
  "Result": float,
  "Error": string
}

Format: json

### Examples
**Example 1**
- Input: {"Number1": 2, "Number2": 2}
- Expected Output: {"Result": 4, "Error": null}

**Example 2**
- Input: {"Number1": 2, "Number2": -2}
- Expected Output: {"Result": null, "Error": "Negative numbers are not allowed"}

**Example 3**
- Input: {"Number1": 2, "Number2": 101}
- Expected Output: {"Result": null, "Error": "Numbers greater than 100 are not allowed"}
```