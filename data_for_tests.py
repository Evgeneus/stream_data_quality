import datetime

observed_cases = [
    # # case 0 from article
    {
        'S1': [['2000-01-01 00:00:00', '2007-01-01 00:00:00'],
               ['UW', 'Google']],
        'S2': [['2000-01-01 00:00:00', '2002-01-01 00:00:00', '2005-01-01 00:00:00'],
               ['Wisc', 'UW', 'Google']],
        'S3': [['2001-01-01 00:00:00', '2006-01-01 00:00:00'],
               ['Wisc', 'UW']],
        'S4': [['2005-01-01 00:00:00'],
               ['UW']],
        'S5': [['2003-01-01 00:00:00', '2005-01-01 00:00:00', '2007-01-01 00:00:00'],
               ['Wisc', 'Google', 'UW']],
    },
    ]


def get_observed_cases():
    observed_cases_new = []
    for case in observed_cases:
        case_new = {}
        for s in case:
            t_new = []
            for t in case.get(s)[0]:
                t_new.append(datetime.datetime.strptime(t, '%Y-%m-%d %H:%M:%S'))
            case_new.update({s: [t_new, case.get(s)[1]]})
        observed_cases_new.append(case_new)

    return observed_cases_new