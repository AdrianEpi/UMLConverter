<img align="middle" width="100%" height="300" src="../img/logo/banner600x200.png">

# RESULTS

## **Index**

1. [Class Diagram](#id1)
2. [Package Information](#id2)
3. [Metrics](#id3)
4. [Metrics Tables](#id4)
5. [Metrics Explanation](#id6)

***


## Class Diagram<a name="id1"></a>

<img align="middle" width="100%" src="./projectUML.png">

 *Legend*

<img align="middle" src="..//img/legend/reddress-darkblue-legend.png">

***


## Package Information<a name="id2"></a>

#### *ast_module*
* AST
* JsAST
* Line
* PyAST
* PythonNode


#### *file_module*
* File
* Markdown
* Searcher


#### *interface_module*
* Interface


#### *metric_module*
* Metric
* MetricClass
* MetricPackage


#### *uml_module*
* Translator
* UMLConverter

***


## Metrics<a name="id3"></a>
---

## Metrics Tables<a name="id4"></a>

### *Class Table*

| Name | Package | NOC | CodeLines | CommentLines | CCD | CBO | Score |
| -- | -- | -- | -- | -- | -- | -- | -- |
| AST | ast_module | 2 | 55 | 151 | 2.75 | 1 | 87.17% |
| JsAST | ast_module | 0 | 137 | 125 | 0.91 | 2 | 81.76% |
| Line | ast_module | 0 | 46 | 51 | 1.11 | 0 | 82.75% |
| PyAST | ast_module | 0 | 348 | 251 | 0.72 | 2 | 73.68% |
| PythonNode | ast_module | 0 | 79 | 104 | 1.32 | 0 | 82.75% |
| File | file_module | 0 | 115 | 59 | 0.51 | 0 | 61.92% |
| Markdown | file_module | 0 | 114 | 30 | 0.26 | 1 | 52.72% |
| Searcher | file_module | 0 | 39 | 40 | 1.03 | 0 | 82.75% |
| Interface | interface_module | 0 | 88 | 94 | 1.07 | 0 | 82.75% |
| Metric | metric_module | 0 | 94 | 16 | 0.17 | 2 | 50.31% |
| MetricClass | metric_module | 0 | 133 | 30 | 0.23 | 0 | 50.02% |
| MetricPackage | metric_module | 0 | 77 | 18 | 0.23 | 0 | 50.02% |
| Translator | uml_module | 0 | 159 | 165 | 1.04 | 1 | 84.17% |
| UMLConverter | uml_module | 0 | 236 | 188 | 0.8 | 9 | 87.0% |

### *Package Table*

| Name | Class Ammount | DIT | LCOM | Score |
| -- | -- | -- | -- | -- |
| ast_module | 5 | 1 | 0.0 | 90.81% |
| file_module | 3 | 0 | 0.5 | 82.9% |
| interface_module | 1 | 0 | 0.0 | 91.38% |
| metric_module | 3 | 0 | 0.0 | 75.06% |
| uml_module | 2 | 0 | 1.0 | 57.79% |

***



## Metrics Explanation<a name="id4"></a>

### *Class Metrics*

* **NOC**: A class's *number of children* (NOC) metric simply measures the number of immediate descendants of the class.
* **CCD**: A class's *code comments density* (CCD) metric simply measures the ratio of comment lines per code lines.
* **CBO**: The *coupling between object classes* (CBO) metric represents the number of classes coupled to a given class (efferent couplings, Ce). This coupling can occur through method calls, field accesses, inheritance, arguments, return types, and exceptions.
* **Score**: The *score* of a class is calculated using 42.5% CBO + 42.5% CCD + 15% NOC making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.

### *Package Metrics*

* **DIT**: The *depth of inheritance tree* (DIT) metric provides for each class a measure of the inheritance levels from the object hierarchy top, excluding languages objects (Class, ABC, Object, BasicObject...).
* **LCOM**: A class's *lack of cohesion in methods* (LCOM) metric counts the sets of methods in a class that are not related through the sharing of some of the class's fields.
* **Score**: The *score* of a class is calculated using 50% Average class score + 35% LCOM + 15% DIT making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.

***

