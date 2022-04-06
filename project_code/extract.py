"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neo_list = []
    with open(neo_csv_path, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            designation = line["pdes"]
            name = line["name"]
            diameter = line["diameter"]
            hazardous = line["pha"]
            neo_list.append(NearEarthObject(designation, name, diameter, hazardous))
    # Return the collection of NEOs
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    close_approaches = []
    with open(cad_json_path, "r") as f:
        reader = json.load(f)
        for approaches in reader["data"]:
            designation = approaches[reader["fields"].index("des")]
            time = approaches[
                reader["fields"].index("cd")
            ]  # time is under column "cd" - time of close-approach in UTC
            distance = approaches[reader["fields"].index("dist")]
            velocity = approaches[reader["fields"].index("v_rel")]  # relative velocity
            close_approaches.append(
                CloseApproach(time, designation, distance, velocity)
            )
    return close_approaches
