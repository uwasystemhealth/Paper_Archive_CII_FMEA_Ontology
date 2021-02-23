from owlready2 import get_ontology, onto_path
import pandas as pd

model_asset = None
model_fmea_iso = None
model_functional_system = None
model_iso = None


def load_ontology_modules():
    global model_asset, model_fmea_iso, model_functional_system, model_iso
    onto_path.append("./owl-files")
    model_asset = get_ontology("asset.owl").load()
    model_fmea_iso = get_ontology("fmea-iso.owl").load()
    model_functional_system = get_ontology("functional-system-ontology.owl").load()
    model_iso = get_ontology("LIS-14.owl").load()
    return model_asset, model_fmea_iso, model_functional_system, model_iso


def arrange_import_structure():
    model_asset.imported_ontologies.append(model_fmea_iso)
    model_fmea_iso.imported_ontologies.append(model_functional_system)
    model_functional_system.imported_ontologies.append(model_iso)


def read_industry_data(component_hierarchy_file_name, component_hierarchy_sheet_name, fmea_file_name, fmea_sheet_name):
    fmea_df = pd.read_excel(fmea_file_name, sheet_name=fmea_sheet_name)
    component_hierarchy_df = pd.read_excel(component_hierarchy_file_name, sheet_name=component_hierarchy_sheet_name)
    return fmea_df, component_hierarchy_df


def populate_component_hierarchy_data(component_hierarchy_df, component_column_name, parent_component_column_name,
                                      criticality_column_name):
    for index, row in component_hierarchy_df.iterrows():
        if not isinstance(row[component_column_name], float):
            child_component_string = row[component_column_name].replace(" ", "_")
            parent_component_string = row[parent_component_column_name].replace(" ", "_")
            is_critical = row[criticality_column_name].strip() == 'Y'
            child_component = model_functional_system.Component('component_' + child_component_string)
            parent_component = model_functional_system.Component('component_' + parent_component_string)
            parent_component.hasPart.append(child_component)
            if is_critical:
                parent_component.hasFunctionalPart.append(child_component)


def populate_fmea_data(fmea_df, fmea_component_column_name, malfunction_column_name):
    for index, row in fmea_df.iterrows():
        failure_string = row[malfunction_column_name]\
            .replace(" ", "_").replace('/', "_").replace("__", "_")
        component_string = row[fmea_component_column_name].replace(" ", "_").replace("__", "_")
        malfunction = model_fmea_iso.Malfunction('malfunction_due_to_'+failure_string+'_'+component_string)
        component = model_functional_system.Component('component_' + component_string)
        component.hasMalfunction.append(malfunction)


def save_populated_ontology():
    model_iso.save('output/LIS-14.owl')
    model_functional_system.save('output/functional-system.owl')
    model_fmea_iso.save('output/fmea-iso.owl')
    model_asset.save('output/asset.owl')


def main():

    component_hierarchy_file_name = "./data/PV_system_and_subsystem.xlsx"
    component_hierarchy_sheet_name = 'Sheet1'
    component_column_name = 'FunctionalLocation'
    parent_component_column_name = 'ParentFunctionalLocation'
    criticality_column_name = 'CriticalForOperations'
    fmea_file_name = './data/PressureVessel_FMEA.xlsx'
    fmea_sheet_name = 'PressureVessel_FMEA'
    fmea_component_column_name = 'FunctionalLocation'
    malfunction_column_name = 'ISO14224_Failure_Mechanism_Subdivision'

    print("Starting FMEA data import script")
    load_ontology_modules()
    arrange_import_structure()
    fmea_df, component_hierarchy_df = read_industry_data(component_hierarchy_file_name, component_hierarchy_sheet_name,
                                                         fmea_file_name, fmea_sheet_name)
    populate_component_hierarchy_data(component_hierarchy_df, component_column_name, parent_component_column_name,
                                      criticality_column_name)
    populate_fmea_data(fmea_df, fmea_component_column_name, malfunction_column_name)
    save_populated_ontology()
    print("Data import complete, see the output folder for results")


if __name__ == "__main__":
    main()
