def solution(id_list, reports, k) :
    report_dict = {}
    result_dict = {who : 0 for who in id_list}
    for report in reports :
        report = report.split(' ')
        if report[-1] in report_dict:
            if report[0] not in report_dict[report[-1]] :
                report_dict[report[-1]].append(report[0])
        else :
            report_dict[report[-1]] = [report[0]]

    stoped = []
    for who, array in report_dict.items() :
        if len(array) >= k :
            stoped.append(who)

    for stop in stoped :
        for who in report_dict[stop] :
            result_dict[who] += 1
    return list(result_dict.values())