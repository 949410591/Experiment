#!/usr/bin/python3
from multiprocessing import Process,Queue
import sys
import csv
import os.path
#test command class
class Args:
	def __init__(self):
		l = sys.argv[1:]
		self.c = l[l.index('-c')+1]
		self.d = l[l.index('-d')+1]
		self.o = l[l.index('-o')+1]
args = Args()
class Config:
	def __init__(self):
		self.config = self._haha()
	def _haha(self):
		d = {'s': 0}
		with open(args.c) as f:
			for i in f.readlines():
				l = i.split('=')
				a, b = l[0].strip(), float(l[1])
				if a == 'JiShuL' or a == 'JiShuH':
					d[a] = b
				else:
					d['s'] += b
		return d
config = Config().config
#print(config)

def hanhan(salary):
	lis = []
	#shuiqian jishu
	shuiqian = int(salary)
	#baoxian
	jishul = config["JiShuL"]
	jishuh = config["JiShuH"]
	baoxian = shuiqian * config["s"]
	if shuiqian  <= jishul:
		baoxian = jishul * config["s"]
	elif shuiqian  >= jishuh:
		baoxian =  jishuh * config["s"]

	#shui
	shuij = shuiqian - baoxian - 3500
	if shuij <= 0:
		shui = 0
	elif shuij <= 1500:
		shui = shuij * 0.03
	elif shuij <= 4500:
		shui = shuij * 0.1 - 105
	elif shuij <= 9000:
		shui = shuij * 0.2 - 555
	elif shuij <= 35000:
		shui = shuij * 0.25 - 1005
	elif shuij <= 55000:
		shui = shuij * 0.3 - 2755
	elif shuij <= 80000:
		shui = shuij * 0.35 - 5505
	else:
		shui = shuij * 0.45 - 13505
	#shuihou
	shuihou = shuiqian -baoxian - shui 
	#xxxx.xx
	return [shuiqian,format(baoxian,".2f"),format(shui,".2f"),format(shuihou,".2f")]



class UserData:
	def __init__(self):
		self.user = self._userdata()
	def _userdata(self):
		with open(args.d) as f:
			dic = {}
			reader = csv.reader(f)
			for i in reader:
				dic[i[0]] = i[1]
			return dic
userdata = UserData().user

class GonZi:
	def __init__(self):
		self.gongzi = self.count_money()
	def count_money(self):
		lic = []
		for i in userdata.keys():
			a = hanhan(userdata[i])
			a.insert(0,i)
			lic.append(a)
		return lic
	def write(self):
		with open(args.o,"w") as f:
			writer = csv.writer(f)
			writer.writerows(self.gongzi)
def son1(queue1):
	pass
def son2(queue1,queue2):
	pass
def son3(queue2):
	GonZi().write()
queue1 = Queue()
queue2 = Queue()
def main():
	Process(target = son1,args = (queue1,)).start()	
	Process(target = son2,args = (queue1,queue2,)).start()
	Process(target = son3,args = (queue2,)).start()
		
if __name__ == "__main__":
	args = Args()
	main()
