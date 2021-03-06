import collections


LOCAL_BODIES = collections.namedtuple(
    "LOCAL_BODY_CHOICES",
    ["GRAM_PANCHAYATH", "BLOCK_PANCHAYATH", "DISTRICT_PANCHAYATH", "MUNICIPALITY", "CORPORATION", "OTHERS",],
)(GRAM_PANCHAYATH=1, BLOCK_PANCHAYATH=2, DISTRICT_PANCHAYATH=3, MUNICIPALITY=4, CORPORATION=5, OTHERS=6,)

LOCAL_BODY_CHOICES = (
    (LOCAL_BODIES.GRAM_PANCHAYATH, "Gram Panchayath"),
    (LOCAL_BODIES.BLOCK_PANCHAYATH, "Block Panchayath"),
    (LOCAL_BODIES.DISTRICT_PANCHAYATH, "District Panchayath"),
    (LOCAL_BODIES.MUNICIPALITY, "Municipality"),
    (LOCAL_BODIES.CORPORATION, "Corporation"),
    (LOCAL_BODIES.OTHERS, "Others"),
)

RESET_PASSWORD_BASE_URL = "reset-password"
