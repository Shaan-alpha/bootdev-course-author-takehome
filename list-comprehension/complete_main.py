def apply_rage(attacks):
    return [attack * 2 for attack in attacks]


def get_critical_hits(attacks):
    return [attack for attack in attacks if attack >= 50]
