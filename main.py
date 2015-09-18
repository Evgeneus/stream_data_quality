from cef_measure import get_CEF
from life_span import get_life_span
from data_for_tests import observed_cases

if __name__ == '__main__':
    ground_truth = ['Wisc', 'Wisc', 'Wisc', 'MSR', 'MSR']

    for case_number, observed in enumerate(observed_cases):
        observed_keys = sorted(observed.keys())

        #initialization of cef
        cef_measures = {}
        for s in observed_keys:
            # print s
            cef = [1, 0.5, 1]
            cef_measures.update({s: cef})
        iter_quantity = 0
        sources_number = len(observed_keys)
        life_span = get_life_span(observed=observed, cef_measures=cef_measures)

        # print initial info
        print 'CASE NUMBER: {}'.format(case_number)
        for key in observed_keys:
            print '{}: {}'.format(key, observed.get(key))
        print 'Initial life span: {}'.format(life_span)
        print '---------------------'
        life_span_old = []

        cef_for_each_s_old = [cef for i in range(sources_number)]
        cef_delta_sum = [1, 1, 1]
        while max(cef_delta_sum) > 0.01*sources_number:
            cef_for_each_s = []
            for s in observed_keys:
                # print s
                cef = get_CEF(life_span, observed.get(s))
                cef_measures.update({s: cef})
                cef_for_each_s.append(cef)

            life_span_old = life_span
            life_span = get_life_span(observed=observed, cef_measures=cef_measures)
            iter_quantity += 1

            cef_delta_sum = [0, 0, 0]
            for old, new in zip(cef_for_each_s_old, cef_for_each_s):
                diff_for_s = [abs(x-y) for x, y in zip(old, new)]
                for i in range(len(cef_delta_sum)):
                    cef_delta_sum[i] += diff_for_s[i]
            cef_for_each_s_old = cef_for_each_s

            print 'iter={}'.format(iter_quantity)
            print 'cef_delta_sum: {}'.format(cef_delta_sum)
            for cef, s in zip(cef_for_each_s, observed_keys):
                print s, ': C={}, E={}, F={}'.format(cef[0], cef[1], cef[2])
            print "Object's life span: {}".format(life_span)
            print '---------------------'

        print 'iter_quantity={}'.format(iter_quantity)
        print "*********************************************************"
