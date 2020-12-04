subj = {}
with open('task_6_text.txt') as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()
        if lecture == '-':
            lecture = '0(l)'
        if practice == '-':
            practice = '0(pr)'
        if lab == '-':
            lab = '0(lab)'
        l_hours, l_text = lecture.split('(')
        pr_hours, pr_text = practice.split('(')
        lab_hours, lab_text = lab.split('(')
        subj[subject] = int(l_hours) + int(pr_hours) + int(lab_hours)
    print(f'Общее количество часов по предметам:\n{subj}')
