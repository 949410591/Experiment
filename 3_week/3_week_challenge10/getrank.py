from pymongo import MongoClient,DESCENDING,ASCENDING
import sys
db = MongoClient("127.0.0.1",27017).shiyanlou

	

def get_rank(user_id):
	#he bing
	data1 = db.contests.find().sort('user_id',DESCENDING)
	num = data1[0]['user_id']
	for i in range(1,num+1):
		user = db.contests.find({'user_id':i})
		if user.count() - 1 :
			score = 0
			submit_time = 0
			for data in user:
				#print(data)	
				score += data['score']
				submit_time += data['submit_time']

			db.result.insert_one({'user_id':i,'score':score,'submit_time':submit_time})
			#print(i,score,submit_time)
		else:
			db.result.insert_one(user[0])

	#pai xu
	data2 = db.result.find().sort([('score',DESCENDING),('submit_time',ASCENDING)])
	n = 1
	for i in data2:
		db.result.update_one({'user_id':i['user_id']},{'$set':{"pai":n}})
		n += 1

	#cha xun
	user = db.result.find_one({'user_id':user_id})
	db.result.drop()
	return user['pai'],user['score'],user['submit_time']
		
	
	
		
if __name__ == '__main__':
	user_id = int(sys.argv[1])
	try :
		if not db.contests.find_one({'user_id':user_id}):
			print("Parameter Error")
			sys.exit()
	except:
			print("Parameter Error")
			sys.exit()
	
	userdata = get_rank(user_id)
	print(userdata)

