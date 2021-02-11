# Paper_Archive_CII_FMEA_Ontology

This repository contains supplementary materials for the paper titled _An ontology for reasoning over engineering textual data stored in FMEA spreadsheet tables_. If you would like to use the work contained in this repository, please cite the following (will post full bibliographic details when available):

- Hokiewicz, M., Klüwer, J. W., Woods, C., Smoker, T., Low, E (2021). An ontology for reasoning over engineering textual data stored in FMEAspreadsheet tablesy. Unpublished manuscript.

### Contents of this repository
- Industrial-data-population-script
  -owl-files (a folder containing all ontology files, all in RDF/XML format for [OWLReady2](https://pythonhosted.org/Owlready2/) compatibility)
  -populator-py.py (a python script that populates an ontology from a FMEA spreadsheet using [OWLReady 2](https://pythonhosted.org/Owlready2/) )

- Ontology-files-turtle-format (the ontology files presented in the paper, all in Turtle format)
  - asset.ttl (the asset ontology)
  - fmea-iso.ttl (the fmea ontology)
  - functional-system-ontology-ttl (the functional system ontology)
  - LIS-14.ttl (the ISO15926 part 14 upper ontology)

### How to open the ontology
To open the ontology, you will need an Ontology Development Environment (ODE) such as [Protégé](https://protege.stanford.edu/). In your editor, simply open the asset.ttl file to see all four ontologies. You may be presented with an error that says "cannot locate ontology", if this is the case then find the requested ontology in your file system to load it. 

### How to run the ontology population script
The ontoloty population script can be run using [Python](https://www.python.org/). However, there are some prerequisites. This is because we cannot share the industry data used for this work for proprietary reasons. To run this file with your data, you will need to edit the following variables in the script.

- component_hierarchy_file_name = <path to a .xlsx containing your asset hierarchy>
- component_hierarchy_sheet_name = <the name of the sheet that the asset hierarchy data is in (i.e. Sheet1)>
- component_column_name = <the column name in the the asset hierarchy spreasheet that contains unique identitiers for your assets (i.e. FunctionalLocation)>
- parent_component_column_name = <the column name in the asset hierarchy spreasheet that contains the immediate parent of each asset (i.e. ParentFunctionalLocation)>
- criticality_column_name = <the column name in asset hierarchy spreasheet that contains a 'Y' or 'N' indicating if the asset is critical to its system's function (i.e. Critical)>
- fmea_file_name = <path to a .xlsx containing your FMEA>
- fmea_sheet_name = <the name of the sheet that the FMEA data is in (i.e. Sheet1)>
- fmea_component_column_name = <the column name in the FMEA spreasheet that contains unique asset identifiers (i.e. FunctionalLocation)>
- malfunction_column_name = <the column name in the FMEA spreasheet that contains a malfuction description (i.e. FailureMechanism)>

Additionally, you will need to create a new folder in your project's directory called "output". This is where the populated ontology will be stored after the script has been run.
