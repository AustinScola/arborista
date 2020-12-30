# Arborista
![test](https://github.com/AustinScola/arborista/workflows/Python%20package/badge.svg)

A tree transformation tool.

Specifically, Arborista can be used as a concrete syntax tree transformation tool for bettering
Python code.

## Name Etymology

The name "Arborista" is a combination of the word "arborist", meaning a person who takes care of
trees, and the suffix "ista", meaning a person who is a specialist at something. This is akin to the
word "barista", meaning a person who is a specialist at making coffee.

## Vision

### Short term

The short term vision for Arborista is for it to be run continuously on repositories to generate
improvements. These improvements can be either manually approved by a developer or automatically
tested and then applied.

To make the most of Arborista, developers should tend to Arborista so that Arborista can tend to
their code. In this way, Arborista will serve to multiply their productivity.

The parts of Arborista that need tending to are its transformations and its domain.

In terms of the transformations, that means that poorly configured transformations need to be
modified or removed and new transformations should be added. The following is a process for this:
- If a developer finds themselves denying a proposed application of a transformation, or builds and
tests frequenty do not pass when a tranformation is applied, then the developer should alter or
remove that transformation.
- If the developer finds themselves manually making similar structural changes to the repository in
multiple places, then they should write a transformation to do it for them, and add it to the set of
transformations.

This process is similar to how when a bug is discovered, a test should be written which catches the
bug, then the code should be altered to make all tests pass.

When it comes to the domain of Arborista, developers can add support for new types of tree
structures so that Arborista can tend to more for them.

As the set of transformations becomes better, Arborista will approach equivalence with a developer
who is dedicated full-time to cleaning up code.

### Medium term

In the medium term, software libraries can start to ship with their own set of recommended
transformations for the usage of the library. These transformations can be used on repositories
which use library.

Software libraries could also ship transformations for updating and downgrading between different
versions of the library.

### Long term

In the long term, Arborista will serve as an exploration of the types of transformations which are
considered helpful.

This will aid in fostering an understanding for how to create a more general purpose solution to the
problem of automated software improvement which does not require hard coded transformations. For
example, maybe one which just aims to reduce the number of instructions that are executed on average
while maintaing equivalence of functionality.

### Wild ideas

One wild idea for Arborista is that it could learn from the approval and denial of the application
of transformations as well as the activity of developers in order to propose changes to its own set
of transformations (or change its set of transformations automatically).

Another relatively wild idea would be to include (or write) lexer and parser generators. In addition
to producing lexers and parsers, nodes could also be generated and methods to convert the nodes back
to strings. This would mean that to add support for a computer programming language, (or any
context-free grammer language) only the specification of the language would need to be provided.

Some transformations of one language also make sense in another language, and so these could be
generalized. Transformations of code from one lanaguage to another could also be created, but the
usefullness of these is debatable.
