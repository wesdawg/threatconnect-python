""" third-party """
from enum import Enum


class ResourceType(Enum):
    """ """
    # misc
    ATTRIBUTES = 10
    DNS_RESOLUTIONS = 20
    OWNERS = 30

    # groups
    ADVERSARY = 110
    ADVERSARIES = 115
    DOCUMENT = 120
    DOCUMENTS = 125
    EMAIL = 130
    EMAILS = 135
    FILE_OCCURRENCE = 140
    FILE_OCCURRENCES = 145
    GROUPS = 150
    INCIDENT = 160
    INCIDENTS = 165
    SECURITY_LABEL = 170
    SECURITY_LABELS = 175
    SIGNATURE = 180
    SIGNATURES = 185
    TAG = 190
    TAGS = 195
    THREAT = 200
    THREATS = 205

    # indicators
    INDICATOR = 500
    INDICATORS = 505
    ADDRESS = 510
    ADDRESSES = 515
    EMAIL_ADDRESS = 520
    EMAIL_ADDRESSES = 525
    FILE = 530
    FILES = 535
    HOST = 540
    HOSTS = 545
    URL = 550
    URLS = 555

    # victims
    VICTIM = 900
    VICTIMS = 905

    # victims
    VICTIM_ASSET = 1000
    VICTIM_ASSETS = 1005
    VICTIM_EMAIL_ADDRESS = 1010
    VICTIM_EMAIL_ADDRESSES = 1015
    VICTIM_NETWORK_ACCOUNT = 1020
    VICTIM_NETWORK_ACCOUNTS = 1025
    VICTIM_PHONE = 1030
    VICTIM_PHONES = 1035
    VICTIM_SOCIAL_NETWORK = 1040
    VICTIM_SOCIAL_NETWORKS = 1045
    VICTIM_WEBSITE = 1050
    VICTIM_WEBSITES = 1055
