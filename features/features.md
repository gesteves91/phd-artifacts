# Complete List of Features

## Features Categories

### Class-Level

| Type | Acronym | Name                                       |
|------|---------|--------------------------------------------|
| CK   | WMC     | Weighted Method Count                      |
| CK   | DIT     | Depth of Inheritance Tree                  |
| CK   | RFC     | Response for Class                         |
| CK   | NOC     | Number to children                         |
| CK   | CBO     | Coupling Between Objects                   |
| CK   | LCOM    | Lack of Cohesion in Methods                |
| OO   | FanIn   | Number of classes that reference the class |
| OO   | FanOut  | Number of classes referenced by the class  |
| OO   | NOA     | Number of attributes                       |
| OO   | NOPRA   | Number of private attributes               |
| OO   | NOPUA   | Number of public attributes                |
| OO   | NOAI    | Number of attributes inherited             |
| OO   | LOC     | Number of lines of code                    |
| OO   | NOM     | Number of methods                          |
| OO   | NOPM    | Number of public methods                   |
| OO   | NOPRM   | Number of private methods                  |
| OO   | NOMI    | Number of methods inherited                |

### Entropy

| Acronym | Name                                               |
|---------|----------------------------------------------------|
| HCM     | History Complexity Measure                         |
| WHCM    | Weighted History Complexity Measure                |
| LinHCM  | Linearly Decayed History Complexity Measure        |
| LogHCM  | LoGarithmically decayed History Complexity Measure |
| ExpHCM  | Exponentially Decayed History Complexity Measure   |

### Change

| Acronym | Name                                            |
|---------|-------------------------------------------------|
| NR      | Number of revisions                             |
| NREF    | Number of times file has been refactored        |
| NFIX    | Number of times file was involved in bug-fixing |
| NAUTH   | Number of authors who committed the file        |
| LINES   | Lines added and removed (sum, max, average)     |
| CHURN   | Codechurn (sum, maximum and average)            |
| CHGSET  | Change set size (maximum and average)           |
| AGE     | Age and weighted age                            |

### Halstead and McCabe

| Acronym             | Name                                |
|---------------------|-------------------------------------|
| Branch count        | Number of branches                  |
| McCabe's complexity | Number of independent paths         |
| McCabe's design     | Complexity of a module              |
| McCabe's essential  | Degree of structuredness            |
| Halstead content    | Independent complexity of a module  |
| Halstead difficult  | Difficult to handle the module      |
| Halstead level      | Inverse of the error proneness      |
| Halstead effort     | Estimated mental effort             |
| Halstead error      | Number of errors in module          |
| Halstead length     | Operators and operands numbers      |
| Halstead time       | Estimate time to develop module     |
| Halstead volume     | Bits required to execute the module |
| Operands            | Total number of operands            |
| Operators           | Total number of operators           |
| Unique operands     | Number of unique operands           |
| Unique operators    | Number of unique operators          |

### Additional

| Acronym | Name                                          |
|---------|-----------------------------------------------|
| DAM     | Data Access Metric                            |
| MOA     | Measure of Aggregation                        |
| MFA     | Measure of Functional Abstraction             |
| CAM     | Cohesion Among Methods of Class               |
| IC      | Inheritance Coupling                          |
| CBM     | Coupling Between Methods                      |
| AMC     | Average Method Complexity                     |
| Ca      | Afferent couplings                            |
| Ce      | Efferent couplings                            |
| CC      | McCabe's cyclomatic complexity (max and mean) |

## Class-Level Quality Attributes (60 static metrics - 55/60 Kept)

#### Clone

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| CC      | Clone Coverage                           | Kept   |
| CCL     | Clone Classes                            | Kept   |
| CCO     | Clone Complexity                         | Kept   |
| CI      | Clone Instances                          | Kept   |
| CLC     | Clone Line Coverage                      | Kept   |
| CLLC    | Clone Logical Line Coverage              | Kept   |
| LDC     | Lines of Duplicated Code                 | Kept   |
| LLDC    | Logical Lines of Duplicated Code         | Gone   |

#### Cohesion

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| LCOM5   | Lack of Cohesion in Methods 5            | Kept   |

#### Complexity

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| NL      | Nesting Level                            | Kept   |
| NLE     | Nesting Level Else-If                    | Kept   |
| WMC     | Weighted Methods per Class               | Kept   |

#### Coupling

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| CBO     | Coupling Between Object Classes          | Kept   |
| CBOI    | Coupling Between Object Classes Inverted | Kept   |
| NII     | Number of Incoming Invocations           | Kept   |
| NOI     | Number of Outgoing Invocations           | Kept   |
| RFC     | Response for a Class                     | Kept   |

#### Documentation

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| AD      | API Documentation                        | Kept   |
| CD      | Comment Density                          | Kept   |
| CLOC    | Comment Lines of Code                    | Kept   |
| DLOC    | Documentation Lines of Code              | Kept   |
| PDA     | Public Documented API                    | Kept   |
| PUA     | Public Undocumented API                  | Kept   |
| TCD     | Total Comment Density                    | Kept   |
| TCLOC   | Total Comment Lines of Code              | Gone   |

#### Inheritance

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| DIT     | Depth of Inheritance Tree                | Kept   |
| NOA     | Number of Ancestors                      | Kept   |
| NOC     | Number of Children                       | Kept   |
| NOD     | Number of Descendants                    | Kept   |
| NOP     | Number of Parents                        | Kept   |

#### Size

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| LLOC    | Logical Lines of Code                    | Kept   |
| LOC     | Lines of Code                            | Kept   |
| NA      | Number of Attributes                     | Kept   |
| NG      | Number of Getters                        | Kept   |
| NLA     | Number of Local Attributes               | Kept   |
| NLG     | Number of Local Getters                  | Kept   |
| NLM     | Number of Local Methods                  | Kept   |
| NLPA    | Number of Local Public Attributes        | Kept   |
| NLPM    | Number of Local Public Methods           | Kept   |
| NLS     | Number of Local Setters                  | Kept   |
| NM      | Number of Methods                        | Kept   |
| NOS     | Number of Statements                     | Kept   |
| NPA     | Number of Public Attributes              | Kept   |
| NPM     | Number of Public Methods                 | Kept   |
| NS      | Number of Setters                        | Kept   |
| TLLOC   | Total Logical Lines of Code              | Kept   |
| TLOC    | Total Lines of Code                      | Kept   |
| TNG     | Total Number of Getters                  | Kept   |
| TNLA    | Total Number of Local Attributes         | Kept   |
| TNLG    | Total Number of Local Getters            | Kept   |
| TNLM    | Total Number of Local Methods            | Kept   |
| TNLPM   | Total Number of Local Public Methods     | Kept   |
| TNLS    | Total Number of Local Setters            | Kept   |
| TNM     | Total Number of Methods                  | Kept   |
| TNOS    | Total Number of Statements               | Kept   |
| TNPM    | Total Number of Public Methods           | Kept   |
| TNS     | Total Number of Setters                  | Kept   |
| TNA     | Total Number of Attributes               | Gone   |
| TNLPA   | Total Number of Local Public Attributes  | Gone   |
| TNPA    | Total Number of Public Attributes        | Gone   |

#### Removed due to high correlation (over 99%)

| Feature | Correlated Feature |
|---------|--------------------|
| LLDC    | LDC                |
| TCLOC   | CLOC               |
| TNA     | TNPA               |
| TNLPA   | NLPA               |
| TNPA    | NA                 |
