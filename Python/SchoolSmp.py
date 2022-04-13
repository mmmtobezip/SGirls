#------------------------------------------------------------------------
# Team Marciale
# Stable Marriage Problem에 기반한 학교 배정 방식
#------------------------------------------------------------------------

from queue import PriorityQueue

# 학생 객체 : no 를 추가하여 동점자가 나오면 번호로 우선순위 결정
class Applier:
	def __init__(self, nn, oo, ss, pp):
		self.name = nn
		self.no = oo
		self.score = ss	# 국영수 과목 점수
		self.pref = pp	# 지망 순서 리스트
		self.pos = 0	# 현재 지망
	def dump(self):
		print(self.name, self.no, self.score, self.pref, self.pos)

# 학교 객체
class School:
	def __init__(self, nn, cc, ww):
		self.name = nn
		self.capa =cc	# 학교 정원
		self.weight = ww	# 과목 가중치
		self.pq = PriorityQueue()	# 현재 배정 학생

	def fight(self, a):		# 경쟁
		ww =0
		for i in range(3):
			ww = ww + self.weight[i]*a.score[i]
		self.pq.put( [ww, a.no, a])
		if (self.pq.qsize() <= self.capa):
			return None
		return self.pq.get()[2]

	def dump(self):
		print(self.name, self.capa, self.weight)

#---------------------------------------------------------------------
# 임의의 데이터 만들기
# Na 학생수, Nb 학교 수, C 정원 (일단 모두 같게- random화도 가능)
Na, Nb, C = 1000, 12, 2[00

import random
Fchar = "김이박최정강조윤장임고양부"
Mchar = "민서예지도하주윤채현지소승미한"
Lchar = "준윤우원찬석성호후서연아은진"

def GenName():
	res = random.choice(Fchar)
	res += random.choice(Mchar)
	res += random.choice(Lchar)
	return res

A=[]
for i in range(Na):
	score = []
	for j in range(3):		# 국영수 점수
		score.append(random.randrange(0, 101))
	np = random.randrange(1, Nb+1)
	p = []
	for j in range(np):
		t = random.randrange(0, Nb)
		if ((t in p) == True):
			continue
		p.append(t)
	A.append(Applier(GenName(), i, score, p))

# 학교 데이터 만들기
Sname = ['사대부고', '서귀포고', '대정여고', '오현고', '제주일고', '남녕고', '중앙여고','신성여고','삼성여고','대기고','대정고','표선고']
B =[]
for i in range(Nb):
	ca = random.randrange(int (C*0.5), int(C*1.5))
	w = [] 
	for j in range(3):
		w.append(random.randrange(50,101))
	B.append(School(Sname[i], ca, w))

# 시간을 측정하는 함수
import datetime as pydatetime
ts = pydatetime.datetime.now().timestamp()

for i in range(len(A)):
	chal = A[i]
	while (True):
		if (chal.pos >= len(chal.pref)):
			break
		tar = chal.pref[chal.pos]
		tt = B[tar].fight(chal)
		chal.pos +=1
		if (tt == None):
			break
		chal = tt

ss = 0 
for i in range(len(B)):
	ss += B[i].pq.qsize()
print("Elapsed", ss/ Na, pydatetime.datetime.now().timestamp()-ts)

'''
# 배정 결과의 예
for i in range(len(B)):
	pp =Sname[i]+"("+str(B[i].pq.qsize())+"): "
	while (B[i].pq.empty()==False):
		pp = pp+ " "+ B[i].pq.get()[2].name
	print(pp)
'''