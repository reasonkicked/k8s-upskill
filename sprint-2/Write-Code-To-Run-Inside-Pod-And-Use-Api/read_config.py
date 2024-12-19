from kubernetes import client, config

def read_configmap(namespace, configmap_name):
    # Load in-cluster configuration
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    try:
        # Fetch the ConfigMap
        config_map = v1.read_namespaced_config_map(configmap_name, namespace)
        print("ConfigMap Data:")
        for key, value in config_map.data.items():
            print(f"{key}: {value}")
    except client.exceptions.ApiException as e:
        print(f"Error reading ConfigMap: {e}")

if __name__ == "__main__":
    namespace = "upskill"
    configmap_name = "app-config"
    read_configmap(namespace, configmap_name)
