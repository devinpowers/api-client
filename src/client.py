import requests

class APIClient:
    def __init__(self, base_url):
        """
        Initialize the API client with the base URL of the FastAPI application.
        :param base_url: Base URL of the API (e.g., "http://localhost:8000")
        """
        self.base_url = base_url

    def get_status(self):
        """Check the API's status."""
        response = requests.get(f"{self.base_url}/status/")
        return response.json()

    def get_supported_formats(self):
        """Get the supported image formats."""
        response = requests.get(f"{self.base_url}/supported-formats/")
        return response.json()

    def extract_text_from_image(self, file_path):
        """Extract text from an image file."""
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(f"{self.base_url}/extract-text/", files=files)
        return response.json()

    def extract_metadata(self, file_path):
        """Extract metadata from an image file."""
        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.post(f"{self.base_url}/extract-metadata/", files=files)
        return response.json()


# Example usage
if __name__ == "__main__":
    client = APIClient(base_url="http://localhost:8000")

    print("Checking API Status...")
    print(client.get_status())

    print("\nSupported Formats:")
    print(client.get_supported_formats())

    image_path = "test.jpg"  # Replace with the path to a test image

    print("\nExtracting Text from Image...")
    print(client.extract_text_from_image(image_path))

    print("\nExtracting Metadata from Image...")
    print(client.extract_metadata(image_path))
