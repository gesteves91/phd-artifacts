# Complete List of Features

## Class-Level Metrics (60 static metrics - 55/60 Kept)

### Clone Metrics

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

### Cohesion

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| LCOM5   | Lack of Cohesion in Methods 5            | Kept   |

### Complexity

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| NL      | Nesting Level                            | Kept   |
| NLE     | Nesting Level Else-If                    | Kept   |
| WMC     | Weighted Methods per Class               | Kept   |

### Coupling

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| CBO     | Coupling Between Object Classes          | Kept   |
| CBOI    | Coupling Between Object Classes Inverted | Kept   |
| NII     | Number of Incoming Invocations           | Kept   |
| NOI     | Number of Outgoing Invocations           | Kept   |
| RFC     | Response for a Class                     | Kept   |

### Documentation

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

### Inheritance

| Acronym | Feature                                  | Status |
| ------- | ---------------------------------------- | ------ |
| DIT     | Depth of Inheritance Tree                | Kept   |
| NOA     | Number of Ancestors                      | Kept   |
| NOC     | Number of Children                       | Kept   |
| NOD     | Number of Descendants                    | Kept   |
| NOP     | Number of Parents                        | Kept   |

### Size

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

## Removed due to high correlation (over 99%)

| Feature | Correlated Feature |
|---------|--------------------|
| LLDC    | LDC                |
| TCLOC   | CLOC               |
| TNA     | TNPA               |
| TNLPA   | NLPA               |
| TNPA    | NA                 |
