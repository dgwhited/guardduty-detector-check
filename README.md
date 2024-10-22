# AWS GuardDuty Detector and Publishing Destination Checker

This Python script allows you to list the enabled regions in an AWS account and check GuardDuty in each region to see if it is enabled. For enabled GuardDuty detectors, it retrieves the detector ID and the associated finding publishing destination, if it exists.

## Features

- Lists all enabled regions in an AWS account
- Checks GuardDuty status in each enabled region
- Retrieves GuardDuty detector IDs
- Fetches finding publishing destinations for enabled detectors

## Prerequisites

- Python 3.x
- AWS CLI configured with appropriate credentials
- boto3 library installed

## Installation

### From PyPi

```
pip install guardduty-detector-check
```

### Or Install locally
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/aws-guardduty-checker.git
   ```

2. Install in a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate"
   pip install .
   ```

## Usage

Run the script using the following command:

```
guardduty-detector-check [-p PROFILE]
```

Options:
- `-p` or `--profile`: Specify an AWS profile name (optional)

Example:
```
guardduty-detector-check -p my-aws-profile
```

The script will output a JSON-formatted list of enabled regions, their GuardDuty detector IDs (if enabled), and the associated publishing destinations (if configured).

## Output

The script outputs a JSON-formatted list of dictionaries, where each dictionary represents a region and contains the following information:
- Region name
- GuardDuty detector ID (if enabled)
- Publishing destination details (if configured)

Example output:
```json
[
  {
    "us-east-1": {
      "abc123ABC123abc123ABC123abc123AB": [
        {
          "DestinationId": "abcABCdefDEFghiGHIjklJKLmnoMNO12",
          "DestinationType": "S3",
          "Status": "PUBLISHING"
        }
      ]
    }
  },
  {
    "us-west-2": {}
  }
]
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.