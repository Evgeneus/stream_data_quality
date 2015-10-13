import datetime

observed_cases = [
    # case 0
    # {
    #     'S0': [['2011-10-19 15:20:00', '2011-10-19 15:23:03', '2011-10-19 15:23:40',
    #             '2011-10-19 15:25:00', '2011-10-19 15:25:55'],
    #            ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']],
    #     'S1': [['2011-10-19 15:20:05', '2011-10-19 15:23:06', '2011-10-19 15:24:10',
    #             '2011-10-19 15:25:15', '2011-10-19 15:26:35'],
    #            ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']],
    #     'S2': [['2011-10-19 15:20:40', '2011-10-19 15:23:15', '2011-10-19 15:24:40',
    #             '2011-10-19 15:25:45', '2011-10-19 15:27:00'],
    #            ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']],
    # },
    {
        'S0': [['2011-10-19 15:20:00', '2011-10-19 15:25:55'],
               ['Wisc', 'MSR']],
        'S1': [['2011-10-19 15:20:05', '2011-10-19 15:26:35'],
               ['Wisc', 'MSR']],
        'S2': [['2011-10-19 15:20:40', '2011-10-19 15:27:00'],
               ['Wisc', 'MSR']],
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