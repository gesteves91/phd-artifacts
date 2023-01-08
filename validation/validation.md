# Ground Truth Validation

These are the nine questions that we asked developers to validate the Organic tool.

| Smell           | Question                                                                                                | Answer |
|-----------------|---------------------------------------------------------------------------------------------------------|--------|
| God Class       | Does the class have more than one responsibility?                                                       | Yes    |
| God Class       | Does the class have functionality that would fit better into other classes?                             | Yes    |
| God Class       | Would splitting up the class improve the overall design?                                                | Yes    |
| Refused Bequest | Does the class use only a little of parent’s behavior?                                                  | Yes    |
| Refused Bequest | Does the class have too many methods that overrides the parent behavior?                                | No     |
| Refused Bequest | Would refactoring the inheritance improve the overall design of this class?                             | Yes    |
| Spaghetti Code  | Is the class well-structured? For instance, would you be able to clearly state what the class is doing? | No     |
| Spaghetti Code  | Is the class difficult to maintain? For instance, are there many conditional branches in the code?      | Yes    |
| Spaghetti Code  | Are most of the methods from this class interacting with other objects?                                 | No     |


These questions were based on:

M. Fowler. 1999. Refactoring: Improving the Design of Existing Code. Addison-Wesley.

W. H. Brown and R. C. Malveau and H. McCormick and T. J. Mowbray. 1998. AntiPatterns: refactoring software, architectures, and projects in crisis. John Wiley & Sons.

J. Schumacher and N. Zazworka and F. Shull and C. B. Seaman and M. A. Shaw. (2010). Building empirical support for automated code smell detection. In: International Symposium on Empirical Software Engineering and Measurement (ESEM). 

M. Lanza and R. Marinescu and S. Ducasse. 2005. Object-Oriented Metrics in Practice. Springer-Verlag.



