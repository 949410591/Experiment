from pymongo import MongoClient,DESCENDING,ASCENDING
import sys
from bson.son import SON
db = MongoClient("127.0.0.1",27017).shiyanlou

def get_rank(user_id):
	a = db.contests.aggregate( 
		[
		{'$group':{
			'_id':'$user_id',
			'score':{'$sum':"$score"},
			'submit_time':{'$sum':"$submit_time"}
			}
		},
		{
		'$project':{
			"user_id":"$_id",
			'_id':0,
			'score':1,
			'submit_time':1}
		},
		{'$sort':SON([('score',-1),('submit_time',1)])}

		])

	for n, a in enumerate(a):
		if a['user_id'] == user_id:
			return n+1, a["score"], a['submit_time']

	
	
	


#return user['pai'],user['score'],user['submit_time']
		
	
	
		
if __name__ == '__main__':
	try :
		user_id = int(sys.argv[1])
		assert db.contests.find_one({'user_id':user_id})
	except:
			print("Parameter Error")
			sys.exit()
	
	userdata = get_rank(user_id)
	print(userdata)