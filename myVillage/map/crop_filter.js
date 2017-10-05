var list=[]
var totalArea=0

for(j in cropList){
	if(j["id"]==i){
		list.append(j)
		totalArea=totalArea+j["area"]
	}
}
