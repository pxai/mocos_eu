import requests
import json
import sys

# sys.argv[0] is the script name itself
input_file = sys.argv[1]
output_file = sys.argv[2]

def read_and_write_lines(input_filename, output_filename, chunk_size=1000):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            total_chars = 0
            output_lines = []

            for line in infile:
                line_length = len(line)

                if total_chars + line_length > chunk_size:
                    # Write the collected lines to the output file
                    translated_lines = translate_text('\n'.join(output_lines))
                    outfile.writelines(translated_lines)
                    # Reset for the next chunk
                    total_chars = 0
                    output_lines = []

                total_chars += line_length
                output_lines.append(line)

            # Write any remaining lines
            if output_lines:
              translated_lines = translate_text('\n'.join(output_lines))
              outfile.writelines(translated_lines)

        print(f"Successfully processed {input_filename} and wrote to {output_filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")



def translate_text(text):
  # URL to which the POST request will be sent
  url = "https://backend.batua.eus/es2eu/translate"  # replace with your URL

  # JSON payload to send with the POST request
  payload = {
      "mkey":"85b92f176fe0efac",
      "text": text,
      "model":"batua_es2eu"
  }

  # Headers (optional)
  headers = {
      "Content-Type": "application/json"
  }

  # Make the POST request
  response = requests.post(url, headers=headers, data=json.dumps(payload))

  # Check if the request was successful
  if response.status_code == 200:
      # Parse the JSON response
      response_data = response.json()

      # Extract the 'message' field
      message = response_data.get("message", "No message field found")
      print("Translated :", len(message))
      return message
  else:
      print(f"Request failed with status code: {response.status_code}")
      return None


# Test the function
# result = translate_text("Hola, como estas?", "eu")

read_and_write_lines(input_file, output_file)