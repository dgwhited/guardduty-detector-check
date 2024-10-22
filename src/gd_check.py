import boto3
import json
import argparse


def create_session(profile=None):
    """Creates a boto session

    Args:
        profile (string): AWS profile name

    Returns:
        session (boto3): Authenticated AWS Session
    """
    if profile:
        return boto3.Session(profile_name=profile)
    else:
        return boto3.Session()


def create_client(session, service, region_name="us-east-1"):
    """Creates a service client from a boto session

    Args:
        session (object): Authenticated boto3 session
        service (string): service name to create the client for

    Returns:
        [object]: client session for specific aws service (eg. accessanalyzer)
    """
    return session.client(service, region_name)


def get_detector_and_publishing_destination(session, region):
    """Gets the guardduty detector in a region if it exists, and gets finding publishing destination

    Args:
        session (boto3): Authenticated AWS Session
        region (str): region name


    Returns:
        dict: detector_id:publishingdestination
    """
    client = create_client(session=session, service="guardduty", region_name=region)
    detector = client.list_detectors()
    detector_ids = detector.get("DetectorIds")
    if detector_ids:
        detector_id = detector_ids[0]
    else:
        return {}
    publishing_destination = client.list_publishing_destinations(
        DetectorId=detector_id
    ).get("Destinations")
    return {detector_id: publishing_destination}


def get_enabled_regions(session):
    """Gets all enabled, enabling, and enabled by default regions

    Args:
        session (boto3): Authenticated AWS Session

    Returns:
        list: All enabled region names
    """
    acct = create_client(session=session, service="account")

    regions = acct.list_regions(
        MaxResults=50,
        RegionOptStatusContains=["ENABLED", "ENABLING", "ENABLED_BY_DEFAULT"],
    )
    region_names = [region.get("RegionName") for region in regions.get("Regions")]
    return region_names


def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "--profile", help="AWS Profile Name (default: None)")
    args = parser.parse_args()

    session = create_session(profile=args.profile)

    region_names = get_enabled_regions(session)

    guardduties = [
        {
            str(region): get_detector_and_publishing_destination(
                session=session, region=region
            )
        }
        for region in region_names
    ]
    print(json.dumps(guardduties, indent=2))


if __name__ == "__main__":
    main()
