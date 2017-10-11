from firebase import firebase
import json
firebase = firebase.FirebaseApplication('https://projectfor551.firebaseio.com/', None)
result = firebase.get('/users', None)
print result
with open ("yelpb.json", "r") as f:
    dt = json.loads(f)
print dt['businesses'][0]

#x = {"rating": 4.5, "review_count": 149, "name": "Hungry Crowd", "transactions": [], "url": "https://www.yelp.com/biz/hungry-crowd-los-angeles?adjust_creative=bmFdLS5PddDOCsE7ICo79Q&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=bmFdLS5PddDOCsE7ICo79Q", "price": "$$", "distance": 10438.718545766465, "coordinates": {"latitude": 34.151896, "longitude": -118.352076}, "phone": "+18188537858", "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/zSNeAyqZlWHMrwKuin2Bbg/o.jpg", "categories": [{"alias": "newamerican", "title": "American (New)"}, {"alias": "breakfast_brunch", "title": "Breakfast & Brunch"}, {"alias": "tapasmallplates", "title": "Tapas/Small Plates"}], "display_phone": "(818) 853-7858", "id": "hungry-crowd-los-angeles", "is_closed": False, "location": {"city": "Los Angeles", "display_address": ["10140 Riverside Dr", "Los Angeles, CA 91602"], "country": "US", "address2": None, "address3": "", "state": "CA", "address1": "10140 Riverside Dr", "zip_code": "91602"}}
#firebase.post('/restaurants', x)
#firebase.put('/restaurants',"number3",x)
