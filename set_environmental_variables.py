import os


def load_env_file(file_path):
    """
    Reads a .env file and returns a dictionary of environment variables.
    """
    env_vars = {}
    with open(file_path) as f:
        for line in f:
            # Strip whitespace and skip comments
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Split key and value
            key, value = line.split("=", 1)
            env_vars[key] = value
    return env_vars


def set_env_variables(env_vars):
    """
    Sets the environment variables in the current process.
    """
    for key, value in env_vars.items():
        os.environ[key] = value


if __name__ == "__main__":

    # Load environment variables from the .env file.
    env_vars = load_env_file(".env")

    # Set environment variables from the loaded file.
    set_env_variables(env_vars)

    # Show the environmental variables from the .env file.
    print("Current Environmental Variables from .env file:")
    for key, value in env_vars.items():
        print(f"{key}: {os.getenv(key)}")
