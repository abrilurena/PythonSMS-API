
# Vonage SMS Sender

This is a simple Python script to send SMS messages using the Vonage (Nexmo) REST API.

## How to use

1. Clone this repository.
2. Create a virtual environment (optional but recommended):
   ```
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set your Vonage credentials as environment variables:
   - On Windows (PowerShell):
     ```
     $env:VONAGE_API_KEY="your_api_key"
     $env:VONAGE_API_SECRET="your_api_secret"
     ```
   - On macOS/Linux:
     ```
     export VONAGE_API_KEY="your_api_key"
     export VONAGE_API_SECRET="your_api_secret"
     ```
6. Run the script:
   ```
   python main.py
   ```

## Notes
- Do not share your real credentials in public repositories.
- The sender ("from") may be restricted depending on the destination country.

## License
MIT
