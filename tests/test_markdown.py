# -*- coding: utf-8 -*-
#   @Proyect:            UMLConverter
#   @Author:             Adrian Epifanio
#   @File:               test_markdown.py
#   @Author:             Adrian Epifanio
#   @Date:               2023-02-09 09:05:54
#   @Email:              adrianepi@gmail.com
#   @GitHub:             https://github.com/AdrianEpi
#   @Last Modified by:   Adrian Epifanio
#   @Last Modified time: 2023-02-09 09:26:45
#   @Description:        ...

from app.modules.file_module.markdown import Markdown
from app.modules.metric_module.metric import Metric
from app.modules.metric_module.metricClass import MetricClass
from app.modules.metric_module.metricPackage import MetricPackage

import pytest



def test_Markdown():
	metrics = Metric()
	package = MetricPackage(0, 'pName')
	mClass = MetricClass(0, 'cName')
	metrics.setClassList([mClass])
	metrics.setPackageList([package])
	md = Markdown(path = "", metrics = metrics, theme = '_none_', projectName = "TEST")
	o1 = '<img align="middle" width="100%" height="300" src="/mnt/e/TFG/UMLConverter/img/logo/banner600x200.png">\n\n# TEST\n\n## **Index**\n\n1. [Class Diagram](#id1)\n2. [Package Information](#id2)\n3. [Metrics](#id3)\n4. [Metrics Tables](#id4)\n5. [Metrics Explanation](#id5)\n\n***\n\n\n## Class Diagram<a name="id1"></a>\n\n<img align="middle" width="100%" src="projectUML.png">\n\n *Legend*\n\n<img align="middle" src="/mnt/e/TFG/UMLConverter/img/legend/_none_-legend.png">\n\n***\n\n\n## Package Information<a name="id2"></a>\n\n#### *pName*\n\n***\n\n\n## Metrics<a name="id3"></a>\n---\n\n## Metrics Tables<a name="id4"></a>\n\n### *Class Table*\n\n| Name | Package | NOC | CodeLines | CommentLines | CCD | CBO | Score |\n| -- | -- | -- | -- | -- | -- | -- | -- |\n| cName | pName | 0 | 0 | 0 | 0.0 | 0 | 0.0% |\n\n### *Package Table*\n\n| Name | Class Ammount | DIT | LCOM | Score |\n| -- | -- | -- | -- | -- |\n| pName | 0 | 0 | 0.0 | 0.0% |\n\n***\n\n\n\n## Metrics Explanation<a name="id5"></a>\n\n### *Class Metrics*\n\n* **NOC**: A class\'s *number of children* (NOC) metric simply measures the number of immediate descendants of the class.\n* **CCD**: A class\'s *code comments density* (CCD) metric simply measures the ratio of comment lines per code lines.\n* **CBO**: The *coupling between object classes* (CBO) metric represents the number of classes coupled to a given class (efferent couplings, Ce). This coupling can occur through method calls, field accesses, inheritance, arguments, return types, and exceptions.\n* **Score**: The *score* of a class is calculated using 42.5% CBO + 42.5% CCD + 15% NOC making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.\n\n### *Package Metrics*\n\n* **DIT**: The *depth of inheritance tree* (DIT) metric provides for each class a measure of the inheritance levels from the object hierarchy top, excluding languages objects (Class, ABC, Object, BasicObject...).\n* **LCOM**: A class\'s *lack of cohesion in methods* (LCOM) metric counts the sets of methods in a class that are not related through the sharing of some of the class\'s fields.\n* **Score**: The *score* of a package is calculated using 50% Average class score + 35% LCOM + 15% DIT making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.\n\n***\n\n'
	o2 = '<img align="middle" width="100%" height="300" src="/home/runner/work/UMLConverter/UMLConverter/img/logo/banner600x200.png">\n\n# TEST\n\n## **Index**\n\n1. [Class Diagram](#id1)\n2. [Package Information](#id2)\n3. [Metrics](#id3)\n4. [Metrics Tables](#id4)\n5. [Metrics Explanation](#id5)\n\n***\n\n\n## Class Diagram<a name="id1"></a>\n\n<img align="middle" width="100%" src="projectUML.png">\n\n *Legend*\n\n<img align="middle" src="/home/runner/work/UMLConverter/UMLConverter/img/legend/_none_-legend.png">\n\n***\n\n\n## Package Information<a name="id2"></a>\n\n#### *pName*\n\n***\n\n\n## Metrics<a name="id3"></a>\n---\n\n## Metrics Tables<a name="id4"></a>\n\n### *Class Table*\n\n| Name | Package | NOC | CodeLines | CommentLines | CCD | CBO | Score |\n| -- | -- | -- | -- | -- | -- | -- | -- |\n| cName | pName | 0 | 0 | 0 | 0.0 | 0 | 0.0% |\n\n### *Package Table*\n\n| Name | Class Ammount | DIT | LCOM | Score |\n| -- | -- | -- | -- | -- |\n| pName | 0 | 0 | 0.0 | 0.0% |\n\n***\n\n\n\n## Metrics Explanation<a name="id5"></a>\n\n### *Class Metrics*\n\n* **NOC**: A class\'s *number of children* (NOC) metric simply measures the number of immediate descendants of the class.\n* **CCD**: A class\'s *code comments density* (CCD) metric simply measures the ratio of comment lines per code lines.\n* **CBO**: The *coupling between object classes* (CBO) metric represents the number of classes coupled to a given class (efferent couplings, Ce). This coupling can occur through method calls, field accesses, inheritance, arguments, return types, and exceptions.\n* **Score**: The *score* of a class is calculated using 42.5% CBO + 42.5% CCD + 15% NOC making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.\n\n### *Package Metrics*\n\n* **DIT**: The *depth of inheritance tree* (DIT) metric provides for each class a measure of the inheritance levels from the object hierarchy top, excluding languages objects (Class, ABC, Object, BasicObject...).\n* **LCOM**: A class\'s *lack of cohesion in methods* (LCOM) metric counts the sets of methods in a class that are not related through the sharing of some of the class\'s fields.\n* **Score**: The *score* of a package is calculated using 50% Average class score + 35% LCOM + 15% DIT making sure thate each metric is between the appropiate limits, the further each value is from the optimal value the less it counts for the score.\n\n***\n\n'
	data = md.generateMarkdown()
	assert((data == o1) or (data == o2))