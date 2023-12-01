# Functions and I-P-O-A Workflow
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

## Testing
Testing is the process of evaluating a system or its component(s) with the intent to find whether it satisfies the specified requirements or not. Testing is executing a system in order to identify any gaps, errors, or missing requirements in contrary to the actual requirements.

**Unit Testing**
Unit testing is a software testing method by which individual units of source code are tested to determine whether they are fit for use. A unit is the smallest testable part of any software. This units could be considered as `functions`, `methods`, `classes`, etc.


**Test Driven Development (TDD)**
There is a methodology called TDD (Test Driven Development) that consists of writing the tests before the code. This helps to write the code with a clear goal in mind and to avoid over-engineering. With TDD we can `adjust` the `process` of our `functions` so they can produce the `output` that we expect.

TDD is the key point where we `manually` adjust the process of our `functions` so with the base `input`, we generate the `output` that we expect. Its a mechanism of `adjustment` of our functions.

## I-P-O-A Workflow
**Static/Declarative Approach**
We can see a pattern in this process of `adjustment` of our functions. There are 2 main process:
- **Execution**: The process of our function that takes the `input` (`I`), applies the `process` (`P`) and generates the `output` (`O`).
- **Adjustment**: The process where if the `output` is not the `expected`, we manually apply an `adjustment` (`A`) the `process` of our function. Acts as feedback

Here a diagram of this process:
```mermaid
flowchart LR
    %% Entities
    I[Input]
    P[Process]
    O[Output]
    E[Expected]
    A{Adjustment}

    %% Sub-Graphs
    subgraph Adjustment
        E
        A
    end

    subgraph Execution
        I
        P
        O
    end

    %% Connections
    I --> P
    P --> O
    O -- comparison --- E

    E --- A
    A -- manual --- P
```

**Dynamic Approach**
We can stablish a parallelism between this process and what `neural networks`, with the difference, this `adjustment` is done not `manually` but `dynamically`
- **Forward Propagation**: The process of our neural network that takes the `input`, applies the `process` (vía `activation functions`) and generates the `output`.
- **Backwards Propagation**: The process where if the `output` is not the `expected` (based on the `loss function`) we dynamically adjust the `process` of our neural network (vía `weights` and `biases`). Acts as feedback.

Here is a diagram in mermaid.js that illustrates all the components of a neural network:
```mermaid
graph LR
%% Backward Propagation
%% - Entities
I_BP([S]):::style_bp
E_BP([E]):::style_bp
Loss_Function[Loss Function]:::style_bp
Loss_Function_Explained[[
    explanation:
    - actual: current activation value \ output
    - expected: expected activation value
    
    loss = actual - expected

    functions:
    - mean squared error
    - cross entropy
]]:::style_bp
Optimizer_Function[Optimizer Function]:::style_bp
Optimizer_Function_Explained[[
    explanation:
    adjust the weights and biases of the model

    optimizers functions
    - gradient descent
    - stochastic gradient descent
    - mini-batch gradient descent
]]:::style_bp

%% - Subgraph
subgraph BACKWARD_PROPAGATION[Backward Propagation]
    direction LR
    I_BP
    E_BP
    Loss_Function
    Loss_Function_Explained
    Optimizer_Function
    Optimizer_Function_Explained
end

%% - Connections
E_BP --- Optimizer_Function
Optimizer_Function --- Optimizer_Function_Explained
Optimizer_Function_Explained --- Loss_Function
Loss_Function --- Loss_Function_Explained
Loss_Function_Explained --- I_BP



%% Forward Propagation
%% - Entities
I_FP([S]):::style_fp
E_FP([E]):::style_fp
Activation_Function[Activation Function]:::style_fp
Activation_Function_Explained[[
    explanation:
    - weighted sum: calculate the weighted sum of the neuron based on the weights and biases with other neurons
    - activation function: apply an activation function to the weighted sum to cal

    functions
    - sigmoid
    - tanh
    - relu
]]:::style_fp

%% - Subgraph
subgraph FORWARD_PROPAGATION[Forward Propagation]
    direction LR
    I_FP
    E_FP
    Activation_Function
    Activation_Function_Explained
end

%% - Connections
I_FP --> Activation_Function
Activation_Function --- Activation_Function_Explained
Activation_Function_Explained --> E_FP

%% Neural Network Model
%% - Components / Entities
N1_LYI[Neuron + BIAS]
N2_LYI[Neuron + BIAS]
N3_LYI[Neuron + BIAS]
N4_LYI[Neuron + BIAS]
N5_LYI[Neuron + BIAS]
N6_LYI[Neuron + BIAS]
N7_LYI[Neuron + BIAS]
N8_LYI[Neuron + BIAS]

N1_LYH[Neuron + BIAS]
N2_LYH[Neuron + BIAS]
N3_LYH[Neuron + BIAS]
N4_LYH[Neuron + BIAS]

N1_LYO[Neuron + BIAS]
N2_LYO[Neuron + BIAS]

%% - Subgraph
subgraph NEURAL_NETWORK[Neural Network]
    direction LR
    subgraph INPUT_LAYER[Input Layer]
        N1_LYI
        N2_LYI
        N3_LYI
        N4_LYI
        N5_LYI
        N6_LYI
        N7_LYI
        N8_LYI
    end

    subgraph HIDDEN_LAYER[Hidden Layer]
        N1_LYH
        N2_LYH
        N3_LYH
        N4_LYH
    end

    subgraph OUTPUT_LAYER[Output Layer]
        N1_LYO
        N2_LYO
    end
end

%% - Connections
%% Synapses
N1_LYI -..-|Weight 0.25| N1_LYH
N2_LYI -..-|Weight 0.50| N1_LYH
N3_LYI -..-|Weight 0.75| N1_LYH

N3_LYI -..-|Weight 0.25| N2_LYH
N4_LYI -..-|Weight 0.50| N2_LYH
N5_LYI -..-|Weight 0.75| N2_LYH

N5_LYI -..-|Weight 0.25| N3_LYH
N6_LYI -..-|Weight 0.50| N3_LYH
N7_LYI -..-|Weight 0.75| N3_LYH

N7_LYI -..-|Weight 0.25| N4_LYH
N8_LYI -..-|Weight 0.50| N4_LYH

N1_LYH -..-|Weight 0.25| N1_LYO
N2_LYH -..-|Weight 0.50| N1_LYO

N3_LYH -..-|Weight 0.25| N2_LYO
N4_LYH -..-|Weight 0.50| N2_LYO

%% Styles
classDef style_fp stroke:#4bcc94
classDef style_bp stroke:#4b9bcc
```