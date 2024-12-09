import sys
# Print app version

def print_version():
    version = 'v0.0.1'
    print(f"App Version: {version}")
    sys.exit(0)

if __name__ == "__main__":
    print_version()  # Calling the function to print the version and exit