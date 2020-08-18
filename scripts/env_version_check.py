import semantic_version
import sys
import yaml

environment = sys.argv[1]

with open('version') as stream:
    service_version = semantic_version.Version(stream.read().replace('\n', ''))

with open('serverless.yml') as stream:
    sls_configs = yaml.safe_load(stream)
    try:
        min_version = sls_configs['custom']['deployment_configs'][environment]['min_version']
        max_version = sls_configs['custom']['deployment_configs'][environment]['max_version']
    except KeyError as ke:
        print("Error, your serverless.yml file is missing required variables for deployment.")
        print("Values that could not be found:\n"
              f"['custom']['deployment_configs']['{environment}']['min_version']\n"
              f"['custom']['deployment_configs']['{environment}']['max_version']\n")
        raise ke

high_number = "99999999999"
min_version_replaced = semantic_version.Version(min_version.replace("*", high_number))
max_version_replaced = semantic_version.Version(max_version.replace("*", high_number))
if min_version_replaced <= service_version <= max_version_replaced:
    print(f"The version {str(service_version)} passed the version constraint: {str(min_version)} <= {str(service_version)} <= {str(max_version)} for the environment: [{environment}]")
else:
    print(f"The version {str(service_version)} failed the version constraint: {str(min_version)} <= {str(service_version)} <= {str(max_version)} for the environment: [{environment}].\n"
          f"Skipping deployment for [{environment}]")
    sys.exit(1)
