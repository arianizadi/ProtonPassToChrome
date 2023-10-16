<p id="readme-top" />

<div align="center">
    <img src="assets/proton-logo_z7innb.svg" alt="Logo" height="80">
  <h3 align="center">Proton Pass to Chrome Password Converter</h3>

  <p align="center">
    Easily convert your Proton Pass passwords to a CSV file that can be imported to Google Chrome.
    </br>
  </p>
</div>

## Prerequisites

Before using this script, make sure you have Python installed on your computer. This script was created and tested with Python 3.

## Usage

1. Export Proton Pass Passwords:
   - Export your Proton Pass passwords as a JSON file. This file should contain your vaults and items. Make sure it is not encrypted.

2. Configure the Script:
   - Open the script file and update the `PROTON_PASS_FILE` and `OUTPUT_FILE` variables to specify the paths to your Proton Pass exported file and the output CSV file, respectively.

3. Run the Script:
   - Execute the script using your Python interpreter. It will read the Proton Pass data, convert it, and save the output to the specified CSV file.

4. Import to Google Chrome:
   - You can now import the generated CSV file into Google Chrome by following the steps:
     - Open Chrome.
     - Click on the three dots (menu) in the top right corner.
     - Go to "Google Password Manager."
     - On the left side, click "Settings."
     - Finally, click "Import." and select the CSV file generated.
     - Enjoy!

## Note

- This script assumes that your Proton Pass data is not encrypted. If it's encrypted, this script won't be able to convert it.

- It's important to ensure that your Proton Pass data is correctly structured. Any variations in the structure may result in errors or incomplete conversions.

- The script will create a CSV file with the following columns: "username," "password," and "website."

- If the Proton Pass data contains items other than login credentials, they will be skipped during the conversion process.

- If any errors occur during the conversion, the script will print a message indicating the issue.

- Proton Pass allows multiple URLs to be associated with a single item. However, Chrome only allows one URL per item. Therefore, if an item has multiple URLs, the script will only use the first URL.
