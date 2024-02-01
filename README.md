# DECIDE
### INTERCEPTOR MISSILE LAUNCH DECISION SYSTEM

A program for deciding whether to launch an interceptor missile based on several factors.

This program judges if a interceptor missile should be launched given several factors, given 
as input to the program. The program will take the given input and print either "YES\n" or 
"NO\n" to stdout indicating whether an interceptor missile should be launched or not.

Using a total of 15 Launch Interceptor Conditions (LICs), all of which are evaluated to 
`True` or `False` given specific computations on given data points-- 2d grid data-- controlled
by given parameters. A special logical connection, the Logical Connection Matrix (LCM), between 
these LICs is also given, together with a Preliminary Unlocking Vector (PUV), as input. 
The program calculates a Conditions Met Vector (CMV), consisting of the boolean values from
calculating each LIC. The parameters relevant to every LIC is stipulated in the specification.
Modifying these parameters will influence the calculated values of one or more LIC.
Using the CMV and the LCM the program creates the Preliminary Unlocking Matrix (PUM). The combined 
AND of each PUM row is logically implied by the corresponding boolean value in the PUV 
(`PUV_i -> and(PUM_i)`, i.e., `not(PUV_i) or and(PUM_i)`) to create the Final Unlocking Vector (FUV). 
The program will recommend a launch iff. all values in the FUV is `True`.

The program specification is given [Here](./decide.pdf).

## Using the program

### Virtual Environment
To be implemented

### Input 
Input is given to the program by specifying a path to a JSON file as a command-line argument

For example, the following would run the program and load the input in the given JSON file:
```bash
python decide.py /path/to/input.json
```
The JSON is formatted as follows:

```json
{
    "numpoints" : <INT>,
    "datapoints" : <[[FLOAT]]>,
    "parameters" : {
        "LENGTH1"   : <FLOAT>,
        "RADIUS1"   : <FLOAT>,
        "EPSILON"   : <FLOAT>,
        "AREA1"     : <FLOAT>,
        "QPTS"      : <INT>,
        "QUADS"     : <INT>,
        "DIST"      : <FLOAT>,
        "NPTS"      : <INT>,
        "KPTS"      : <INT>,
        "APTS"      : <INT>,
        "BPTS"      : <INT>,
        "CPTS"      : <INT>,
        "DPTS"      : <INT>,
        "EPTS"      : <INT>,
        "FPTS"      : <INT>,
        "GPTS"      : <INT>,
        "LENGTH2"   : <FLOAT>,
        "RADIUS2"   : <FLOAT>,
        "AREA2"     : <FLOAT>,
    },
    "LCM" : <[[STRING ('NOTUSED' | 'ANDD' | 'ORR')]]>,
    "PUV" : <[BOOLEAN]>
}
```
## ESSENCE state
We are in the ''In use'' state of the ESSENCE hierarchy. This is because we have quite established ways of planning, working, and reviewing which everyone follows for the most part. While we are mostly consistent, occasional slip ups do still occur. We do feel, however, that these practices help us work more efficiently and effectively. This is an important part since if the practices were not beneficial in our work, sticking by them would be quite difficult. To get to the next state, we need to evaluate our practices and see how to improve them. This can be done by regularly amassing feedback at meetings and then adjusting the practices accordingly. We have only had one iteration of trying out these practices and would need more iterations to get to the next state.

## Contributing / Workflow
We use a Github organization to track our development process, creating a project
to make use of Github's kanban-like issue board and linking this repository to said 
project. 

Thoroughly develop the backlog before starting to work on tickets.
Tickets are connected to specific branches which implements the tickets, these are
merged to our main branch through pull-requests.

### TBD - Trunk based development
We used a trunk based development model in which we, for each feature, bug, doc, etc,
create branches of off the main branch indicating atomic changes relating to a specific
ticket. 

These branches *needs* to be connected to an actual issue. For example, if I want
to add a feature, i create a branch titled feature/[ISSUE NUMBER]/name-of-feature.

Branches are merged to main only through the use of GitHub pull-requests.

### Conventional Commits
We used a format "conventional commits" in or commit messages. Every commit has the 
following format (bar merge commits and conflict resolutions):

```
<type>(<optional scope>)<!>: <description>
<BLANK LINE>
<optional body>
<BLANK LINE>
<optional footer(s)>
```


# Statement of contributions

## Review process 
Using Github pull requests, we made sure that every group member got to write issues,
create pull-requests, review pull-requests and write code (resolving issues). This 
was done in an ad-hoc manner.

## Rasmus Danielsson
### Issues 
[LIC3](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/8)

[I/O](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/17)

[LIC12](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/26)

[LIC14](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/28)

[This very README](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/38)

[More I/O](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/39)

### Reviews
[LIC5](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/43)

[Main flow structure](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/35)

## Dante Astorga Castillo
### Issues
[Main flow structure](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/33)
[Launch logic](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/24)
[Logic for setting FUV](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/22)
[Logic for setting PUM](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/19)
[LIC6](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/11)
### Reviews 
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
## Sebastian Montén
### Issues
[LIC4](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/21)
[LIC5](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/10)
[LIC9](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/9)
### Reviews
## Ludvig Skare
### Issues
[LIC0](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/5)
[LIC10](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/23)
[LIC11](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/25)
[LIC13](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/27)
### Reviews
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
## Victor Stenmark
### Issues
[LIC1](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/6)
[LIC2](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/7)
[LIC7](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/12)
[LIC8](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/20)
[Docstrings](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/29)
[Standardized angle calculations](https://github.com/KTH-DD2480-Fundsoft/assignment-1/issues/51)
### Reviews
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
[REVIEW](https://github.com/KTH-DD2480-Fundsoft/assignment-1/pull/)
