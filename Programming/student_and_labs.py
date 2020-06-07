class Student():
    name = None
    config = None
    marks = None
    n = 0

    def __init__(self, name, config):
        self.name = name
        self.config = config
        self.marks = {}
        for i in range(0, self.config['lab_num']):
            self.marks[i] = 0

    def make_lab(self, m, n=n):
        if n == n:
            if self.marks.get(n) < m:
                if float(m) > float(self.config['lab_max']):
                    self.marks[n] = self.config['lab_max']
                while self.marks.get(n) != 0:
                    n += 1
        if float(m) > float(self.config['lab_max']):
            self.marks[n] = self.config['lab_max']
        else:
            self.marks[n] = m
        return self

    def make_exam(self, m):
        if m > self.config['exam_max']:
            self.marks['exam'] = self.config['exam_max']
            return (self.config['exam_max'])
        else:
            self.marks['exam'] = m
        return self

    def is_certified(self):
        if sum(self.marks.values()) >= self.config['k'] * 100:
            return (sum(self.marks.values()), True)
        else:
            return (sum(self.marks.values()), False)


conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
oleg = Student('Oleg', conf)
oleg.make_lab(1)     # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(8, 0) # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(1) # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
oleg.make_lab(10, 7) # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(4, 1) # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(5) # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
oleg.make_lab(6.5) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
oleg.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified()) # (59.5, False)
oleg.make_lab(7, 1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified()) # (62.5, True)